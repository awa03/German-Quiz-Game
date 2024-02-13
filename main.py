import dearpygui.dearpygui as pygui
import Windows.Primary as primary
import Settings.Fonts as fonts
import Settings.User_Settings as settings
import Windows.Frame_Updates_Main.Update as update

pygui.create_context()

# Default Profile
fonts.Start()
fonts.Set_Theme()
primary.Start()

# Editable User Settings
user_settings_instance = settings.user_settings()
settings.Apply_Settings(user_settings_instance)

# Update Function
while pygui.is_dearpygui_running():
    pygui.render_dearpygui_frame()
    update.on_frame_change()

pygui.create_viewport(title='German Quiz', width=1280, height=720)
pygui.setup_dearpygui()
pygui.show_viewport()
pygui.set_primary_window("Primary Window", True)
pygui.start_dearpygui()
pygui.destroy_context()

