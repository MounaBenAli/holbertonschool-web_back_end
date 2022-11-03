--  creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal

-- Requirements:
-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)


DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
DECLARE av_score FLOAT;
SET @av_score  = (SELECT AVG(score) WHERE corrections.user_id = user_id);
UPDATE users SET average_score = av_score  WHERE users.id = user_id;
END $$
DELIMITER ;