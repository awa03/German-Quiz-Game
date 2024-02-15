import dearpygui.dearpygui as pygui
def Add_Menu_Bar(parent_window):
  with pygui.viewport_menu_bar():
    with pygui.menu(label="File", parent=parent_window):
        pygui.add_menu_item(label="Save", parent=parent_window)
        pygui.add_menu_item(label="Save As", parent=parent_window)

    with pygui.menu(label="Settings", parent=parent_window):
        pygui.add_menu_item(label="Setting 1", check=True, parent=parent_window)
        pygui.add_menu_item(label="Setting 2", parent=parent_window)

def temp(sender, app_data):
    print("Menu Item Clicked")
