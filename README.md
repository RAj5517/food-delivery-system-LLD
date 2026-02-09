# Food Delivery System – Low Level Design (LLD)

This repository is created to practice **Low Level Design (LLD)** using an
interview-style approach.

The goal is to understand how to:
- Gather requirements
- Narrow down scope
- Make assumptions consciously
- Think in terms of objects, responsibilities, and relationships

⚠️ **No implementation or final design is included at this stage.**
The focus is only on problem understanding and requirement analysis.

---

## 📌 Problem Statement

Design a simplified **online food delivery system** similar to platforms
like Swiggy or Zomato.

The system should allow a user to:
- Discover restaurants
- View food items
- Place orders
- Make payments
- Receive notifications once an order is placed

This is a **Low Level Design problem**, not a full production system.

---

## 🧩 Functional Requirements

The system should support the following **functional requirements**:

1. A user should be able to search restaurants based on location
2. A restaurant should have a menu consisting of multiple food items
3. A user should be able to add food items to a cart
4. A user should be able to place an order
5. Orders can be of different types:
   - Delivery order
   - Pickup order
6. A user should be able to make payment while placing an order
7. A user should be notified once the order is placed successfully

---

## ⚙️ Non-Functional Requirements

1. The system should be easy to extend (new order types, payment methods)
2. The design should follow object-oriented principles
3. The system should avoid tight coupling between components
4. The code should be readable and maintainable
5. The focus is on design clarity, not performance optimization

---

## 🧠 Assumptions

To keep the scope manageable and suitable for an LLD interview:

- Payment processing is handled by a **third-party service**
- Notification delivery (SMS / Email / Push) is handled externally
- No database or persistence layer is required
- Data can be stored in memory
- No authentication or authorization is required
- No delivery partner workflow is required
- Only the **user-side happy flow** is considered
- Error handling is minimal

---

## 🔍 Out of Scope

The following are intentionally **out of scope** for this design:

- REST APIs or HTTP layer
- Frontend / UI
- Database schema or ORM
- Microservices or distributed systems
- Concurrency or multithreading
- Real payment gateway integrations

---

## 📐 Design Approach (Planned)

The design will be created using the following steps:

1. Identify core entities
2. Define relationships (composition, aggregation, inheritance)
3. Create UML class diagrams
4. Validate design decisions
5. Implement the finalized design in code

---

## 🚧 Current Status

- [x] Problem statement defined
- [x] Requirements gathered
- [x] Assumptions finalized
- [ ] UML class diagram
- [ ] Design review
- [ ] Code implementation

---

## 📎 Note

This repository is meant for **learning, interviews, and discussion**.
The design will evolve step by step and trade-offs will be documented.
