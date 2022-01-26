# WeHelp Bootcamp 第五週作業

### 要求三
* SELECT * FROM `member`;
![](https://raw.githubusercontent.com/JackTsai890405/wehelp-assignments/master/week-5/q3_images/取得所有會員資料.jpg)
* SELECT * FROM `member` ORDER BY `time` DESC;
![](https://raw.githubusercontent.com/JackTsai890405/wehelp-assignments/master/week-5/q3_images/order_by_desc.jpg)
* SELECT * FROM `member` ORDER BY `time` DESC LIMIT 1, 3;
![](https://raw.githubusercontent.com/JackTsai890405/wehelp-assignments/master/week-5/q3_images/order_by_desc_limit.jpg)
* SELECT * FROM `member` WHERE `username` = "test";
![](https://raw.githubusercontent.com/JackTsai890405/wehelp-assignments/master/week-5/q3_images/where篩選.jpg)
* SELECT * FROM `member` WHERE `username` = "test" AND `password` = "test";
![](https://raw.githubusercontent.com/JackTsai890405/wehelp-assignments/master/week-5/q3_images/where篩選2.jpg)
* UPDATE `member` SET `name` = "test2" WHERE `username` = "test";

### 要求四
* SELECT COUNT(*) FROM `member`;
![](https://raw.githubusercontent.com/JackTsai890405/wehelp-assignments/master/week-5/q4_images/count_member.jpg)
* SELECT SUM(`follower_count`) FROM `member`;
![](https://raw.githubusercontent.com/JackTsai890405/wehelp-assignments/master/week-5/q4_images/sum_member.jpg)
* SELECT AVG(`follower_count`) FROM `member`;
![](https://raw.githubusercontent.com/JackTsai890405/wehelp-assignments/master/week-5/q4_images/average_member.jpg)

### 要求五
* SELECT `member`.`name`, `message`.`content` FROM `member` JOIN `message` ON `member`.`id` = `message`.`member_id`;
![](https://raw.githubusercontent.com/JackTsai890405/wehelp-assignments/master/week-5/q5_images/get_all_content.jpg)
* SELECT `member`.`name`, `message`.`content` FROM `member` 
JOIN `message` ON `member`.`id` = `message`.`member_id`
WHERE `member`.`username` = "test";
![](https://raw.githubusercontent.com/JackTsai890405/wehelp-assignments/master/week-5/q5_images/get_username_is_test_content.jpg)
