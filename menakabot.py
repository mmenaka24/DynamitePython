class MenakaBot:
    def __init__(self):
        pass
    
    def make_move(self, gamestate):

        number_of_rounds = len(gamestate.rounds)

        # Every 25 rounds, play dynamite (this ensures no more than 100 dynamites are played)
        if number_of_rounds % 25 == 0:
            return 'D'
        
        else:

            # Count number of each type of move over last 22 rounds - assume opponent will play the least played and beat that
            r = 0
            p = 0
            s = 0
            w = 0
            d = 0
            
            if number_of_rounds < 22:
                rounds_to_count = gamestate.rounds
            else:
                rounds_to_count = gamestate.rounds[-22:]

            for round in rounds_to_count:
                if round.p1 == 'R':
                    r +=1
                elif round.p1 == 'P':
                    p +=1
                elif round.p1 == 'S':
                    s +=1
                elif round.p1 == 'W':
                    w +=1
                elif round.p1 == 'D':
                    d +=1
            
            moves = [r, p, s, w, d]
            move_index = moves.index(min(moves))

            if move_index == 0:
                # Assume opponent will play rock, beat with paper
                return 'P'
            elif move_index == 1:
                # Assume opponent will play paper, beat with scissors
                return 'S'
            elif move_index == 2:
                # Assume opponent will play scissors, beat with rock
                return 'R'
            elif move_index == 3:
                # Assume opponent will play water, beat with rock, paper or scissors (depending on round number)
                move_chooser = number_of_rounds % 3
                if move_chooser == 0:
                    return 'R'
                elif move_chooser == 1:
                    return 'P'
                elif move_chooser == 2:
                    return 'S'
            elif move_index == 4:
                # Assume opponent will play dynamite, beat with water
                return 'W'