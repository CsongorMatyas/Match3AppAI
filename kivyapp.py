import mss
from PIL import Image
import numpy as np
from IPython.display import Image as Img
from IPython.display import display as Dsp
import pyautogui
import time
import urllib.request
from random import randint

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config
from kivy.core.window import Window

class Board(object):
    def __init__(self,
                 Size = 8,
                 G = None):
        self.Game = G
        self.Size = Size
        self.n = Size
        self.tol = G.tol
        
        sct_img, image_array = self.Game.Grab(self.Game.BoardP)
        #np.save('Board.npy', image_array)
        #mss.tools.to_png(sct_img.rgb, sct_img.size, output='mon-1.png')
        #np_Board = np.load("Board.npy")
        self.image_array = image_array
        
        self.Get_Empty_Grid()
        self.Grid_click_positions = self.Get_grid_click_pos()
        
        self.M3 = []
        self.M4 = []
        self.M5 = []
    
    def Get_Empty_Grid(self):
        EmptyGrid = []
        
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append([])
                
            EmptyGrid.append(row)
            
        self.EmptyGrid = EmptyGrid
    
    def Fill_empty_grid(self):
        tol = self.tol
        
        np_Board = self.image_array
        
        Grid = []
        for ROW in self.EmptyGrid:
            R_O_W = []
            for cell in ROW:
                R_O_W.append([])
            Grid.append(R_O_W)
        
        if self.Game.Type == 'N':
            Red    = [52.5, 14.5, 13.0]
            Green  = [18.0, 41.5, 10.5]
            Blue   = [13.0, 35.0, 50.5]
            Purple = [32.0, 10.0, 45.0]
            Yellow = [58.5, 49.0, 21.5]
            Brown  = [29.0, 20.5, 19.0]
            Skull  = [35.0, 34.5, 34.0]
            Skull5 = [50.0, 27.5, 23.0]

            leave = False

            for row in range(self.n):
                if leave:
                    continue

                for col in range(self.n):
                    if leave:
                        continue

                    R, G, B = 0, 0, 0

                    for r in range(20):
                        for c in range(20):
                            Pixel = np_Board[row * 46 + 13 + r][col * 46 + 13 + c]
                            R += Pixel[0]
                            G += Pixel[1]
                            B += Pixel[2]

                    if ((abs(Red[0] - (R / 1600)) < tol) and
                        (abs(Red[1] - (G / 1600)) < tol) and
                        (abs(Red[2] - (B / 1600)) < tol)):
                        if Grid[row][col] == []:
                            Grid[row][col] = 'Re'

                    elif ((abs(Green[0] - (R / 1600)) < tol) and
                          (abs(Green[1] - (G / 1600)) < tol) and
                          (abs(Green[2] - (B / 1600)) < tol)):
                        if Grid[row][col] == []:
                            Grid[row][col] = 'Gr'

                    elif ((abs(Blue[0] - (R / 1600)) < tol) and
                          (abs(Blue[1] - (G / 1600)) < tol) and
                          (abs(Blue[2] - (B / 1600)) < tol)):
                        if Grid[row][col] == []:
                            Grid[row][col] = 'Bl'

                    elif ((abs(Purple[0] - (R / 1600)) < tol) and
                          (abs(Purple[1] - (G / 1600)) < tol) and
                          (abs(Purple[2] - (B / 1600)) < tol)):
                        if Grid[row][col] == []:
                            Grid[row][col] = 'Pu'

                    elif ((abs(Yellow[0] - (R / 1600)) < tol) and
                          (abs(Yellow[1] - (G / 1600)) < tol) and
                          (abs(Yellow[2] - (B / 1600)) < tol)):
                        if Grid[row][col] == []:
                            Grid[row][col] = 'Ye'

                    elif ((abs(Brown[0] - (R / 1600)) < tol) and
                          (abs(Brown[1] - (G / 1600)) < tol) and
                          (abs(Brown[2] - (B / 1600)) < tol)):
                        if Grid[row][col] == []:
                            Grid[row][col] = 'Br'

                    elif ((abs(Skull[0] - (R / 1600)) < tol) and
                          (abs(Skull[1] - (G / 1600)) < tol) and
                          (abs(Skull[2] - (B / 1600)) < tol)):
                        if Grid[row][col] == []:
                            Grid[row][col] = 'Sk'

                    elif ((abs(Skull5[0] - (R / 1600)) < tol + 3) and
                          (abs(Skull5[1] - (G / 1600)) < tol + 3) and
                          (abs(Skull5[2] - (B / 1600)) < tol + 3)):
                        if Grid[row][col] == []:
                            Grid[row][col] = 'Sk'

                    else:
                        #time.sleep(5)
                        print('No match for this averaged pixel:')
                        print(R / 1600, G / 1600, B / 1600)
                        if self.Game.Check_for(self.Game.LeaveTH, 
                                               self.Game.np_LeaveTH):
                            leave = True
                            break
        
        elif self.Game.Type == 'TH':
            Copper = [9.45, 3.75, 2.70]
            Sylver = [6.45, 8.55, 9.43]
            Gold   = [12.82, 8.55, 2.58]
            RChest = [7.92, 4.47, 2.73]
            Purse  = [8.85, 6.27, 4.20]
            BChest = [8.65, 7.64, 7.08]
            GChest = [9.66, 8.80, 4.36]
            Vault  = [6.61, 4.50, 3.05]
            #8.11375 4.68 2.93625
            #7.886875 4.553125 2.825
            #7.906875 4.509375 2.765625
            #7.738125 4.26 2.5475
            #
            
            #6.605625 4.521875 3.0525
            #6.63125 4.494375 3.066875
            
            Pearl  = [179.0, 82.0, 111.0]
            
            leave = False

            for row in range(self.n):
                if leave:
                    continue

                for col in range(self.n):
                    if leave:
                        continue

                    R, G, B = 0, 0, 0

                    for r in range(10):
                        for c in range(10):
                            Pixel = np_Board[row * 46 + 18 + r][col * 46 + 18 + c]
                            R += Pixel[0]
                            G += Pixel[1]
                            B += Pixel[2]
                            if ((abs(Pearl[0] - Pixel[0]) < 20.0) and
                                (abs(Pearl[1] - Pixel[1]) < 20.0) and
                                (abs(Pearl[2] - Pixel[2]) < 20.0)):
                                Grid[row][col] = 'M'

                    if ((abs(Copper[0] - (R / 1600)) < tol) and
                        (abs(Copper[1] - (G / 1600)) < tol) and
                        (abs(Copper[2] - (B / 1600)) < tol)):
                        if Grid[row][col] == []:
                            Grid[row][col] = 'C'

                    elif ((abs(Sylver[0] - (R / 1600)) < tol) and
                          (abs(Sylver[1] - (G / 1600)) < tol) and
                          (abs(Sylver[2] - (B / 1600)) < tol)):
                        if Grid[row][col] == []:
                            Grid[row][col] = 'S'

                    elif ((abs(Gold[0] - (R / 1600)) < tol) and
                          (abs(Gold[1] - (G / 1600)) < tol) and
                          (abs(Gold[2] - (B / 1600)) < tol)):
                        if Grid[row][col] == []:
                            Grid[row][col] = 'G'

                    elif ((abs(RChest[0] - (R / 1600)) < tol) and
                          (abs(RChest[1] - (G / 1600)) < tol) and
                          (abs(RChest[2] - (B / 1600)) < tol)):
                        if Grid[row][col] == []:
                            Grid[row][col] = 'r'

                    elif ((abs(Purse[0] - (R / 1600)) < tol) and
                          (abs(Purse[1] - (G / 1600)) < tol) and
                          (abs(Purse[2] - (B / 1600)) < tol)):
                        if Grid[row][col] == []:
                            Grid[row][col] = 'P'

                    elif ((abs(BChest[0] - (R / 1600)) < tol) and
                          (abs(BChest[1] - (G / 1600)) < tol) and
                          (abs(BChest[2] - (B / 1600)) < tol)):
                        if Grid[row][col] == []:
                            Grid[row][col] = 'b'

                    elif ((abs(GChest[0] - (R / 1600)) < tol) and
                          (abs(GChest[1] - (G / 1600)) < tol) and
                          (abs(GChest[2] - (B / 1600)) < tol)):
                        if Grid[row][col] == []:
                            Grid[row][col] = 'g'

                    else:
                        #time.sleep(5)
                        print('No match for this averaged pixel:')
                        print(row, col, R / 1600, G / 1600, B / 1600)
                        if self.Game.Check_for(self.Game.LeaveTH, 
                                               self.Game.np_LeaveTH):
                            leave = True
                            break

        else:
            print('Incorrect game type was given!')
            
        return(Grid)
    
    def Get_grid_click_pos(self):
        Grid_click_positions = []
        for n in range(self.n):
            Row = []
            for m in range(self.n):
                Row.append([int(self.Game.BoardP['left'] + 
                                self.Game.BoardP['width'] / self.n * 2) + 
                                (self.Game.BoardP['width'] / self.n * m),
                            int(self.Game.BoardP['top'] + 
                                self.Game.BoardP['height'] / self.n * 2) + 
                                (self.Game.BoardP['height'] / self.n * n)])
            Grid_click_positions.append(Row)
        return(Grid_click_positions)
    
    def Check_grid(self, board = []):
        N = self.n
        
        Gem_value_dict = {'C' : 10, 'S' : 100, 'G' : 1000, 'P' : 10000, 
                          'b' : 100000, 'g' : 1, 'r' : 0,
                          'Re' : 1, 'Gr' : 1, 'Bl' : 1, 'Pu' : 1, 'Ye' : 1, 'Br' : 1, 'Sk' : 1,
                           0 : 0,  1 : 0,  2 : 0,  3 : 0,  4 : 0,  5 : 0,  6 : 0,  7 : 0,  8 : 0,  9 : 0, 
                          10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0, 15 : 0, 16 : 0, 17 : 0, 18 : 0, 19 : 0,
                          20 : 0, 21 : 0, 22 : 0, 23 : 0, 24 : 0, 25 : 0, 26 : 0, 27 : 0, 28 : 0, 29 : 0, 
                          30 : 0, 31 : 0, 32 : 0, 33 : 0, 34 : 0, 35 : 0, 36 : 0, 37 : 0, 38 : 0, 39 : 0}

        Grid = []
        for row in self.EmptyGrid:
            ROW = []
            for cell in row:
                ROW.append([])
            Grid.append(ROW)

        #Horizontal

        for row in range(N):
            for col in range(N - 2):
                if ((board[row][col] == board[row][col + 1]) and
                    (board[row][col] == board[row][col + 2])):
                    #print(row, col, 'H', board[row][col], board[row][col + 1], board[row][col + 2])
                    Grid[row][col].append('H')
                    Grid[row][col + 1].append('H')
                    Grid[row][col + 2].append('H')

        #Vertical
        for row in range(N - 2):
            for col in range(N):
                if ((board[row][col] == board[row + 1][col]) and
                    (board[row][col] == board[row + 2][col])):
                    #print(row, col, 'V', board[row][col], board[row + 1][col], board[row + 2][col])
                    Grid[row][col].append('V')
                    Grid[row + 1][col].append('V')
                    Grid[row + 2][col].append('V')

        ToF = False
        M4  = False #match 4 gems
        M5  = False #match 5 gems
        gem_counter = 0
        gem_score = 0
        removed_gems = {'Re' : 0, 'Gr' : 0, 'Bl' : 0, 'Pu' : 0, 'Ye' : 0, 'Br' : 0, 'Sk' : 0}

        for r, ROW in enumerate(Grid):
            for c, CELL in enumerate(ROW):
                if CELL != []:
                    gem_counter += 1
                    gem_score += Gem_value_dict[board[r][c]]
                    if board[r][c] in removed_gems:
                        removed_gems[board[r][c]] += 1
                        
                    if len(CELL) > 1:
                        not_same = False
                        linear_5 = False
                        if len(CELL) > 2:
                            linear_5 = True
                        for m in CELL:
                            if m != CELL[0]:
                                not_same = True
                        if not_same or linear_5:
                            M4 = True
                            M5 = True
                        else:
                            M4 = True
                    ToF = True
        
        return(ToF, M4, M5, gem_counter, gem_score, Grid, removed_gems)
    
    def Get_moves(self, board = []):
        M3, M4, M5 = [], [], []
        
        for row in range(self.Size):
            for col in range(self.Size):
                
                #Move Down
                if row < self.Size - 1:
                    if board[row][col] != board[row + 1][col]:
                        
                        board_copy = []
                        for ROW in board:
                            R_O_W = []
                            for cell in ROW:
                                R_O_W.append(cell)
                            board_copy.append(R_O_W)

                        FROM = board[row][col]
                        TO = board[row + 1][col]

                        board_copy[row][col] = TO
                        board_copy[row + 1][col] = FROM

                        M3_ToF, M4_ToF, M5_ToF, gem_counter, gem_score, matched_grid, removed_gems = self.Check_grid(board = board_copy)
                        
                        #'''
                        cascade_score = 0
                        cascade_gem_counter = 0
                        cascade_removed_gems = {'Re' : 0, 'Gr' : 0, 'Bl' : 0, 'Pu' : 0, 'Ye' : 0, 'Br' : 0, 'Sk' : 0}

                        board_after_move = self.Check_after_move(board, [row, col, row + 1, col], matched_grid)
                        ToF_, M4_, M5_, gem_counter_, gem_score_, matched_grid_, removed_gems_ = self.Check_grid(board = board_after_move)
                        
                        if M5_:
                            M5_ToF = True
                        
                        if M4_:
                            M4_ToF = True
                        
                        for key, val in removed_gems.items():
                            removed_gems[key] += removed_gems_[key]
                            
                        condition = False

                        if gem_score_ > 0:
                            cascade_score += gem_score_
                            cascade_gem_counter += gem_counter_
                            condition = True

                        while condition:
                            board_after_move = self.Check_after_move(board_after_move, None, matched_grid_)
                            ToF_, M4_, M5_, gem_counter_, gem_score_, matched_grid_, removed_gems_ = self.Check_grid(board = board_after_move)
                            
                            if M5_:
                                M5_ToF = True

                            if M4_:
                                M4_ToF = True

                            if gem_score_ > 0:
                                cascade_score += gem_score_
                                cascade_gem_counter += gem_counter_
                                for key, val in removed_gems.items():
                                    removed_gems[key] += removed_gems_[key]
                                
                            else:
                                condition = False

                        score = (gem_score + cascade_score) * (gem_counter + cascade_gem_counter) * (gem_counter + cascade_gem_counter)
                        #'''
                        
                        if M5_ToF:
                            M5.append([gem_counter, gem_score, matched_grid, board_copy, [row, col, row + 1, col], removed_gems])
                        elif M4_ToF:
                            M4.append([gem_counter, gem_score, matched_grid, board_copy, [row, col, row + 1, col], removed_gems])
                        elif M3_ToF:
                            M3.append([gem_counter, gem_score, matched_grid, board_copy, [row, col, row + 1, col], removed_gems])
                
                #Move Right
                if col < self.Size - 1:
                    if board[row][col] != board[row][col + 1]:
                        board_copy = []
                        
                        for ROW in board:
                            R_O_W = []
                            for cell in ROW:
                                R_O_W.append(cell)
                            board_copy.append(R_O_W)

                        FROM = board[row][col]
                        TO = board[row][col + 1]

                        board_copy[row][col] = TO
                        board_copy[row][col + 1] = FROM

                        M3_ToF, M4_ToF, M5_ToF, gem_counter, gem_score, matched_grid, removed_gems = self.Check_grid(board = board_copy)
                        
                        #'''
                        cascade_score = 0
                        cascade_gem_counter = 0
                        cascade_removed_gems = {'Re' : 0, 'Gr' : 0, 'Bl' : 0, 'Pu' : 0, 'Ye' : 0, 'Br' : 0, 'Sk' : 0}

                        board_after_move = self.Check_after_move(board, [row, col, row, col + 1], matched_grid)
                        ToF_, M4_, M5_, gem_counter_, gem_score_, matched_grid_, removed_gems_ = self.Check_grid(board = board_after_move)
                        
                        for key, val in removed_gems.items():
                            removed_gems[key] += removed_gems_[key]
                            
                        condition = False

                        if gem_score_ > 0:
                            cascade_score += gem_score_
                            cascade_gem_counter += gem_counter_
                            condition = True

                        while condition:
                            board_after_move = self.Check_after_move(board_after_move, None, matched_grid_)
                            ToF_, M4_, M5_, gem_counter_, gem_score_, matched_grid_, removed_gems_ = self.Check_grid(board = board_after_move)

                            if gem_score_ > 0:
                                cascade_score += gem_score_
                                cascade_gem_counter += gem_counter_
                                for key, val in removed_gems.items():
                                    removed_gems[key] += removed_gems_[key]
                                
                            else:
                                condition = False

                        score = (gem_score + cascade_score) * (gem_counter + cascade_gem_counter) * (gem_counter + cascade_gem_counter)
                        #'''
                        
                        if M5_ToF:
                            M5.append([gem_counter, gem_score, matched_grid, board_copy, [row, col, row, col + 1], removed_gems])
                        elif M4_ToF:
                            M4.append([gem_counter, gem_score, matched_grid, board_copy, [row, col, row, col + 1], removed_gems])
                        elif M3_ToF:
                            M3.append([gem_counter, gem_score, matched_grid, board_copy, [row, col, row, col + 1], removed_gems])

        return(M3, M4, M5)

    def Check_after_move(self, board, move, matched_grid):
        board_after_move = []
        rank_up_dict = {'C' : 'S', 'S' : 'G', 'G' : 'P', 'P' : 'b', 
                        'b' : 'g', 'g' : 'r', 'r' : 's'}

        for ROW in board:
            R_O_W = []
            for cell in ROW:
                R_O_W.append(cell)
            board_after_move.append(R_O_W)

        if move != None:
            board_after_move[move[0]][move[1]] = board[move[2]][move[3]]
            board_after_move[move[2]][move[3]] = board[move[0]][move[1]]

        for r, row in enumerate(matched_grid):
            for c, cell in enumerate(row):
                if cell != []:
                    board_after_move[r][c] = []

        for r in range(self.Size)[::-1]:
            for c in range(self.Size)[::-1]:
                if board_after_move[r][c] == []:
                    if r > 0:
                        if board_after_move[r - 1][c] != []:
                            board_after_move[r][c] = board_after_move[r - 1][c]
                            board_after_move[r - 1][c] = []
                        else:
                            if r > 1:
                                if board_after_move[r - 2][c] != []:
                                    board_after_move[r][c] = board_after_move[r - 2][c]
                                    board_after_move[r - 2][c] = []
                                else:
                                    if r > 2:
                                        if board_after_move[r - 3][c] != []:
                                            board_after_move[r][c] = board_after_move[r - 3][c]
                                            board_after_move[r - 3][c] = []

        counter = 0
        for r in range(8)[::-1]:
            for c in range(8)[::-1]:
                if board_after_move[r][c] == []:
                    board_after_move[r][c] = counter
                    counter += 1

        return(board_after_move)
    
