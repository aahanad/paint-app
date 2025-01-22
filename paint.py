from tkinter import* 
from tkinter.colorchooser import askcolor
class Paint(object):
    def __init__ (self):
        self.screen=Tk()
        self.screen.geometry("600x600")
        self.pen=Button(self.screen,text="pen",fg="black",bg="white",font=("Brush Script",10),command=self.use_pen)
        self.pen.place(x=100,y=50)
        self.brush=Button(self.screen,text="brush",fg="black",bg="white",font=("Brush Script",10),command=self.use_brush)
        self.brush.place(x=180,y=50)
        self.colord=Button(self.screen,text="color",fg="black",bg="white",font=("Brush Script",10),command=self.choose_color)
        self.colord.place(x=240,y=50)
        self.eraser=Button(self.screen,text="eraser",fg="black",bg="white",font=("Brush Script",10),command=self.choose_eraser)
        self.eraser.place(x=310,y=50)
        self.clear=Button(self.screen,text="clear",fg="black",bg="white",font=("Brush Script",10),command=self.clear_all)
        self.clear.place(x=40,y=50)
        self.width=Scale(self.screen,from_=1,to=20,orient=HORIZONTAL)
        self.width.place(x=420,y=35)
        self.canvas=Canvas(self.screen,bg="white",width=600,height=600)
        self.canvas.place(x=0,y=80)
        self.pensize=3
        self.color="black"
        self.setup()
        self.screen.mainloop()
    def setup (self):
        self.active_Button=self.pen
        self.eraser_on=False
        self.oldx=None
        self.oldy=None
        self.canvas.bind("<B1-Motion>",self.paint)
        self.canvas.bind("<ButtonRelease-1>",self.reset)
    def use_pen(self):
        self.activate_button(self.pen)
    def use_brush(self):
        self.activate_button(self.brush)
        self.line_width=self.width.get()+5
    def choose_color(self):
        self.eraser_on=False
        self.color=askcolor(color=self.color)[1]
    def choose_eraser(self):
        self.activate_button(self.eraser,eraser_mode=True)
    def activate_button(self,btn,eraser_mode=False):
        self.active_Button.config(relief=RAISED)
        btn.config(relief=SUNKEN)
        self.active_Button=btn
        self.eraser_on=eraser_mode
    def paint(self,event):
        self.line_width=self.width.get()
        paint_color="white" if self.eraser_on else  self.color
        if self.active_Button==self.brush:
             self.line_width=self.width.get()+5
        else:   
            self.line_width=self.width.get()

          

        if self.oldx and self.oldy:
            self.canvas.create_line(self.oldx,self.oldy,event.x,event.y,width=self.line_width,fill=paint_color,smooth=TRUE,splinesteps=36,capstyle=ROUND)

        self.oldx=event.x
        self.oldy=event.y
    def reset(self,event):
        self.oldx=None
        self.oldy=None
    def clear_all(self):
        self.canvas.delete("all")
Paint()
#complete last weeks