INSERT INTO artist (artist_name) VALUES
('Smes');

INSERT INTO release (release_name) VALUES
('Roadkill');

INSERT INTO "user" (user_name, email, passwordhash) VALUES
('michaelakasmes', 'S.Michael.ES@protonmail.com', '$2y$10$jqypodSQNWE/C3EO67/f3O3LK/ukde6Gdvcj3XV/uM8zmg7/n/dje');


INSERT INTO track (track_title, release_id, length, date_posted) VALUES
('Roadkill', 1, 186, NOW());

INSERT INTO artist_release (artist_id, release_id) VALUES
(1, 1);

INSERT INTO user_release (user_id, release_id) VALUES
(1, 1);