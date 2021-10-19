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

 Date: 19/10/2021 13:37:27
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for grade_amount
-- ----------------------------
DROP TABLE IF EXISTS `grade_amount`;
CREATE TABLE `grade_amount`  (
  `grade` varchar(5) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `amount` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `num` int(0) NULL DEFAULT NULL
) ENGINE = MyISAM AUTO_INCREMENT = 36 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of grade_amount
-- ----------------------------
INSERT INTO `grade_amount` VALUES ('A', '0-1000', 22000);
INSERT INTO `grade_amount` VALUES ('B', '0-1000', 30300);
INSERT INTO `grade_amount` VALUES ('C', '0-1000', 23403);
INSERT INTO `grade_amount` VALUES ('D', '0-1000', 43020);
INSERT INTO `grade_amount` VALUES ('E', '0-1000', 23440);
INSERT INTO `grade_amount` VALUES ('F', '0-1000', 32990);
INSERT INTO `grade_amount` VALUES ('G', '0-1000', 12239);
INSERT INTO `grade_amount` VALUES ('A', '1000-5000', 30394);
INSERT INTO `grade_amount` VALUES ('B', '1000-5000', 43039);
INSERT INTO `grade_amount` VALUES ('C', '1000-5000', 53403);
INSERT INTO `grade_amount` VALUES ('D', '1000-5000', 34040);
INSERT INTO `grade_amount` VALUES ('E', '1000-5000', 23930);
INSERT INTO `grade_amount` VALUES ('F', '1000-5000', 18393);
INSERT INTO `grade_amount` VALUES ('G', '1000-5000', 12300);
INSERT INTO `grade_amount` VALUES ('A', '5000-10000', 23439);
INSERT INTO `grade_amount` VALUES ('B', '5000-10000', 43939);
INSERT INTO `grade_amount` VALUES ('C', '5000-10000', 12939);
INSERT INTO `grade_amount` VALUES ('D', '5000-10000', 34459);
INSERT INTO `grade_amount` VALUES ('E', '5000-10000', 23994);
INSERT INTO `grade_amount` VALUES ('F', '5000-10000', 12239);
INSERT INTO `grade_amount` VALUES ('G', '5000-10000', 9009);
INSERT INTO `grade_amount` VALUES ('A', '10000-20000', 12399);
INSERT INTO `grade_amount` VALUES ('B', '10000-20000', 43900);
INSERT INTO `grade_amount` VALUES ('C', '10000-20000', 53994);
INSERT INTO `grade_amount` VALUES ('D', '10000-20000', 23994);
INSERT INTO `grade_amount` VALUES ('E', '10000-20000', 69304);
INSERT INTO `grade_amount` VALUES ('F', '10000-20000', 50939);
INSERT INTO `grade_amount` VALUES ('G', '10000-20000', 49030);
INSERT INTO `grade_amount` VALUES ('A', '20000-50000', 34455);
INSERT INTO `grade_amount` VALUES ('B', '20000-50000', 69505);
INSERT INTO `grade_amount` VALUES ('C', '20000-50000', 79669);
INSERT INTO `grade_amount` VALUES ('D', '20000-50000', 34995);
INSERT INTO `grade_amount` VALUES ('E', '20000-50000', 66959);
INSERT INTO `grade_amount` VALUES ('F', '20000-50000', 89348);
INSERT INTO `grade_amount` VALUES ('G', '20000-50000', 34994);

SET FOREIGN_KEY_CHECKS = 1;
