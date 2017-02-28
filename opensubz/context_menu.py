import winreg, os, sys

ICON_NAME = 'play.ico'

REG_PATH_BACKGROUND = r'Software\Classes\directory\Background\shell\opensubz'
REG_PATH_FOLDER = r'Software\Classes\directory\shell\opensubz'
ICON_PATH = '"' + os.path.join(sys.prefix, 'icon', 'play.ico') + '"'
PYTHON_SCRIPT_PATH = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), 'opensubz.exe')
SCRIPT_PATH_BACKGROUND = '"' + PYTHON_SCRIPT_PATH + '" "--search" "%V"'
SCRIPT_PATH_FOLDER = '"' + PYTHON_SCRIPT_PATH + '" "--search" "%1"'


def set_reg(name, value, reg_path):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0,
                                      winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(registry_key)
        return True
    except WindowsError as e:
        print(e)
        print('\nAn error occurred when trying to add the "Download Subtitles" shortcut to the context menu.')
        return False


def get_reg(name, reg_path):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0,
                                      winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None


def install():
    # Add keys to Registry
    set_reg('', 'Download Subtitles', REG_PATH_BACKGROUND)
    set_reg('Icon', ICON_PATH, REG_PATH_BACKGROUND)
    set_reg('', SCRIPT_PATH_BACKGROUND, REG_PATH_BACKGROUND + '\command')

    set_reg('', 'Download Subtitles', REG_PATH_FOLDER)
    set_reg('Icon', ICON_PATH, REG_PATH_FOLDER)
    set_reg('', SCRIPT_PATH_FOLDER, REG_PATH_FOLDER + '\command')

    print('\n"Download Subtitles" shortcut added to the Windows context menu.')


def uninstall():
    print('\nNot supported yet.')




