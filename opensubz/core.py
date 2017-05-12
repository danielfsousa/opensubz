import os
import shutil
import tempfile
import zipfile

import requests

from opensubtitles.opensubtitles import OpenSubtitles
from opensubtitles.utils import File
from opensubz.config import Config


class OpenSubz(object):

    @staticmethod
    def search(path, language='eng'):
        print('Starting OpenSubz...\n')
        print(path)
        print('\nSearching for subtittles...')

        result = OpenSubz._download_by_hash(path, language)

        if result['arq_video'] == 0:
            print('\nI haven\'t found any video file.\n')

        if len(result['nao_achou']) > 0:
            print('\nI haven\'t found any subtitle that fits these video files:\n')
            for file in result['nao_achou']:
                print(os.path.basename(file))
            print('\nTrying to get all subtitles...')
            OpenSubz._download_by_name(result['nao_achou'], language)

        input('\nPress any key to exit.')

    @staticmethod
    def _get_opensubs_token(open_subtitles):
        opensubs_token = None
        err = True
        config = Config()
        while err:
            try:
                opensubs_token = open_subtitles.login(config.email, config.password)
                if opensubs_token is not None:
                    err = False
            except Exception as e:
                print('\nAn error occurred while trying to get the opensubtitles token. Trying again...')
                print(e)
                continue

        return opensubs_token

    @staticmethod
    def _search_opensubtitles(open_subtitles, params):
        err = True
        tries = 0
        while err:
            try:
                data = open_subtitles.search_subtitles(params)
                err = False
                return data
            except:
                if tries > 5:
                    exit()
                print('\nSubtitle not found. Trying again...')
                tries += 1
                continue

    @staticmethod
    def _save_subtitles(links, diretorio):
        try:
            res = requests.get(links[0]['download'])
            res.raise_for_status()

            temp = tempfile.mkdtemp()

            nome_legenda_original = links[0]['nome-original']
            nome_legenda_zip = links[0]['nome-arquivo'][:-4] + '.zip'
            nome_legenda = links[0]['nome-arquivo'][:-4] + '.srt'
            dir_zip = os.path.join(temp, nome_legenda_zip)

            print('\nDownloading subtitle... ' + links[0]['nome-arquivo'])
            zipado = open(dir_zip, 'wb')
            for chunk in res.iter_content(8192):
                zipado.write(chunk)
            zipado.close()

            with zipfile.ZipFile(dir_zip, "r") as z:
                z.extractall(temp)

            shutil.move(os.path.join(temp, nome_legenda_original), os.path.join(diretorio, nome_legenda))
            shutil.rmtree(temp)
        except Exception as e:
            print('\nError while saving the subtitle. ' + str(e))

    @staticmethod
    def _download_by_hash(diretorio, language):
        sub = OpenSubtitles()
        token = OpenSubz._get_opensubs_token(sub)
        arq_video = 0
        nao_achou = []

        if token:
            for pastas, subpastas, nome_arquivos in os.walk(diretorio):
                for nome_arquivo in nome_arquivos:
                    if nome_arquivo.endswith('.mkv') or nome_arquivo.endswith('.mp4') or nome_arquivo.endswith('.avi'):
                        arq_video += 1

                        legenda = nome_arquivo[:-4] + '.srt'
                        if os.path.isfile(os.path.join(pastas, legenda)):
                            print('\nYou\'ve already downloaded the subtitle: ' + legenda + '. Let\'s skip this.')
                            continue

                        f = File(os.path.join(pastas, nome_arquivo))
                        fhash = f.get_hash()
                        if fhash:
                            links = []
                            size = f.size
                            data = OpenSubz._search_opensubtitles(sub, [
                                {'sublanguageid': language, 'moviefhash': fhash, 'moviebytesize': size}])

                            if len(data) == 0:
                                nao_achou.append(os.path.join(pastas, nome_arquivo))
                                print('I haven\'t found the subtitle for "%s"' % nome_arquivo)
                                continue

                            for subtitle in data:
                                links.append({'nome-original': subtitle['SubFileName'], 'nome-arquivo': nome_arquivo,
                                              'download': subtitle['ZipDownloadLink']})

                            OpenSubz._save_subtitles(links, pastas)
                        else:
                            print('Error getting the file hash: "%s"' % nome_arquivo)
            return {'arq_video': arq_video, 'nao_achou': nao_achou}
        else:
            print('Error getting opensubtitles token.')

    @staticmethod
    def _download_by_name(arquivos, language):
        if len(arquivos) > 0:
            sub = OpenSubtitles()
            token = OpenSubz._get_opensubs_token(sub)

            if token:
                for arquivo in arquivos:
                    NOME = os.path.basename(arquivo)
                    DIRETORIO = os.path.dirname(arquivo)

                    data = OpenSubz._search_opensubtitles(sub, [
                        {'sublanguageid': language, 'query': NOME}])

                    if len(data) > 0:
                        print('\nI have found these subtitles:\n')

                        for i, legenda in enumerate(data):
                            print('%d. Name: %s. Downloads: %s. Author: %s' %
                                  (i, legenda['SubFileName'], legenda['SubDownloadsCnt'], legenda['UserNickName']))

                        print('\nDigit the subtitle number you want to download.')
                        num = input('> ')

                        if num.isdigit():
                            num = int(num)
                            links = [{'nome-original': data[num]['SubFileName'], 'nome-arquivo': NOME,
                                      'download': data[num]['ZipDownloadLink']}]

                            OpenSubz._save_subtitles(links, DIRETORIO)
                    else:
                        print('\nSorry, I could not find subtitles for: %s' % NOME)
