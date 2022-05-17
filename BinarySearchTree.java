class Node{
    int data;
    Node left;
    Node right;
    public Node(int data){
        this.data = data;
        left = null;
        right = null;
    }
}

public class Main
{
    public static Node root;
    public Main(){
        this.root = null;
    }
    public void insert(int id){
    Node newNode = new Node(id);
    if(root==null){
        root = newNode;
        return;
    }
    Node current = root;
    Node parent = null;
    while(true){
        parent = current;
        if(id<current.data){
            current = current.left;
            if(current==null){
                parent.left = newNode;
                return;
            }
        }
        else{
            current = current.right;
            if(current==null){
                parent.right = newNode;
                return;
                }
            }
        }
    }
    public void display(Node root){
        if(root!=null){
            display(root.left);
            System.out.print(" "+root.data);
            display(root.right);
        }
    }
    public boolean find(int id){
        Node current = root;
        while(current!=null){
            if(current.data==id){
                return true;
            }
            else if(current.data>id){
                current = current.left;
            }
            else{
                current = current.right;
            }
        }
        return false;
    }
    public boolean delete(int id){
        Node parent = root;
        Node current = root;
        boolean isLeftChild = false;
        while(current.data!=id){
            parent = current;
            if(current.data>id){
                isLeftChild = true;
                current = current.left;
            }
            else{
                isLeftChild = false;
                current = current.right;
            }
            if(current==null){
                return false;
            }
        }
        //if i am here that means we have found the Node
        //Case 1: if node to be deleted has no childred
        
    }
	public static void main(String[] args) {
		Main b = new Main();
		b.insert(1);
		b.insert(2);
		b.insert(3);
		b.insert(4);
		b.insert(6);
		b.insert(8);
		b.insert(9);
		b.insert(10);
		b.insert(15);
		b.insert(16);
		b.insert(20);
		b.insert(25);
		System.out.println("original Tree: ");
		b.display(b.root);
		System.out.println("\nCheck whether Node with value 4 exists: "+b.find(4));
		
	}
}
