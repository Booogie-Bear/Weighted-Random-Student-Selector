#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List

class Person():
    """A object oriented intepretation of a normal human being. Persons have the following properties:
    ...

    Attributes
    ----------
    first_name : string
        Person's first name
    last_name : string
        Person's last name
    name : string
        Person's full name

    Methods
    -------
    get_name()
        Returns person's name
    get_first_name()
        Returns person's first name
    get_last_name()
        Returns person's last name

    """
    def __init__(self, first_name:str, last_name:str):
        """
        Parameters
        ----------
        first_name : string
            Person's first name
        last_name : string
            Person's last name

        """
        self.first_name = first_name
        self.last_name = last_name
        self.name = f"{self.first_name} {self.last_name}"

    def get_name(self) -> str:
        "str: Returns name of the person as string"
        return self.name

    def get_first_name(self) -> str:
        "str: Returns first name of the person as string"
        return self.first_name

    def get_last_name(self) -> str:
        "str: Returns last name of the person as string"
        return self.last_name


class GStudent(Person):
    """A Galvanize student with a probability weight of how many times they have been "randomly" picked to answer questions. GStudents have the following properties:
    ...

    Attributes
    ----------
    first_name : string
        Person's first name
    last_name : string
        Person's last name
    pWeight : float
        The students probability weight in respect to classroom size
    name : string
        Person's full name

    Methods
    -------
    get_probability()
        Returns probability weight of student

    """
    def __init__(self, first_name:str, last_name:str, pWeight:float=None):
        """
        Parameters
        ----------
        pWeight : float
            The students initial probability weight, can be found by dividing 1 by current class size

        """
        super().__init__(first_name, last_name)
        self.pWeight = pWeight


class GClass:

    def __init__(self, program:str, cohortID:int, location:str="Seattle"):
        self.program = program
        self.cohortID = cohortID
        self.location = location
        self.classroom = []

    def __repr__(self):
        return f"GClass(\"{self.program}\", {self.cohortID}, \"{self.location}\")"

    def __str__(self):
        return f"Galvanize {self.location} {self.program} Cohort {self.cohortID}"

    def createClass(self, student_names:List[str]) -> None:
        pass
