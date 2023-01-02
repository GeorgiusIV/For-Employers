import unittest
import KruskalVerification as krsk

class method_testing(unittest.TestCase):
    
    def test_happypath_test_one(self):
        
        G = krsk.Graph(["a","b","c","d"])
        G += [("a","b",1),("b","c",1),("c","d",1),("a","d",10)]
        G_answer = [("a","b",1),("b","c",1),("c","d",1)]
        self.assertEqual(G.kruskal().edges,G_answer)

    def test_happypath_test_two(self):
        
        H = krsk.Graph(["a","b","c","d","e","f","g"])
        H += [("a","b",1),("b","c",10),("c","d",10),("d","e",1),("e","f",1),("f","c",1),("c","g",1),("g","a",10)]
        H_answer = [("a","b",1),("d","e",1),("e","f",1),("f","c",1),("c","g",1),("b","c",10)]
        self.assertEqual(H.kruskal().edges,H_answer)

    def test_happypath_test_three(self):
                
        I = krsk.Graph(["a","b","c","d"])
        I += [("a","b",1),("a","d",10),("b","d",1),("b","c",10),("c","d",1)]
        I_answer = [("a","b",1),("b","d",1),("c","d",1)]
        self.assertEqual(I.kruskal().edges,I_answer)


    def test_sadpath_test_one(self):
                
        # testing if a character can be entered instead of an integer

        G = krsk.Graph(["a","b","c"])
        G += [("a","b",10),("a","c","b")]
        G_answer = [("a","b",10)]
        self.assertEqual(G.edges,G_answer)

    def test_sadpath_test_two(self):

        # testing if a list can be entered as a string, instead of an integer
                
        G = krsk.Graph(["a","b","c"])
        G += [("a","b",10),("a","c","[a,b]")]
        G_answer = [("a","b",10)]
        self.assertEqual(G.edges,G_answer)

    def test_sadpath_test_three(self):
        
        # testing if a list can be entered instead of an integer

        G = krsk.Graph(["a","b","c"])
        G += [("a","b",10),("a","c",["a","b"])]
        G_answer = [("a","b",10)]
        self.assertEqual(G.edges,G_answer)



    def test_sadpath_test_four(self):
                
        # Testing if Hexadecimal is converted to an integer

        G = krsk.Graph(["a","b","c"])
        G += [("a","b",10),("a","c",0XFF)]
        G_answer = [("a","b",10),("a","c",255)]
        self.assertEqual(G.edges,G_answer)

    def test_sadpath_test_five(self):
                
        # Testing if Binary is converted to an integer

        G = krsk.Graph(["a","b","c","d"])
        G += [("a","b",10),("b","c",20),("a","c",0b111),("c","d",0b110)]
        G_answer = [("a","b",10),("b","c",20),("a","c",7),("c","d",6)]
        self.assertEqual(G.edges,G_answer)

    def test_sadpath_test_six(self):
                
        # Testing if Octal is converted to an integer

        G = krsk.Graph(["a","b","c"])
        G += [("a","b",10),("a","c",0o7)]
        G_answer = [("a","b",10),("a","c",7)]
        self.assertEqual(G.edges,G_answer)



    def test_sadpath_test_seven(self):
                
        # testing if verts can be repeated in a tuple

        G = krsk.Graph(["a","b","c"])
        G += [("a","b",10),("a","a",1)]
        G_answer = [("a","b",10)]
        self.assertEqual(G.edges,G_answer)



    def test_sadpath_test_eight(self):
                
        # testing if a tuple can be less than length three

        G = krsk.Graph(["a","b","c"])
        G += [("a","b",10),("a","c"),("a","c",20)]
        G_answer = [("a","b",10),("a","c",20)]
        self.assertEqual(G.edges, G_answer)


    def test_sadpath_test_nine(self):
                
        # testing if a tuple can be greater than length three

        G = krsk.Graph(["a","b","c"])
        G += [("a","b",10),("a","b",1,"c")]
        G_answer = [("a","b",10)]
        self.assertEqual(G.edges,G_answer)

    def test_sadpath_test_ten(self):

        # testing if the same edges can be added to the graph twice

        G = krsk.Graph(["a","b","c"])
        G += [("a","b",10),("a","b",1)]
        G_answer = [("a","b",10)]
        self.assertEqual(G.edges,G_answer)


    def test_sadpath_test_eleven(self):

        # testing if the same verts can be added to the graph twice

        G = krsk.Graph(["a","b","c"])
        G += ["a","b"]
        G += ["a","b"]
        G_answer = []
        self.assertEqual(G.edges,G_answer)


    def test_sadpath_test_eleven(self):

        # testing an edge can be added without the necessary vertex

        G = krsk.Graph(["a","c"])
        G += [("a","b")]
        G_answer = []
        self.assertEqual(G.edges,G_answer)



        
if __name__ == "__main__":
    unittest.main()