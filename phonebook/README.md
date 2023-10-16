# Phonebook Application

The Phonebook Application is a Python program designed to help you manage your contacts and phone numbers efficiently. It serves as a digital directory, allowing you to store and retrieve contact information quickly and easily. Whether you're managing personal or business contacts, this tool simplifies the process of organizing and accessing your phonebook.

## Features
- **Contact Management**: Add, edit, and delete contacts with ease.
- **Search and Retrieval**: Quickly find and retrieve contact details using various search criteria.
- **Categorization**: Optional - Organize your contacts into categories (e.g., friends, family, work) for better organization.
- **Export and Import**: Backup and transfer your phonebook by exporting it to a file and importing it when needed.

## How to Use the Phonebook
Follow these steps to use the Phonebook Application:

1. **Run the Script**:
Execute the script by running the following command:
```python main.py```

2. **Main Menu**:
The program will present a main menu with options to manage your phonebook.
```sh
**********************
*   PHONEBOOK MENU   *
**********************
1. View All Contacts
2. Search Contacts
3. Add Contact
4. Edit Contact
5. Delete Contact
6. Export Phonebook
7. Import Phonebook
8. Exit
```
Customize it to suit your program requirement.

3. **Add a Contact**: `add_contact`
Choose the option to add a contact, and provide the contact's name, phone number, and category.
```sh
Enter contact name: John Doe
Enter phone number: +1 (123) 456-7890
Enter category: Friends
```

4. **Search Contacts**: `find_contact`
Use the search option to find contacts by name, phone number, or category.

5. **View all contacts**: `list_contacts`
You can list all contacts. You can add pagination or scrolling effect but this might require you to use a frontend framework. 

6. **Edit or Delete Contacts**: `update_contact` or `delete_contact` 
You can edit or delete contacts from your phonebook using the provided options.

7. **Export and Import**:
Backup your phonebook by exporting it to a file. Import your phonebook from a previously saved file when needed.

## Categories
The Phonebook Application allows you to categorize your contacts for better organization. You can create custom categories such as:

- Friends
- Family
- Colleagues
- Business
- Personal
- Emergency
- Customize your categories based on your specific contact management needs.

**Note**:
If a contact name already exists but the phone number is different or similar, it should prompt the user to confirm whether they want to update the existing contact.

**Bonus**:
You know how a typical phonebook works, as the user types a phone number, the application should display contact name suggestions based on the entered digits to streamline the process of associating a phone number with an existing contact.