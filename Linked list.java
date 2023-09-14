class Node {
  int data;
  Node next;

  public Node(int data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  Node head;

  public LinkedList() {
    head = null;
  }

  public void add(int data) {
    Node newNode = new Node(data);

    if (head == null) {
      head = newNode;
    } else {
      Node currentNode = head;
      while (currentNode.next != null) {
        currentNode = currentNode.next;
      }

      currentNode.next = newNode;
    }
  }

  public void print() {
    Node currentNode = head;

    while (currentNode != null) {
      System.out.println(currentNode.data);
      currentNode = currentNode.next;
    }
  }
}
