class Stack {
  private int[] data;
  private int top;

  public Stack(int capacity) {
    data = new int[capacity];
    top = -1;
  }

  public void push(int value) {
    if (isFull()) {
      throw new StackOverflowError();
    }

    top++;
    data[top] = value;
  }

  public int pop() {
    if (isEmpty()) {
      throw new StackUnderflowError();
    }

    int value = data[top];
    top--;
    return value;
  }

  public boolean isEmpty() {
    return top == -1;
  }

  public boolean isFull() {
    return top == data.length - 1;
  }
}
