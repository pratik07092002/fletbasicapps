import flet as ft 
import os 
def main(page:ft.Page):
    r = ft.Row(wrap=True , scroll= "always" , expand= True)
    page.add(r)
    
    for i in range(200):
        r.controls.append(
            
            
            ft.Container(
                ft.Text(f"Item {i}"),
                height=100,
                width=100,
                alignment= ft.alignment.center,
                bgcolor= ft.colors.RED,
                border_radius= ft.border_radius.all(5)
            )
        )
        page.update()
ft.app(target=main)        