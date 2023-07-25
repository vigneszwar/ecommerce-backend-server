

class Node {
    int val;
    Node next;
    Node(int val)
    {
        this.val=val;
    }
}

class MergeTwoSortedList {
      Node head;

      public void insertAtBeginning( Node newnode) {
        if (head == null) {
            head = newnode;
        }
        else {
            newnode.next = head;
            head = newnode;
        }
    }

     public static Node mergeTwoLists(Node list1, Node list2) {
       
        if(list1== null)
            return list2;
        if(list2 == null)
            return list1;
        
        Node small, big;
    
        if(list1.val <= list2.val)
        {
            small = list1;
            big = list2;
        }
        else
        {
            small = list2;
            big = list1;
        }
        
        Node head = small;
        
        while(small != null && big != null)
        {
            Node temp = null;
            
            // while our small is smaller than the big we will keep on looping
            while(small != null && small.val <= big.val)
            {
                temp = small;   // to get the previous node of small 
                small = small.next; // so at the end of this loop small would be pointing to the node which is larger than big
            }
            
            temp.next = big;
            
            // as the conception of small and big has changed here, we will swap them
            
            Node swap = big;
            big = small;
            small = swap;
        }
        
        return head;

    }

    public static void main(String[] args) {
        Node list1 = new Node(5);
        list1.next = new Node(10);
        list1.next.next = new Node(15);
        list1.next.next.next = new Node(40);
 
        Node list2 = new Node(2);
        list2.next = new Node(3);
        list2.next.next = new Node(20);

        System.out.println(mergeTwoLists(list1 , list2));
    }
}
