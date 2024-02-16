# singleton for user dearpygui setting 

import dearpygui.dearpygui as pygui 
class user_settings:
    def __init__(self):
        self.theme = "Default"
        self.theme_color = (255, 140, 23)
        self.theme_style = 5
        self.theme_color_input = (140, 255, 23)
        self.theme_style_input = 5
        self.theme_color_button = (140, 255, 23)
        self.theme_style_button = 5
        self.theme_color_text = (140, 255, 23)

def Apply_Settings(user_settings):
    with pygui.theme() as global_theme:
        with pygui.theme_component(pygui.mvAll):
            pygui.add_theme_color(pygui.mvThemeCol_FrameBg, user_settings.theme_color, category=pygui.mvThemeCat_Core)
            pygui.add_theme_style(pygui.mvStyleVar_FrameRounding, user_settings.theme_style, category=pygui.mvThemeCat_Core)

        with pygui.theme_component(pygui.mvInputInt):
            pygui.add_theme_color(pygui.mvThemeCol_FrameBg, user_settings.theme_color_input, category=pygui.mvThemeCat_Core)
            pygui.add_theme_style(pygui.mvStyleVar_FrameRounding, user_settings.theme_style_input, category=pygui.mvThemeCat_Core)

        with pygui.theme_component(pygui.mvButton):
            pygui.add_theme_color(pygui.mvThemeCol_Button, user_settings.theme_color_button, category=pygui.mvThemeCat_Core)
            pygui.add_theme_style(pygui.mvStyleVar_FrameRounding, user_settings.theme_style_button, category=pygui.mvThemeCat_Core)

        with pygui.theme_component(pygui.mvText):
            pygui.add_theme_color(pygui.mvThemeCol_Text, user_settings.theme_color_text, category=pygui.mvThemeCat_Core)
            
def Modify_Settings(user_settings, theme, theme_color, theme_style, theme_color_input, theme_style_input, theme_color_button, theme_style_button, theme_color_text):
    user_settings.theme = theme
    user_settings.theme_color = theme_color
    user_settings.theme_style = theme_style
    user_settings.theme_color_input = theme_color_input
    user_settings.theme_style_input = theme_style_input
    user_settings.theme_color_button = theme_color_button
    user_settings.theme_style_button = theme_style_button
    user_settings.theme_color_text = theme_color_text
    Apply_Settings(user_settings)

# Theme Options - Default, Dark, Light, Classic, Grey, Dark 2, Light 2, Grey 2
def Set_Theme(user_settings, theme):
    pygui.set_global_font_scale(10)
    user_settings.theme = theme
    Apply_Settings(user_settings)
