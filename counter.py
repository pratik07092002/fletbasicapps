import flet as ft

def main(page: ft.Page):
    page.title = "Counter App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    txt_number = ft.TextField(value = "0",text_align= ft.TextAlign.RIGHT,width=50)
    
    
    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()
    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()
        
    page.add(
        ft.Row(
            alignment= ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(ft.icons.REMOVE , on_click= minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD , on_click= plus_click)
            ]
        )
    )        
ft.app(target=main)
    