import dearpygui.dearpygui as pygui

def Start():
    pygui.set_global_font_scale(2)

def Set_Theme():
    with pygui.theme() as global_theme:
        with pygui.theme_component(pygui.mvAll):
            pygui.add_theme_color(pygui.mvThemeCol_FrameBg,
                                  (255, 140, 23),
                                  category=pygui.mvThemeCat_Core
                                  )
            pygui.add_theme_style(pygui.mvStyleVar_FrameRounding,
                                  5,
                                  category=pygui.mvThemeCat_Core
                                  )

        with pygui.theme_component(pygui.mvInputInt):
            pygui.add_theme_color(
                pygui.mvThemeCol_FrameBg,
                (140, 255, 23),
                category=pygui.mvThemeCat_Core
            )
            pygui.add_theme_style(pygui.mvStyleVar_FrameRounding,
                                  5,
                                  category=pygui.mvThemeCat_Core
                                  )

def Set_Font_Default():
    with pygui.font_registry():
        font = pygui.add_font("Settings/Lato/Lato-Thin.tff", 50)
    return font


def Set_Font(path):
    with pygui.font_registry():
        font = pygui.add_font(path, 20)
    return font


