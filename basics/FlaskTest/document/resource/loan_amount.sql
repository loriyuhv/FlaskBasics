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

 Date: 19/10/2021 13:37:35
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for loan_amount
-- ----------------------------
DROP TABLE IF EXISTS `loan_amount`;
CREATE TABLE `loan_amount`  (
  `zone` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `num` int(0) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of loan_amount
-- ----------------------------
INSERT INTO `loan_amount` VALUES ('0-1000', 2623);
INSERT INTO `loan_amount` VALUES ('1000-5000', 100057);
INSERT INTO `loan_amount` VALUES ('5000-10000', 232900);
INSERT INTO `loan_amount` VALUES ('10000-20000', 350962);
INSERT INTO `loan_amount` VALUES ('20000-50000', 200537);

SET FOREIGN_KEY_CHECKS = 1;
