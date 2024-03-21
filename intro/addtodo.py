import flet as ft 
"""
def main(page):
    def add_clicked():
        page.add(ft.Checkbox(label= new_task.value))
        new_task.value = ""
        new_task.focus()
        
        new_task.update()
    new_task = ft.TextField(hint_text="Add todo")
    new_task.disabled = True
    page.add(ft.Row(controls=[new_task, ft.ElevatedButton("Add" , on_click= add_clicked )]))
    
ft.app(target=main)        
""" 
# adding name in app ui 
def main(page):
    first_name = ft.TextField(autofocus= True)
    last_name = ft.TextField()
    c= ft.Column()
    
    def show_text(e):
        c.controls.append(ft.Text(f" hello {first_name.value} {last_name.value}"))
        page.update()
        
        
    page.add(
        first_name,
        last_name,
        ft.ElevatedButton( "Click" , on_click= show_text ),
        c 
    )
ft.app(target= main)