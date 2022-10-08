package com.company;

public abstract class Phone { // cannot create object from abstract class
    String age = "10"; //also we can have final methods and variables in subclass body

    public abstract void call();  // abstract method
    public abstract void sleep();
    public void talk(){
        System.out.println("Give a call");
        System.out.println(age);
    }

}
