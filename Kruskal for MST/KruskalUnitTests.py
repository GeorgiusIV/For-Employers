import unittest
import KruskalForMST as krsk

class method_testing(unittest.TestCase):
    
    def test_Kruskal(self):
        
        G = krsk.Graph(["a","b","c","d"])
        G += [("a","b",1),("b","c",1),("c","d",1),("a","d",10)]
        G_answer = [("a","b",1),("b","c",1),("c","d",1)]
        self.assertEqual(G.Kruskal().edges,G_answer)
        
        H = krsk.Graph(["a","b","c","d","e","f","g"])
        H += [("a","b",1),("b","c",10),("c","d",10),("d","e",1),("e","f",1),("f","c",1),("c","g",1),("g","a",10)]
        H_answer = [("a","b",1),("d","e",1),("e","f",1),("f","c",1),("c","g",1),("b","c",10)]
        self.assertEqual(H.Kruskal().edges,H_answer)
        
        I = krsk.Graph(["a","b","c","d"])
        I += [("a","b",1),("a","d",10),("b","d",1),("b","c",10),("c","d",1)]
        I_answer = [("a","b",1),("b","d",1),("c","d",1)]
        self.assertEqual(I.Kruskal().edges,I_answer)
        
if __name__ == "__main__":
    unittest.main()