/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.patternproject;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.ListIterator;


public class IteratorPattern {
    
    static ArrayList <Student> students = new ArrayList<>();
    public static void MakeList() {
        students.clear();
        Student mike = new Student("Mike","Digan",1995,1234);
        students.add(mike);
        Student mark = new Student("Mark","Hamill",1951,2345);
        students.add(mark);
        Student walter = new Student("Walter","White",1958,3456);
        students.add(walter);
        Student carl = new Student("Carl","Sagan",1934,4567);
        students.add(carl);
        Student paul = new Student("Paul","McCartney",1942,5678);
        students.add(paul);
        Student joe = new Student("Joe","Dirt",1964,6789);
        students.add(joe);
    }
    
    public static void AddMoreStudents() {
        Student margo = new Student("Margo","Hayes",1998);
        students.add(margo);
        Student brian = new Student("Brian","Greene",1963);
        students.add(brian);
        Student roger = new Student("Roger","Waters",1943);
        students.add(roger);
    }
    
    public static void TraverseArray() {
        Iterator<Student> classes = students.iterator();
        Student tempStu = new Student();
        while(classes.hasNext()) {
            tempStu = classes.next();
            System.out.println(tempStu.lastName + ", " + tempStu.firstName + " ID no. " 
                    + tempStu.id + " born in " + tempStu.birthYear);
        }
    }
    
    public static void ReverseTraverse() {
        ListIterator<Student> classes = students.listIterator();
        Student tempStu = new Student();
        while(classes.hasNext()) {
            classes.next();
        }

        while(classes.hasPrevious()) {
            tempStu = classes.previous();
            System.out.println(tempStu.lastName + ", " + tempStu.firstName + " ID no. " 
                    + tempStu.id + " born in " + tempStu.birthYear);
        }
    }    
    
    public static void EachRemaining() {
        ListIterator<Student> classes = students.listIterator();
        Student tempStu = new Student();
        while(classes.hasNext()) {
            tempStu = classes.next();
            if(tempStu.id == -1) {
                classes.previous();
                classes.forEachRemaining(person -> person.id = (int) (Math.random() * (9999-1000) + 1000));
            }
        }
    }
    
    public static boolean HasIds() {
        Iterator<Student> classes = students.iterator();
        Student tempStu = new Student();
        while(classes.hasNext()) {
            tempStu = classes.next();
            if(tempStu.id == -1) return false;
        }
        return true;
    }
    
    public static Student GetStudent(int id) {
        Student tempStu = new Student();
        Iterator<Student> stu = students.iterator();
        while(stu.hasNext()) {
            tempStu = stu.next();
            if(tempStu.id == id) break;
        }
        return tempStu;
    }
    
    public static void main(String [] args) {
        MakeList();
        TraverseArray();
        for(int i = 0; i < 50; i++) System.out.print('-');
        System.out.println("\n \n");
        ReverseTraverse();
    }
}