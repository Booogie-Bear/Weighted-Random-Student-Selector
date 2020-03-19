#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List

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
    def __contains__(self, val:str):
        return val in self.classroom
    def __iter__(self):
        return iter(self.classroom)
    def __len__(self):
        return len(self.classroom)


    def createClass(self, student_names:List[str]) -> None:
        pass
