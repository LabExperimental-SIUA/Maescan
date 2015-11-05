from gettext import translation


class LanguageController:

    def __init__(self, p_env):
        self.env = p_env

    def change_language(self, lang):
        translations = translation(domain='messages', localedir='./i18n/locale', languages=[lang])
        self.env.install_gettext_translations(translations)
        return self.env.get_template('index.jade').render()