class Game(object):
    def __init__(self, 
                 Type = 'N',
                 Deck = None,
                 tol = 6.0):
        
        self.game_screen = {"top": 57, "left": 35, "width": 710, "height": 415} #755
        self.x = self.game_screen["left"]
        self.y = self.game_screen["top"]
        self.w = self.game_screen["width"]
        self.h = self.game_screen["height"]
        x = self.game_screen["left"]
        y = self.game_screen["top"]
        w = self.game_screen["width"]
        h = self.game_screen["height"]
        
        self.Krystara = {"top": y + h - 18, "left": x + int(w / 2) - 28, "width": 56, "height": 16}
        self.Gold = {"top": y + h - 43, "left": x + int(w / 2) - 28, "width": 56, "height": 16}
        self.BoardP = {"top": y + 30, "left": x + 171, "width": 368, "height": 368}
        self.LeaveTH = {"top": y + h - 35, "left": x + 185, "width": 45, "height": 15}
        self.PlayTH = {"top": y + h - 40, "left": x + 455, "width": 100, "height": 25}
        self.Error = {"top": y + h - 160, "left": x + 330, "width": 50, "height": 20}
        self.MyTurn = {"top": y + 20, "left": x + 106, "width": 5, "height": 3}
        #MT [253 253 253]
        self.Pos_1_l = {"top": y + 27, "left": x + 51, "width": 15, "height": 3}
        #Leg [243 162 33]
        self.Pos_1_fr = {"top": y + 35, "left": x + 161, "width": 3, "height": 3}
        self.Pos_2_u = {"top": y + 125, "left": x + 51, "width": 15, "height": 3}
        #Ult [29 113 253]
        self.Pos_2_fr = {"top": y + 134, "left": x + 161, "width": 3, "height": 3}
        self.Pos_3_l = {"top": y + 225, "left": x + 51, "width": 15, "height": 3}
        #Leg [242 161  32]
        self.Pos_3_fr = {"top": y + 234, "left": x + 161, "width": 3, "height": 3}
        self.Pos_4_e = {"top": y + 322, "left": x + 51, "width": 15, "height": 3}
        #Epi [149  54 230]
        self.Pos_4_fr = {"top": y + 334, "left": x + 161, "width": 3, "height": 3}
        self.Pos_4_si = {"top": y + 322, "left": x + 51, "width": 15, "height": 3}

        self.np_Krystara = np.load('Krystara.npy')
        self.np_Gold     = np.load("Gold.npy")
        self.np_Board    = np.load("Board.npy")
        self.np_LeaveTH  = np.load("LeaveTH.npy")
        self.np_PlayTH   = np.load("PlayTH.npy")
        self.np_Error    = np.load("Error.npy")
        self.np_MyTurn   = np.load("MyTurn.npy")
        self.np_Pos_1_l  = np.load("Pos_1_l.npy")
        self.np_Pos_2_u  = np.load("Pos_2_u.npy")
        self.np_Pos_3_l  = np.load("Pos_3_l.npy")
        self.np_Pos_4_e  = np.load("Pos_4_e.npy")
        self.np_Pos_1_fr = np.load("Pos_1_fr.npy")
        self.np_Pos_2_fr = np.load("Pos_2_fr.npy")
        self.np_Pos_3_fr = np.load("Pos_3_fr.npy")
        self.np_Pos_4_fr = np.load("Pos_4_fr.npy")

        self.PlayTH_pos = [int(self.PlayTH['left'] + 
                               self.PlayTH['width'] / 2),
                           int(self.PlayTH['top'] + 
                               self.PlayTH['height'] / 2)]
        
        self.Type = Type
        self.Deck = Deck
        self.tol = tol
        self.Error = []
        
        #Actual Start
        B = Board(G = self)
        self.Board = B
        self.Board.Filled_grid = self.Board.Fill_empty_grid()
        
        broken = False
        for row in self.Board.Filled_grid:
            for cell in row:
                if cell == []:
                    broken = True
        if broken:
            time.sleep(5)
            self.Board.Filled_grid = self.Board.Fill_empty_grid()
        
        (self.Board.m3, self.Board.m4, self.Board.m5, 
         self.Board.gem_counter, self.Board.gem_score, 
         self.Board.matching_grid, self.Board.removed_gems) = self.Board.Check_grid(board = self.Board.Filled_grid)
        
        if self.Board.m3 or self.Board.m4 or self.Board.m5:
            self.Error.append("Board has matched gems but it shouldn't!")
    
    def Grab(self, param):
        with mss.mss() as sct:
            sct_img = sct.grab(param)
            image_array = np.array(Image.frombytes('RGB', (sct_img.width, sct_img.height), sct_img.rgb))
        return(sct_img, image_array)
    
    def Check_for(self, something, np_s, tol = 3):
        sct_img, image_array = self.Grab(something)

        yes_equal = 0
        no_different = 0
        for n, A in enumerate(np_s):
            for m, a in enumerate(A):
                if np.allclose(image_array[n][m], np_s[n][m], atol = tol):
                    yes_equal += 1
                else:
                    no_different += 1

        if yes_equal > no_different:
            return(True)
        else:
            return(False)
    
    def Solve_board(self):
        M3, M4, M5 = self.Board.Get_moves(board = self.Board.Filled_grid)
        
        for move in M3:
            print("M3")
            print(move[4])
            print(move[5])
            for ROW in move[3]:
                print(ROW)
        for move in M4:
            print("M4")
            print(move[4])
            print(move[5])
            for ROW in move[3]:
                print(ROW)
        for move in M5:
            print("M5")
            print(move[4])
            print(move[5])
            for ROW in move[3]:
                print(ROW)
        
        
    def Click(self, pos):
        pyautogui.click(pos)
        pyautogui.moveTo(740, 460)

    def Make_move(self, move):
        self.Click(self.Board.Grid_click_positions[move[0]][move[1]])
        time.sleep(1)
        self.Click(self.Board.Grid_click_positions[move[2]][move[3]])


################################################################################

class GoW(App):
    def build(self):
        

        

        MyGame = Game()

        M3, M4, M5 = MyGame.Board.Get_moves(board = MyGame.Board.Filled_grid)
        
        TEXT = ''

        for move in M3:
            TEXT += '{}\n'.format(move[4])
            
        for move in M4:
            TEXT += '{}\n'.format(move[4])

        for move in M5:
            TEXT += '{}\n'.format(move[4])

        #MyGame.Solve_board()
        #print(MyGame.Board.Filled_grid)
        #print(MyGame.Error)
        
        return Label(text=TEXT)

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '100')

Window.top = 500
Window.left = 50

GoW().run()