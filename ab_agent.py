# -*- coding: utf-8 -*-
import random
import time
import copy
import action
import operator
import math
from action import Action

INF = 2147483647
_CardNumPerType_ = 13
_Ordery_ = [10, 11,  9, 4,  3, 12, 1,  13,  5,  8,  6,  7,  2]
_UpperBd_ = 100
_HotThresh_ = 10
_Step_ = 2

class Agent:
   def __init__(self, index = 0):
      self.index = index
   
   def genmove(self, state):
      pass

class PlayerState:
   def __init__(self, history, leg, card, cardNum1, cardNum2, cardNum3, cardNum4, mountNum, point, order, the_specific_small_h):
      self.myCard = MyCard(leg, card)# var card non exist
      cardNum = list()
      cardNum.append(cardNum1)
      cardNum.append(cardNum2)
      cardNum.append(cardNum3)
      cardNum.append(cardNum4)
      self.board = Board(history, mountNum, point, order, cardNum)
      #self.power = [50, 80, 90, 40, 10, 120, 100, 130, 0, 45, 10, 60, 85] #.263
      #self.power = [50, 80, 90, 40, 10, 120, 150, 130, 0, 45, 10, 60, 70] #.255
      self.power = [50, 80, 90, 40, 10, 130, 200, 140, 0, 45, 150, 160, 170] #.272 
      #self.power = [50, 80, 90, 40, 10, 130, 200, 140, 210, 45, 150, 160, 170] #.245
      #self.power = [50, 80, 90, 40, 10, 130, 200, 140, 0, 145, 150, 160, 170] #.258
      #self.power = [50, 80, 90, 40, 10, 130, 200, 140, 70, 145, 150, 160, 170] #.279 V
      #self.power = [50, 80, 90, 40, 10, 130, 200, 140, 270, 145, 150, 160, 170] #.241
      #self.power = [40, 50, 60, 30, 10, 130, 200, 140, 70, 145, 150, 160, 170] #.249
      #self.power = [40, 50, 60, 70, 80, 110, 200, 120, 130, 140, 150, 160, 170] #.232
      #self.power = [40, 50, 60, 70, 80, 100, 110, 120, 70, 140, 150, 160, 170] #.268
      #self.power = [40, 50, 60, 70, 80, 100, 130, 120, 90, 140, 150, 160, 170] #.267
      self.counter = 0
      #             1,  2,  3,   4,  5,  6,   7,  8,   9, 10,  j,  q,   k
      if the_specific_small_h is None:
         self.smallh = None
      else:   
         self.smallh = the_specific_small_h

   def __str__(self):
      return str(self.myCard.moves)

   def checkLose(self):
      return len(self.myCard.moves) == 0

   # TODO
   def simulateMove(self, action):
      move = 0
      for c in action.cards_used:
         self.myCard.cards.remove(c)
         move = move + getCardValue(c)
      if len(action.cards_used) == 1 and action.cards_used[0] == 1:
         self.board.nowPoint = 0
      elif move == 13:
         self.board.nowPoint = 99
      elif move == 1 or move == 2 or move == 3 or move == 6 or move == 8:
         self.board.nowPoint += move  
      elif move == 10 or move == 12:
         if action.victim == -1:
            self.board.nowPoint += move
         elif action.victim == -2:
            self.board.nowPoint -= move
      elif move == 4:
         self.order *= -1
      self.myCard.moves.remove(action)

   def Eval(self, userid):
      score = 0
      for card in self.myCard.cards:
         score = score + self.power[getCardValue(card)]
      for cnum in self.board.cardNum:
         score = score - cnum*60
      score = score + 2*self.board.cardNum[userid]
      return score

   def myTestEval(self, userid):
      power_here = list()
      temp_ordery = list()
      for card in range(_CardNumPerType_):
         power_here.append(random.randint(0,1024))

      # TODO: reconstruct power due to the ordery in _Ordery_
      for card in range(len(power_here)):
         power_here.sort()
         temp_ordery.append(_Ordery_[card])

      self.power = [0]
      which_one = 1
      for run in range(_CardNumPerType_):
         for ind in range(_CardNumPerType_):
            if temp_ordery[ind] == which_one:
               self.power.append(power_here[len(power_here) - 1])
               which_one += 1 
               break     
      #                 1, 2,  3, 4,  5,   6, 7,   8,  9,  10,  j,  q,  k
      #    ordery:      10, 11,  9, 4,  3, 12, 1,  13,  5,  8,  6,  7,  2
      score = 0
      nine = 0
      for card in self.myCard.cards:
         if getCardValue(card) == 9:      # todo: specialcase9
            nine += 1
         score = score + self.power[getCardValue(card)-1]

      if nine >= 1: 
         pass
      else: # no nine, compare cardnumber
         diff = 0
         for cnum in self.board.cardNum:
            diff += cnum-self.board.cardNum[userid] # other's card is more than mycard
         score = score - 60*diff
         #score = score + 60*abs(3 - self.board.cardNum[userid])
      return score

   def expEval(self, userid):
      seven = _UpperBd_*math.atan(self.counter - _HotThresh_)
      self.power = [0, _UpperBd_/5, _UpperBd_/5, _UpperBd_/4, _UpperBd_ *3/4, _UpperBd_*4/5, -_UpperBd_/2, seven, -_UpperBd_, _UpperBd_, _UpperBd_/2, _UpperBd_ *2/3, _UpperBd_/2, _UpperBd_]
      #                 1,                   2,       3,           4,                5,             6,          7,      8,         9,         10,               j,         q,          k
      score = 0
      nine = 0
      for card in self.myCard.cards:
         if getCardValue(card) == 9:      # todo: specialcase9
            nine += 1
         score = score + self.power[getCardValue(card)-1]

      if nine >= 1: 
         pass
      else: # no nine, compare cardnumber
         diff = 0
         for cnum in self.board.cardNum:
            diff += cnum-self.board.cardNum[userid] # other's card is more than mycard
         score = score - 60*diff
         #score = score + 60*abs(3 - self.board.cardNum[userid])
      self.counter += _Step_
      return score

