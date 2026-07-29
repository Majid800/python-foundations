CREATE TABLE users
(
    user_id SERIAL PRIMARY KEY,

    email_address VARCHAR(255) UNIQUE NOT NULL,

    first_name VARCHAR(50) NOT NULL,

    last_name VARCHAR(50) NOT NULL,

    username VARCHAR(50) UNIQUE NOT NULL,

    password VARCHAR(255) NOT NULL,

    role VARCHAR(30) NOT NULL,

    dispense BOOLEAN NOT NULL DEFAULT FALSE,

    check_prescriptions BOOLEAN NOT NULL DEFAULT FALSE,

    order_stock BOOLEAN NOT NULL DEFAULT FALSE,

    access_pmr BOOLEAN NOT NULL DEFAULT FALSE);


	INSERT INTO users
(
    email_address,
    first_name,
    last_name,
    username,
    password,
    role,
    dispense,
    check_prescriptions,
    order_stock,
    access_pmr
)
VALUES
(
    'john.smith@gmail.com',
    'John',
    'Smith',
    'johnsmith',
    'Password123!',
    'Pharmacist',
    TRUE,
    TRUE,
    TRUE,
    TRUE
);

INSERT INTO users
(
    email_address,
    first_name,
    last_name,
    username,
    password,
    role,
    dispense,
    check_prescriptions,
    order_stock,
    access_pmr
)
VALUES
(
    'amy.brown@gmail.com',
    'Amy',
    'Brown',
    'amybrown',
    'SecurePass1!',
    'Dispenser',
    TRUE,
    TRUE,
    FALSE,
    FALSE
);
