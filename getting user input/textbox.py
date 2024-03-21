import flet as ft 

def main(page):
    name = ft.TextField(hint_text= "name")
    def but_click(e):
        if not name.value:
            name.error_text = "please enter text"
        else:
            
            page.add(ft.Text(f"Hello {name.value}"))    
    page.add(name, ft.ElevatedButton("Click here" , on_click= but_click))
ft.app(target= main)            