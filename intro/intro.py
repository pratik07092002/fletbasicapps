import flet as ft
import time
def main(page:ft.Page):
    
#    t  = ft.Text(value="Hello Screen" , color='Green')
#   page.controls.append(t)
#    page.update()
#    t = ft.Text()
#    page.add(t)
    
    for i in range(10):
#        t.value = f"step {i}"
#        page.update()
#        time.sleep(1)
# i ind[0]
# 6  0 
# 7  1
# 8  2 
# 9  3
        page.controls.append(ft.Text(f"line {i}"))
        if i>5:
            page.controls.pop(0)
        page.update()
        time.sleep(1)
            
        
    
ft.app(target=main)