import flet as ft


def main(page: ft.Page):
    c_dropdown = ft.Dropdown(options=[
        ft.dropdown.Option("Blue"),
        ft.dropdown.Option("Red")
    ])
    col = ft.Column(
       
    )
    def btn_click(e):
        col.controls.append(ft.Text(f" Selected Color is {c_dropdown.value}"))
        page.update()
    sub_btn = ft.ElevatedButton("Click Here" , on_click= btn_click)
    page.add(c_dropdown , sub_btn , col)
        
    
ft.app(target= main)    