class MyCard:
   def __init__(self, moves, cards):
      self.moves = moves
      self.cards = cards

class Board:
   def __init__(self, r, rn, p, o, c):
      self.record = r
      self.restNum = rn
      self.nowPoint = p
      self.order = o
      self.cardNum = c

cardType = ['♠ ', '♥ ', '♦ ', '♣ ']
def getCardString(cardIndex):
    cardvalue = 13 if (cardIndex % 13 == 0) else cardIndex % 13
    return str(cardvalue) + cardType[(cardIndex-1)/13]
def getCardValue(cardIndex):
   cardvalue = 13 if (cardIndex % 13 == 0) else cardIndex % 13
   return cardvalue
def getMoveString(move):
   return str(move)

class RandomAgent(Agent):
   def __init__(self, i = 0):
      self.i = i
      #print "Constructing Random Agent, player id = ", self.i

   def genmove(self, state):
      return randomGenmove(state)

class ExpAgent(Agent):
   def __init__(self, i = 0): # only need to know id
      self.i = i
      #print "Constructing Alpha-Beta Agent, player id = ", self.i

   def genmove(self, state):
      return self.abGenmove(state)

   def abGenmove(self, state, depth = 3, maxTime = 10):
      startTime = time.time()
      self.endTime = startTime + maxTime
      self.depth = depth
      score = self.search(state, -INF, INF, depth)
      #print "use " + str(time.time()-startTime) + "time"
      return self.bestmove #todo:

   def search(self, s, alpha, beta, depth): # fail soft negascout
      # todo: simulate move, 
      if s.checkLose():
         return -INF
      if depth == 0 or self.timeUp(): # or some heuristic
         return s.expEval(self.i) if depth%2 == 0 else -s.expEval(self.i) #todo:check
      m = -INF # current lower bound, fail soft
      n = beta # current upper bound
      for a in s.myCard.moves:
         news = copy.deepcopy(s)
         #news.simulateMove(a)
         
         tmp = -self.search(news, -n, -max(alpha, m), depth-1)
         if tmp > m: #todo:check
            if depth == self.depth:
               self.bestmove = a               
            if n == beta or depth < 3 or tmp >= beta:
               m = tmp
            else:
               m = -self.search(news, -beta, -tmp, depth-1) #research
         if m >= beta: # cut off
            return m 
         n = max(alpha, m) + 1 # set up null window
      return m

   def timeUp(self):
      nowTime = time.time()
      if nowTime > self.endTime:
         return True
      else:
         return False

class ScoutTestAgent(Agent):
   def __init__(self, i = 0): # only need to know id
      self.i = i
      #print "Constructing Test-Alpha-Beta Agent, player id = ", self.i

   def genmove(self, state):
      return self.abGenmove(state)

   def abGenmove(self, state, depth = 1, maxTime = 10):
      startTime = time.time()
      self.endTime = startTime + maxTime
      self.depth = depth
      score = self.search(state, -INF, INF, depth)
      #print "use " + str(time.time()-startTime) + "time"
      return self.bestmove #todo:

   def search(self, s, alpha, beta, depth): # fail soft negascout
      # todo: simulate move, 
      if s.checkLose():
         return -INF
      if depth == 0 or self.timeUp(): # or some heuristic
         return s.myTestEval(self.i) if depth%2 == 0 else -s.myTestEval(self.i) #todo:check
      m = -INF # current lower bound, fail soft
      n = beta # current upper bound
      for a in s.myCard.moves:
         news = copy.deepcopy(s)
         #news.simulateMove(a)
         
         tmp = -self.search(news, -n, -max(alpha, m), depth-1)
         if tmp > m: #todo:check
            if depth == self.depth:
               self.bestmove = a               
            if n == beta or depth < 3 or tmp >= beta:
               m = tmp
            else:
               m = -self.search(news, -beta, -tmp, depth-1) #research
         if m >= beta: # cut off
            return m 
         n = max(alpha, m) + 1 # set up null window
      return m

   def timeUp(self):
      nowTime = time.time()
      if nowTime > self.endTime:
         return True
      else:
         return False
      

         
