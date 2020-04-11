/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.patternproject;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 *
 * @author mav
 */
public class IteratorPatternTest {
    
    public IteratorPatternTest() {
    }
    
    @BeforeAll
    public static void setUpClass() {
    }
    
    @AfterAll
    public static void tearDownClass() {
    }
    
    @BeforeEach
    public void setUp() {
    }
    
    @AfterEach
    public void tearDown() {
    }

    @Test
    public void testGetStudent() {
        IteratorPattern.MakeList();
        Student stu = IteratorPattern.GetStudent(1234);
        String expected = "Mike";
        assertEquals(expected,stu.firstName);   

    }
    
    @Test
    public void testEachRemaining() {
        IteratorPattern.MakeList();
        assertEquals(true,IteratorPattern.HasIds());
        IteratorPattern.AddMoreStudents();
        assertEquals(false,IteratorPattern.HasIds());
        IteratorPattern.EachRemaining();
        assertEquals(true,IteratorPattern.HasIds());
    }
    
    @Test
    public void testRemoveStudent() {
        IteratorPattern.MakeList();
        IteratorPattern.RemoveStudent(1234);
        assertEquals("NONE",IteratorPattern.GetStudent(1234).firstName);
    }
}
