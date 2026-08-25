import flet as ft

class Campo_nota(ft.Row):
    def __init__(self):
        super().__init__()

        self.caixa_texto = ft.TextField (label="Nota",
                                    filled=True)
        
        self.caixa_selecao = ft.Checkbox(on_change=self.alterar_cor)

       #ft.Row = serve para fazer itens (por ex: TextField, Checkbox) ficarem em uma linha

        self.estilo_caixa_selecao = ft.Container(content=ft.Row(controls= [self.caixa_texto,self.caixa_selecao],),
                                           bgcolor="#2f9aff",
                                           border= ft.Border.all(5, color="#0011ff"),
                                           border_radius=10,
                                           padding=10,
                                           animate=ft.Animation(duration=500, 
                                                                curve=ft.AnimationCurve.EASE_IN_TO_LINEAR,
                                                                ))

        self.controls = [self.estilo_caixa_selecao]

    def alterar_cor(self):

        if self.caixa_selecao.value == False:
                    self.estilo_caixa_selecao.bgcolor = "#2f9aff"
        else:
            self.estilo_caixa_selecao.bgcolor = "#4ce9fd"

    @property
    def value(self):
          return self.caixa_texto.value

       

   
  