class HumanAgent(Agent):
   """
   The human agent, action decided by human.
   """
   def __init__(self, i = 0):
      self.i = i
      print "Constructing Human Agent, id = ", self.i

   def genmove(self, state):
      return self.humanGenmove(state)

   def humanGenmove(self, state):
      s = ""
      for card in state.myCard.cards:
         s = s + getCardString(card) + ", "
      moves = list()
      for m in state.myCard.moves:
         moves.append(getMoveString(m) + ",\n")
      print "The card you have: ", s
      print "other people's cardNum = %d, %d, %d" % (state.board.cardNum[1], state.board.cardNum[2], state.board.cardNum[3])
      print "The legal move you can take: "
      for i in range(0, len(moves)):
         print "move index:", i, moves[i], 
      print "The point now is: ", state.board.nowPoint
      move = raw_input("pick the move by input the move index: ")   
      while ((move.isdigit() == False) or (int(move) < 0) or (int(move) >= len(state.myCard.moves))):
         move = raw_input("The move index value is illegal, try again: ")                   
      print "The move you take is: ", state.myCard.moves[int(move)]
      return state.myCard.moves[int(move)]

   def pygameGenmove(self, idx, cards_used):
      return Action(idx, cards_used)
   

class MonteAgent(Agent):
   """
   The Montecaro agent
   """
   def __init__(self, i = 0):
      self.i = i
      #print "Constructing Montecaro Agent, id = ", self.i

   def genmove(self, state):
      # In any circumstance, when unknown_cards < 17, use monte carlo algorithm
      if state.board.cardNum[1] + state.board.cardNum[2] + state.board.cardNum[3] + state.board.restNum > 17:
          return randomGenmove(state)
      else:
          return self.monteGenmove(state)

   # Monte_Carlo_Part
   
   def monteGenmove(self, state):
      # Find the unknown cards
      win_rate = {}
      fullCard = self.fullCard()
      temp = self.usedCard(state)
      usedCard = []
      for i in temp:
         for j in i:
            usedCard.append(j)
      usedCard.extend(state.myCard.cards)
      cards_unknown = [i for i in fullCard if i not in usedCard]

      for candidate in state.myCard.moves:
         for i in range(0, 1067):
            
            # Replicate situation

            win_point = 0
            cards_1 = state.myCard.cards

            # Shuffle and deal cards
            random.shuffle(cards_unknown)
            dummy = 0
            cards_2 = cards_unknown[dummy : state.board.cardNum[1]]
            dummy += state.board.cardNum[1]
            cards_3 = cards_unknown[dummy : dummy + state.board.cardNum[2]]
            dummy += state.board.cardNum[2]
            cards_4 = cards_unknown[dummy : dummy + state.board.cardNum[3]]
            dummy += state.board.cardNum[3]
            mountain = cards_unknown[dummy:]

            '''
            # Play under certain condition
            # Build a simulation judge (mc_judge) and write in the card distribution above
            mc_judge = Judge()
            mc_judge.card = []
            for i in [cards_1, cards_2, cards_3, cards_4]:
               hand = []
               for j in i:
                  hand.append(j)
               mc_judge.card.append(hand) 
            #做出已經出完candidate牌的樣子?
            a.cards_used = candidate
            mc_judge.doAction(a)      

            # (Player1在模擬局中，出candidate，之後讓mc_judge自己跑ab_agent跑完全程，回傳輸贏）???
            mc_judge.GameStart()   # PS: mc_indicator要是全局變量，不然會無限mc下去???
            if mc_judge.winner == 0: # winner要改全局變量???
               win_point += 1
            '''
         # find the win rate of a certain candidate, append it
         win_rate.update({candidate : win_point / 1067})
      print "win_rate", win_rate
      decided_card = max(win_rate.iteritems(), key=operator.itemgetter(1))[0]
      print "decided_card=================================", decided_card
      return decided_card

   def fullCard(self):
      fullCard = []
      for i in range(1,53):
         fullCard.append(i)
      return fullCard

   def usedCard(self, state):
      usedCard = []
      for i in state.board.record:
         usedCard.append(i.cards_used)
      return usedCard


