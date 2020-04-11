/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.patternproject;

/**
 *
 * @author mav
 */
public class Student {
    public String firstName;
    public String lastName;
    public int  birthYear;
    public int  id;
    
    public Student() {
        firstName = "NONE";
        lastName = "NONE";
        birthYear = -1;
        id = -1;
    }
    
    public Student(String fName, String lName, int bYear, int ident) {
        firstName = fName;
        lastName = lName;
        birthYear = bYear;
        id = ident;
    }
    
    public Student(String fName, String lName, int bYear) {
        firstName = fName;
        lastName = lName;
        birthYear = bYear;
        id = -1;
    }
}

