# 🌐 Network Source Monitoring And Access Management System

A multi-task Python and HTML-based project that simulates a real-world network infrastructure management system. The system is designed around object-oriented principles and classic design patterns to model network device monitoring, role-based access control, and an administrative web interface.

---

## 📌 Overview

The project is split across three tasks, each addressing a distinct layer of a network management system — a frontend dashboard, a device monitoring engine, and a user access control module. Together they demonstrate how software design patterns can be applied to build scalable, maintainable systems that mirror real enterprise network tooling.

---

## 🖥️ Task 01 — Admin Dashboard (index.html)

A static HTML and CSS frontend that simulates the visual layer of a network monitoring platform. It presents a login panel supporting two roles — Network Administrator and Network Operator — followed by a live-style dashboard.

The dashboard displays four key metrics at a glance: total servers, routers and switches, active alerts, and overall network uptime. A device table lists each node in the network with its type, IP address, operational status, and current CPU usage. Alert filters let the operator toggle visibility of CPU overload events, offline devices, and bandwidth violations, while a view mode selector narrows the display to all devices, servers only, or alerts only.

---

## 🔍 Task 02 — Network Device Monitoring (task2.py)

A Python module that models network infrastructure using three core design patterns.

An abstract base class defines the contract that all network devices must fulfill — every device exposes its name, IP, type, and operational status through a common interface. Three concrete device types are implemented on top of this: Server, Router, and Switch, each carrying its own relevant attributes such as CPU load for servers.

Device instantiation is handled through the **Factory Pattern** via a `DeviceFactory` class. Rather than constructing devices directly, the caller specifies a device type by name and receives the correct object — decoupling creation logic from business logic and making it straightforward to extend the system with new device types.

The **Singleton Pattern** governs two system-wide managers. `NetworkMonitor` maintains a centralized registry of all active devices and alerts, ensuring that no matter how many times it is referenced across the codebase, a single shared instance coordinates all monitoring state. `LogManager` follows the same pattern to enforce a single, authoritative audit log. Both singletons are verified at runtime to confirm their identity is preserved across multiple instantiations.

---

## 🔐 Task 03 — Access Management System (task3.py)

A Python module that implements role-based access control for network system users, again structured around abstract classes and design patterns.

An abstract `NetworkUser` class defines the interface that all user types must implement: a role identifier and a permission set. Three concrete roles extend this — `GuestUser` with no permissions, `OperatorUser` with read-level access to monitoring and logs, and `AdminUser` with full control including device management and access control administration.

User creation is handled by a `UserFactory`, keeping the instantiation logic centralized and extensible. The **Factory Pattern** here mirrors Task 2 — callers request a user by role name and receive a fully initialized object without depending on concrete classes.

Session lifecycle is managed by a `SessionManager` implemented as a **Singleton**. It handles login, logout, and access checks in a single shared session store. When a user attempts an action, the manager cross-references their active session against their permission list and returns a clear permit or deny decision. Singleton integrity is confirmed at the end of execution by comparing two independently obtained references.

---

## 🧩 Design Patterns Applied

🔷 **Abstract Base Classes** enforce a consistent interface across all device and user types, making the system open for extension while protecting the integrity of the core contract.

🏭 **Factory Pattern** centralizes object creation for both devices and users, eliminating scattered constructors and making it trivial to add new types without modifying existing logic.

☝️ **Singleton Pattern** ensures global system state — monitoring data, logs, and sessions — is managed through a single authoritative instance, preventing duplication and maintaining consistency across the application.

---

## 🛠️ Technologies Used

- 🐍 Python 3 with the `abc` module for abstract class enforcement
- 🌐 HTML5 and CSS3 for the frontend dashboard
- 🧱 Object-Oriented Programming: abstraction, inheritance, and polymorphism
- 🎨 Software Design Patterns: Factory, Singleton, and Abstract Base Class

---

## 👨‍💻 Author

**Muhammad Abdullah**
BSE student
[GitHub](https://github.com/muhammad-abdullaahh) • [LinkedIn](https://www.linkedin.com/in/muhammad-abdullaahh)
