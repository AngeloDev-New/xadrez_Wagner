import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Cores (convertendo hexadecimal para RGB)
def hex_to_rgb(hex_color):
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

blackColor = hex_to_rgb('a77a51')
whiteColor = hex_to_rgb('dfbf96')

# Tamanho do tabuleiro e da janela
tabuleiro = (8, 8)
window_size = (600, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Tabuleiro de Xadrez com Rainha")

# Tamanho de cada célula
cell_width = window_size[0] // tabuleiro[0]
cell_height = window_size[1] // tabuleiro[1]

# Carregar imagens
queen_img = pygame.image.load("assets/rainha.png")
block_img = pygame.image.load("assets/block.png")

# Redimensionar imagens
queen_img = pygame.transform.scale(queen_img, (cell_width, cell_height))
block_img = pygame.transform.scale(block_img, (cell_width, cell_height))

# Posições iniciais
rainha_pos = (0, 0)
block_pos = (1, 1)

def colocarRainha(pos):
    linha, coluna = pos
    x = coluna * cell_width
    y = linha * cell_height
    screen.blit(queen_img, (x, y))

def colocarBlock(pos):
    linha, coluna = pos
    x = coluna * cell_width
    y = linha * cell_height
    screen.blit(block_img, (x, y))
class position:
    def __init__(self, position):
        self.position = position
        self.block = False
        self.queen = False

class Tabuleiro:
    def __init__(self):
        self.positions = [[position((x,y)) for y in range(8)] for x in range(8)]
        self.posibilits = 64
        self.searchQueens()

    @staticmethod
    def blocksFromPoint(point):
        def diagonalPrincipal(point):
            line, col = point
            result = []
            for offset in range(-7, 8):
                new_line = line + offset
                new_col = col + offset
                if 0 <= new_line < 8 and 0 <= new_col < 8 and (new_line, new_col) != point:
                    result.append((new_line, new_col))
            return result

        def diagonalSecundaria(point):
            line, col = point
            result = []
            for offset in range(-7, 8):
                new_line = line + offset
                new_col = col - offset
                if 0 <= new_line < 8 and 0 <= new_col < 8 and (new_line, new_col) != point:
                    result.append((new_line, new_col))
            return result

        def horizontal(point):
            line = point[0]
            colun_else = point[1]
            return [(line, colun) for colun in range(8) if colun != colun_else]

        def vertical(point):
            line_else = point[0]
            colun = point[1]
            return [(line, colun) for line in range(8) if line != line_else]

        return (
            vertical(point)
            + horizontal(point)
            + diagonalPrincipal(point)
            + diagonalSecundaria(point)
        )

    def getPoints(self):
        # Solução clássica para o problema das 8 rainhas
        def sequence():
            for a in range(8):
                for b in range(8):
                    for c in range(8):
                        for d in range(8):
                            for e in range(8):
                                for f in range(8):
                                    for g in range(8):
                                        for h in range(8):
                                            for i in range(8):
                                                for j in range(8):
                                                    for k in range(8):
                                                        for m in range(8):
                                                            for n in range(8):
                                                                for o in range(8):
                                                                    for p in range(8):
                                                                        for q in range(8):
                                                                            yield (a,b,c,d,e,f,g,h,i,j,k,m,n,o,p,q)
        def queensAlive(a,b,c,d,e,f,g,h,i,j,k,m,n,o,p,q):
            points = [
                    (a, b),
                    (c, d),
                    (e, f),
                    (g, h),
                    (i, j),
                    (k, m),
                    (n, o),
                    (p, q)
            ]
            print(points)
            # def blocksFromPoint(point):
            for point in points:
                for poinB in points:
                    if poinB in self.blocksFromPoint(point) or point == poinB:
                        return False
            return True
        for a,b,c,d,e,f,g,h,i,j,k,m,n,o,p,q in sequence():
            if queensAlive(a,b,c,d,e,f,g,h,i,j,k,m,n,o,p,q):
                yield [
                    (a, b),
                    (c, d),
                    (e, f),
                    (g, h),
                    (i, j),
                    (k, m),
                    (n, o),
                    (p, q)
                ]
        # [
        #     (0, 0),
        #     (1, 4),
        #     (2, 7),
        #     (3, 5),
        #     (4, 2),
        #     (5, 6),
        #     (6, 1),
        #     (7, 3)
        # ]

    def searchQueens(self):
  
        for points in self.getPoints():
            self.eigthQueen = [(point, self.blocksFromPoint(point)) for point in points]
            break
      


tb = Tabuleiro()
# Loop principal
running = True
while running:
    screen.fill((0, 0, 0))  # fundo preto

    # Desenhar tabuleiro
    for linha in range(tabuleiro[0]):
        for coluna in range(tabuleiro[1]):
            cor = whiteColor if (linha + coluna) % 2 == 0 else blackColor
            rect = pygame.Rect(coluna * cell_width, linha * cell_height, cell_width, cell_height)
            pygame.draw.rect(screen, cor, rect)

    # Desenhar a rainha e o bloco
    # Logica para colocar rainhas e bloqueios
    
    for position,blocks in tb.eigthQueen:
        colocarRainha(position)
        for block in blocks:
            colocarBlock(block)


    pygame.display.flip()

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
