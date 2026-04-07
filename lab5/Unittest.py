import unittest
from lab5 import min_moves, directions_knight, directions_king, directions_rook, directions_queen, directions_bishop, direction_pawn

class TestMoves(unittest.TestCase):

    def test_min_knight_moves(self):
        self.assertEqual(min_moves((7, 0), (0, 7), directions_knight), 6)
    
    def test_min_king_moves(self):
        self.assertEqual(min_moves((7, 0), (0, 7), directions_king), 7)
    
    def test_min_rook_moves(self):
        self.assertEqual(min_moves((7, 0), (0, 7), directions_rook), 2)
    
    def test_min_queen_moves(self):
        self.assertEqual(min_moves((7, 0), (0, 7), directions_queen), 1)
    
    def test_min_bishop_moves(self):
        self.assertEqual(min_moves((7, 0), (0, 7), directions_bishop), 1)

    def test_min_pawn_moves(self):
        self.assertEqual(min_moves((0, 0), (7, 0), direction_pawn), 7)
    
    def test_impossible_pawn_move(self):
        self.assertEqual(min_moves((0, 0), (7, 7), direction_pawn), "Шляху немає")
    
    def test_impossible_bishop_move(self):
        self.assertEqual(min_moves((7, 0), (0, 6), directions_bishop), "Шляху немає")

if __name__ == '__main__':
    unittest.main()