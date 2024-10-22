# Banking Service Application

## Overview

The Banking Service Application is designed to handle all primary information required to maintain customer accounts in a bank. The system provides functionality for both customers and admin staff to manage banking operations efficiently.

## Features

- **User Authentication**: All users must log in to access the system, displaying their names on the interface.
- **Super User Account**: A default Super User Account is available to create admin staff accounts.
- **Customer Registration**: Customers fill out a registration form, and staff enter their details into the system to generate unique account numbers and default passwords.
- **Account Types**: Customers can register for either Savings or Current accounts.
- **Login and Transactions**: Customers log in using their account number and password, with capabilities to modify their password and perform deposit and withdrawal transactions.
- **Admin Capabilities**: Admin staff can update customer details, excluding customer ID and name.
- **Minimum Balance Checks**: Withdrawal transactions are subject to minimum balance requirements (RM100 for Savings and RM500 for Current accounts).
- **User Interface**: The system features a unique menu-based user interface for all interactions.
- **Statement of Account**: Admin staff and customers can generate account statements for a specified date range, displaying totals for deposits and withdrawals.
- **Data Storage**: All details are saved in text files for persistent data management.
- **Input Validation**: The application includes validation for user entries to prevent logical errors.
