/*
 Navicat Premium Data Transfer

 Source Server         : loriyuhv
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 19/10/2021 13:37:47
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for loan_grade
-- ----------------------------
DROP TABLE IF EXISTS `loan_grade`;
CREATE TABLE `loan_grade`  (
  `grade` varchar(5) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `subgrade` varchar(5) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `num` int(0) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of loan_grade
-- ----------------------------
INSERT INTO `loan_grade` VALUES ('A', '1', 16654);
INSERT INTO `loan_grade` VALUES ('B', '1', 23498);
INSERT INTO `loan_grade` VALUES ('C', '1', 33180);
INSERT INTO `loan_grade` VALUES ('D', '1', 25181);
INSERT INTO `loan_grade` VALUES ('E', '1', 14388);
INSERT INTO `loan_grade` VALUES ('F', '1', 12460);
INSERT INTO `loan_grade` VALUES ('G', '1', 9654);
INSERT INTO `loan_grade` VALUES ('A', '2', 10206);
INSERT INTO `loan_grade` VALUES ('B', '2', 27320);
INSERT INTO `loan_grade` VALUES ('C', '2', 33561);
INSERT INTO `loan_grade` VALUES ('D', '2', 20894);
INSERT INTO `loan_grade` VALUES ('E', '2', 13672);
INSERT INTO `loan_grade` VALUES ('F', '2', 11432);
INSERT INTO `loan_grade` VALUES ('G', '2', 8904);
INSERT INTO `loan_grade` VALUES ('A', '3', 11892);
INSERT INTO `loan_grade` VALUES ('B', '3', 32698);
INSERT INTO `loan_grade` VALUES ('C', '3', 33993);
INSERT INTO `loan_grade` VALUES ('D', '3', 18867);
INSERT INTO `loan_grade` VALUES ('E', '3', 12491);
INSERT INTO `loan_grade` VALUES ('F', '3', 10923);
INSERT INTO `loan_grade` VALUES ('G', '3', 9200);
INSERT INTO `loan_grade` VALUES ('A', '4', 18350);
INSERT INTO `loan_grade` VALUES ('B', '4', 33683);
INSERT INTO `loan_grade` VALUES ('C', '4', 34491);
INSERT INTO `loan_grade` VALUES ('D', '4', 18960);
INSERT INTO `loan_grade` VALUES ('E', '4', 12800);
INSERT INTO `loan_grade` VALUES ('F', '4', 10230);
INSERT INTO `loan_grade` VALUES ('G', '4', 9640);
INSERT INTO `loan_grade` VALUES ('A', '5', 25503);
INSERT INTO `loan_grade` VALUES ('B', '5', 30564);
INSERT INTO `loan_grade` VALUES ('C', '5', 29132);
INSERT INTO `loan_grade` VALUES ('D', '5', 16196);
INSERT INTO `loan_grade` VALUES ('E', '5', 11013);
INSERT INTO `loan_grade` VALUES ('F', '5', 9800);
INSERT INTO `loan_grade` VALUES ('G', '5', 8800);

SET FOREIGN_KEY_CHECKS = 1;
