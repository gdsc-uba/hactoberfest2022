package com.company;

public class Main {

    public static void main(String[] args) {
//        Phone p1 = new Phone();  we cannot initialize object because phone is abstract class
        Samsung s1 = new Samsung();
        s1.call();
        s1.sleep();
        s1.talk();
    }
}
