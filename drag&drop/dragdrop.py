import flet as ft 

def main(page: ft.Page):
    page.title = "Drag and Drop"
    
    def drag_accept(e):
        src = page.get_control(e.src_id)
        
        src.content.content.value = "0"
        
        e.control.content.content.value = "1"
        page.update()
        
    page.add(
        ft.Row(
            [
                ft.Draggable(
                    group="number",
                    content= ft.Container(
                        width= 50,
                        height= 50 ,
                        bgcolor= ft.colors.CYAN,
                        border_radius=5,
                        content= ft.Text(
                            "1", size=20
                        )
                    )
                ),
                ft.Container(width=50),
                ft.DragTarget(
                    group="number",
                    content= ft.Container(
                        width=50,
                        height=50,
                        bgcolor= ft.colors.AMBER,
                        border_radius= 5,
                        content= ft.Text("0" , size=20),
                        
                    ),
                on_accept=drag_accept
                ),
            
                
            ]
        )
    )    
    
    
ft.app(target=main)    