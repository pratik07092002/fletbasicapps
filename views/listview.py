import flet as ft 

def main(page: ft.Page):
    lv = ft.ListView(expand=True , spacing= 15 )
    for i in range(200):
        lv.controls.append(ft.Text(f"Line {i}"))
    page.add(lv)
    
ft.app(target=main)        
    