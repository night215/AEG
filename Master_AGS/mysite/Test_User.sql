--CREATE TABLE auth_user(id INTEGER NOT NULL PRIMARY KEY, username, password, first_name, last_name, email, is_superuser BOOLEAN NOT NULL, is_staff BOOLEAN NOT NULL, is_active BOOLEAN NOT NULL, date_joined, last_login);

--INSERT INTO auth_user(id, username, password, first_name, last_name, email, is_superuser, is_staff, is_active, date_joined, last_login)
--VALUES(2, "PParthav99", "Parthav40", "Parthav", "Pillai", "yeshparth99@gmail.com", 1, 0, 1, 2023, strftime('%Y-%m-%d %H:%M:%S', 'now'));

--UPDATE auth_user
--SET date_joined = '2023-01-08 09:33:19'
--WHERE id = 2;

--INSERT INTO auth_group(id, name)
--VALUES(1, "Harish");

SELECT sql FROM sqlite_master WHERE type='table' AND name='auth_user';