class HeuristicAgent(Agent):
   """
   Only use heuristics.
   """
   def __init__(self, i = 0):
      self.i = i
      #print "Constructing Heuristic Agent, id = ", self.i

   # Totally by heuristic...
   def genmove(self, state):
      move = state.myCard.moves[0]     
      if len(state.myCard.cards) == 1 or len(state.myCard.moves) == 1:
         return move
      if len(state.myCard.cards) == 2:
         for a in range(0, len(state.myCard.moves)):
            m = 0
            for c in state.myCard.moves[a].cards_used:
               m = m + getCardValue(c)
            if len(state.myCard.moves[a].cards_used) == 2:
               if m != 9:
                  continue
               else:
                  movelist = [state.myCard.moves[a]]
                  while a < len(state.myCard.moves)-1:
                     a += 1
                     n = 0
                     for j in state.myCard.moves[a].cards_used:
                        n = n + getCardValue(j)
                     if n != 9:                       
                        return state.myCard.moves[a-1]
                     else:
                        movelist.append(state.myCard.moves[a])
                  return self.chooseMaxCard(state, movelist)
                  #return random.choice(movelist)
      movelist = list()
      if len(state.myCard.cards) == 3:
         for a in state.myCard.moves:
            m = 0
            for c in a.cards_used:
               m = m + getCardValue(c)
            handCards = len(state.myCard.cards) - len(a.cards_used) + 1
            if handCards < 3 and m == 9:
               movelist.append(a)
         move = self.pickBest(state)
      movelist2 = list()
      if len(state.myCard.cards) > 3:         
         for a in state.myCard.moves:
            m = 0
            for c in a.cards_used:
               m = m + getCardValue(c)
            handCards = len(state.myCard.cards) - len(a.cards_used) + 1
            if handCards < 4 and m == 9:
               movelist.append(a)
            if handCards == 4 and m != 9: # try to reduce cards to 4
               movelist2.append(a)
         move = self.pickBest(state)
      print "+++++++++++++++++++++++", move
      if len(movelist) > 0:
          return self.chooseMaxCard(state, movelist)
      if len(movelist2) > 0:
          return random.choice(movelist2)
      move = self.pickBest(state)
      return move

   def pickBest(self, state):
   # choose 1-card action only, by the card-power in class PlayerState
      p = 0
      best = list()
      for a in state.myCard.moves:
         best.append(a)         
         if len(a.cards_used) > 1:
            continue
         m = 0
         for c in a.cards_used:
            m = m + getCardValue(c)
         power = state.power[m-1]
         if power > p:
            best[:] = []
            p = power
            best.append(a)
         if power == p:
            best.append(a)
      return random.choice(best)

   def chooseMaxCard(self, state, movelist):
      """ return the most-hand-card victim move"""
      cardList = list(state.board.cardNum)
      cardNumList = list(state.board.cardNum)
      cardNumList.sort()      
      cardNumList.reverse()
      victim = list()
      for c in range(0, len(cardNumList)):
         victim.append(cardList.index(cardNumList[c]))
         cardList.remove(cardNumList[c])
      move = list()
      for i in range(0, len(victim)):
         if move == []:
            for m in movelist:
               if ((m.victim-1) == victim[i]):
                  move.append(m)
            if len(move) > 0:
               break
      if len(move) == 0:
         move = movelist
      return random.choice(move)

def randomGenmove(state):
   a = len(state.myCard.moves)
   if a == 0:
      return []
   else:
      i = random.randint(0, len(state.myCard.moves)-1)
      #print state.myCard.moves[i]
      return state.myCard.moves[i]


if __name__ == "__main__":
   from action import Action
   cards1 = [4, 5, 13, 16, 24]
   cards2 = [2, 7, 9, 18, 27]
   idx = 1
   act = [Action(idx+2, [8], 1)]
   act.append(Action(idx+2, [4], 0))
   act.append(Action(idx+2, [4, 8], 0))
   ai = ScoutAgent(idx)
   human = HumanAgent(idx+1)
   heu = HeuristicAgent(idx+2)
   record = "1 ChangeCard 9 2"
   state = PlayerState(record, [1, 3, 4, 12], [1,3, 16,24], 3, 4, 0, 2, 33, 99, 1)
   # record, legal, mycard
   state2 = PlayerState(record, act,[4, 8], 3, 4, 0, 2, 33, 99, 1)
   b = human.genmove(state)
   c = heu.genmove(state2)
   #print c
   #print "Simple agent's action " + ai.genmove(state)
   #print "Human player's action ", human.genmove(state2)
