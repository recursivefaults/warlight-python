import unittest
import node
import edge

class NodeTest(unittest.TestCase):
    def setUp(self):
        self.n = node.Node()

    def test_can_execute(self):
        r = self.n.execute(self.fakey_func, None)
        self.assertEquals(r, True)

    def test_can_execute_no_func(self):
        r = self.n.execute(None, None)
        self.assertEquals(r, None)
        
    def test_node_has_edges(self):
        edges = self.n.edges
        self.assertIsInstance(edges, list)
        
    def test_can_select_next_node(self):
        n1 = node.Node()
        n2 = node.Node()
        self.n.edges.append(edge.Edge(0.1, n1))
        self.n.edges.append(edge.Edge(0.9, n2))
        self.n.set_seed(0)
        r = self.n.select_next()
        self.assertIsInstance(r, node.Node)
        self.assertEquals(r, n2)
        
    def test_can_not_select_next_node(self):
        r = self.n.select_next()
        self.assertEquals(r, None)


    def fakey_func(self):
        return True


        
if __name__ == '__main__':
    unittest.main()
        

