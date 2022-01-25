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
DELETE FROM `member` WHERE `name` = "test";
INSERT INTO `member`(`name`, `username`, `password`) VALUES ("test", "test", "test");
-- 使用 SELECT 指令取得所有在 member 資料表中的會員資料
SELECT * FROM `member`;
-- 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序
SELECT * FROM `member` ORDER BY `time` DESC;
-- 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序
SELECT * FROM `member` ORDER BY `time` DESC LIMIT 1, 3;
-- 使用 SELECT 指令取得欄位 username 是 test 的會員資料
SELECT * FROM `member` WHERE `username` = "test";
-- 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料
SELECT * FROM `member` WHERE `username` = "test" AND `password` = "test";
-- 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2
UPDATE `member` SET `name` = "test2" WHERE `username` = "test";

-- 取得 member 資料表中，總共有幾筆資料（幾位會員）
SELECT COUNT(*) FROM `member`;
-- 取得 member 資料表中，所有會員 follower_count 欄位的總和
SELECT SUM(`follower_count`) FROM `member`;
-- 取得 member 資料表中，所有會員 follower_count 欄位的平均數
SELECT AVG(`follower_count`) FROM `member`;

-- 在資料庫中，建立新資料表，取名字為 message，資料表中必須包含以下欄位設定
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
-- 取得所有留言，結果須包含留言者會員的姓名
SELECT `member`.`name`, `message`.`content` FROM `member` JOIN `message` ON `member`.`id` = `message`.`member_id`;
-- 取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名
SELECT `member`.`name`, `message`.`content` FROM `member` 
JOIN `message` ON `member`.`id` = `message`.`member_id`
WHERE `member`.`username` = "test";