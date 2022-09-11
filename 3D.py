import GameWidgets
import pygame
pygame.init()
master=GameWidgets.ScreenCommands.Screen(Color=GameWidgets.Colors.White,Icon='OctaveEditor.png')
screen=master.Return()
master.Register_Master(screen)
master.Set_Icon()
red=GameWidgets.Colors.Red
blue=GameWidgets.Colors.Blue
green=GameWidgets.Colors.Green
white=GameWidgets.Colors.White
black=GameWidgets.Colors.black
text='''3D Cube With Polygons!'''
btn=GameWidgets.Btn.Active_Btn(screen,Colors=(red,green,blue,black,white),X=0,Y=300,text=text,Size=32)
run=True
while run:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            run=False
        btn.Detect(pygame.mouse.get_pos(),e)
    master.Fill()
    btn.Draw()
    pygame.draw.polygon(screen,GameWidgets.Colors.gray_grey,((100,120),(150,150),(100,180),(50,150)))
    pygame.draw.polygon(screen,GameWidgets.Colors.dim_gray_dim_grey,((100,180),(150,150),(150,200),(100,230)))
    pygame.draw.polygon(screen,GameWidgets.Colors.dark_gray_dark_grey,((100,180),(100,230),(50,200),(50,150)))
    pygame.display.update()
pygame.quit()
