CREATE TABLE users
(
    user_id     SERIAL          NOT NULL,
    username    VARCHAR(255)    NOT NULL,
    email       VARCHAR(255)    NOT NULL UNIQUE,
    hashed_password    VARCHAR(255)    NOT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    edited_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT  user_pk PRIMARY KEY(user_id)
);

-- Indexes
CREATE UNIQUE INDEX email_unique ON users(email);

