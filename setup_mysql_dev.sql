-- Write a script that prepares a MySQL server for the Mini-fpl project:

-- A database mini_fpl_db
-- A new user mini_fpl_user (in localhost)
-- The password of mini_fpl_user should be set to mini_fpl_pwd
-- mini_fpl_dev should have all privileges on the database mini_fpl_db (and only this database)
-- mini_fpl_user should have SELECT privilege on the database performance_schema (and only this database)
-- If the database mini_fpl_db or the user mini_fpl_user already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS mini_fpl_db;
CREATE USER IF NOT EXISTS mini_fpl_user@'localhost' IDENTIFIED BY 'mini_fpl_pwd';
GRANT ALL PRIVILEGES ON mini_fpl_db.* TO mini_fpl_user@'localhost';
GRANT SELECT ON performance_schema.* TO mini_fpl_user@'localhost';
