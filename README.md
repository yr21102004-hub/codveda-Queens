# ♛ N-Queens Problem (Backtracking Algorithm)

## 📌 Project Overview
This project provides a solution to the **N-Queens Problem** using **Python**, **Object-Oriented Programming (OOP)**, and the **Backtracking algorithm**.

The goal of the problem is to place **N queens on an N×N chessboard** such that no two queens threaten each other.  
A queen can attack another queen if they share the same **row**, **column**, or **diagonal**.

This project is implemented as part of my **Python Development Internship at Codveda Technologies**.

## 🎯 Problem Statement
Given an integer **N**, place **N queens** on an **N×N chessboard** so that:
- No two queens are in the same row  
- No two queens are in the same column  
- No two queens are in the same diagonal  

The program should generate **all possible valid solutions**.

## 🧠 Solution Approach
The solution uses the **Backtracking algorithm**, which works as follows:
1. Place a queen in a safe position in the current row.
2. Move to the next row and repeat the process.
3. If no valid position is found, backtrack to the previous row and try a different position.
4. Continue until all possible solutions are explored.

The implementation follows an **OOP-based design**, where all logic and data are encapsulated within a dedicated class.

## 🛠 Technologies Used
- Python
- Object-Oriented Programming (OOP)
- Backtracking Algorithm
- Recursion

## 📂 Project Structure
