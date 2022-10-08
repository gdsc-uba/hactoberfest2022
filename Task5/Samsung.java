package com.company;

public class Samsung extends Phone{
    final String name= "arun";  //also we can have final methods and variables in subclass body

    @Override
    public void call() {
        age = "10";
        System.out.println("Inside samsung call");
    }

    @Override
    public void sleep() {
        System.out.println("Inside samsung sleep");

    }

}
