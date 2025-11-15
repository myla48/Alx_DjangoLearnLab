# LibraryProject

A Django project for the **Advanced Features and Security** module.  
This project demonstrates how to extend Django with a custom user model, role-based permissions, and secure features for managing a library system.

---

## 🚀 Features
- **Custom User Model** (`bookshelf.CustomUser`)
  - Extends `AbstractUser`
  - Adds `date_of_birth` and `profile_photo` fields
- **Role-Based Access Control**
  - Groups: Admins, Editors, Viewers
  - Custom permissions on `Book` model: `can_create`, `can_delete`
- **Book Management**
  - Create, view, and delete books with permission checks
- **Favorites & Recommendations** *(future tasks)*
  - Users can favorite books and get personalized recommendations

---

## 📂 Project Structure
