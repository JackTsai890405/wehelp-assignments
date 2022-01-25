DROP DATABASE `website`;

CREATE DATABASE `website`;

USE `website`;

DESCRIBE `member`;

CREATE TABLE `member`(
	`id` BIGINT NOT NULL AUTO_INCREMENT, 
	`name` VARCHAR(255) NOT NULL,
    `username` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `follower_count` INT NOT NULL DEFAULT 0,
    `time` DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY (`id`)
);

SET SQL_SAFE_UPDATES = 0;

INSERT INTO `member`(`name`, `username`, `password`) VALUES ("test1234", "test1234", "test1234");

SELECT * FROM `member`;

SELECT * FROM `member` ORDER BY `time` DESC;

SELECT * FROM `member` ORDER BY `time` DESC LIMIT 1, 3;

SELECT * FROM `member` WHERE `username` = "test";

SELECT * FROM `member` WHERE `username` = "test" AND `password` = "test";

UPDATE `member` SET `name` = "test2" WHERE `username` = "test";

-- 取得 member 資料表中，總共有幾筆資料（幾位會員）
SELECT COUNT(*) FROM `member`;
-- 取得 member 資料表中，所有會員 follower_count 欄位的總和
SELECT SUM(`follower_count`) FROM `member`;
-- 取得 member 資料表中，所有會員 follower_count 欄位的平均數
SELECT AVG(`follower_count`) FROM `member`;

DESCRIBE `message`;
SELECT * FROM `message`;
CREATE TABLE `message`(
	`id` BIGINT NOT NULL AUTO_INCREMENT, 
	`member_id` BIGINT NOT NULL,
    `content` VARCHAR(255) NOT NULL,
    `time` DATETIME NOT NULL DEFAULT NOW(),
    PRIMARY KEY (`id`),
    FOREIGN KEY `message`(`member_id`) REFERENCES `member`(`id`)
);

-- Test
INSERT INTO `message`(`member_id`, `content`) VALUES ("5", "OXOXOX");
-- Test

-- Optional
SELECT `member`.`name`, `message`.`content` FROM `member` JOIN `message` ON `member`.`id` = `message`.`member_id`;
-- Optional
SELECT `member`.`name`, `message`.`content` FROM `member` 
JOIN `message` ON `member`.`id` = `message`.`member_id`
WHERE `member`.`username` = "test";