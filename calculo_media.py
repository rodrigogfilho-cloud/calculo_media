import flet as ft
from component.classe_campo_nota import Campo_nota

def main(pagina:ft.Page):
    pagina.window.width = 600
    pagina.window.height= 700
    pagina.title = "Cálculo Média"
    pagina.horizontal_alignment = "center"
     

    titulo = ft.Text(value="Cálculo Média",
                     size= 30,
                     font_family="Times New Roman")

    lista_campos_notas = []

    def adicionar_campo_nota():
        lista_campos_notas.append(Campo_nota())

    def calcular_media():
        soma_notas = 0
        contador_notas = 0
        for campo in lista_campos_notas:
            nota = float(campo.value)
            soma_notas += nota
            contador_notas += 1
            resultado.value = round(soma_notas / contador_notas,2)

    def excluir ():

        copia_lista = lista_campos_notas.copy()
        for x in copia_lista:
            if x.caixa_selecao.value == True:
                lista_campos_notas.remove(x)
            

    botao_add = ft.FloatingActionButton(icon=ft.Icons.ADD,
                                        on_click=adicionar_campo_nota)

    botao_excluir_notas = ft.FloatingActionButton(icon= ft.Icons.DELETE_FOREVER,
                                                  on_click = excluir)

    linha_botoes =  ft.Row(controls = [botao_add,botao_excluir_notas],
                              alignment="center") #Linha de botões para adicionar nota e excluir nota

    coluna_notas = ft.Column(controls=lista_campos_notas,
                             expand=True,
                             wrap=True,
                             scroll=ft.ScrollMode.AUTO,
                             )

    botao_calcular = ft.Button(content="Calcular",
                               on_click=calcular_media)

    resultado = ft.TextField(value=0,
                             read_only=True,
                             )

    
        

    linha_resultado = ft.Row(controls=[botao_calcular,resultado],
                             alignment="center",
                             width = 440)


    container_resultado = ft.Container(content=linha_resultado,
                                       bgcolor = "#85d2ff",
                                    padding = 2,
                                    border = ft.Border.all(2),
                                    border_radius = 10,
                                    )
    
    pagina.controls = [titulo,
                       linha_botoes,
                       coluna_notas,
                       container_resultado,
                       ]
    
ft.run(main)