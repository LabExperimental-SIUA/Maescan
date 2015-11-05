import polib
import os


class PoParser:

    @staticmethod
    def compile_po_files():
        locale_path = os.getcwd() + '/i18n/locale'
        langs = os.listdir(locale_path)
        for lang in langs:
            path = './i18n/locale/' + lang + '/LC_MESSAGES/messages'
            po = polib.pofile(path + '.po')
            po.save_as_mofile(path + '.mo')
