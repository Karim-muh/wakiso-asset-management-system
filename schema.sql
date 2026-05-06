# USERS
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) UNIQUE,
    email VARCHAR(35),
    password VARCHAR(40),
    role ENUM('admin', 'employee') NOT NULL
);

# DEPARTMENTS
CREATE TABLE departments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    location VARCHAR(30)
);

# ASSETS
CREATE TABLE assets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    category VARCHAR(50),
    status ENUM('available','assigned','maintenance','disposed') DEFAULT 'available',
    location VARCHAR(20)
);

# REQUISITIONS (REQUESTS)
CREATE TABLE requisitions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    asset_id INT,
    status ENUM('pending','approved','rejected') DEFAULT 'pending',
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (asset_id) REFERENCES assets(id)
);

# ALLOCATIONS (ASSIGNMENT)
CREATE TABLE allocations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    asset_id INT,
    user_id INT,
    issue_date DATE,
    return_date DATE,
    FOREIGN KEY (asset_id) REFERENCES assets(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
