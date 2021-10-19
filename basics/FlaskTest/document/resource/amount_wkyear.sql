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

 Date: 19/10/2021 13:37:14
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for amount_wkyear
-- ----------------------------
DROP TABLE IF EXISTS `amount_wkyear`;
CREATE TABLE `amount_wkyear`  (
  `wkyears` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `amount` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `num` int(0) NULL DEFAULT NULL
) ENGINE = MyISAM AUTO_INCREMENT = 26 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of amount_wkyear
-- ----------------------------
INSERT INTO `amount_wkyear` VALUES ('1', '0-1000', 9940);
INSERT INTO `amount_wkyear` VALUES ('2', '0-1000', 12344);
INSERT INTO `amount_wkyear` VALUES ('3', '0-1000', 6344);
INSERT INTO `amount_wkyear` VALUES ('4', '0-1000', 34554);
INSERT INTO `amount_wkyear` VALUES ('5', '0-1000', 23485);
INSERT INTO `amount_wkyear` VALUES ('1', '1000-5000', 23000);
INSERT INTO `amount_wkyear` VALUES ('2', '1000-5000', 12393);
INSERT INTO `amount_wkyear` VALUES ('3', '1000-5000', 43993);
INSERT INTO `amount_wkyear` VALUES ('4', '1000-5000', 23939);
INSERT INTO `amount_wkyear` VALUES ('5', '1000-5000', 16949);
INSERT INTO `amount_wkyear` VALUES ('1', '5000-10000', 23949);
INSERT INTO `amount_wkyear` VALUES ('2', '5000-10000', 43994);
INSERT INTO `amount_wkyear` VALUES ('3', '5000-10000', 54994);
INSERT INTO `amount_wkyear` VALUES ('4', '5000-10000', 23993);
INSERT INTO `amount_wkyear` VALUES ('5', '5000-10000', 12939);
INSERT INTO `amount_wkyear` VALUES ('1', '10000-20000', 34949);
INSERT INTO `amount_wkyear` VALUES ('2', '10000-20000', 54949);
INSERT INTO `amount_wkyear` VALUES ('3', '10000-20000', 23993);
INSERT INTO `amount_wkyear` VALUES ('4', '10000-20000', 54939);
INSERT INTO `amount_wkyear` VALUES ('5', '10000-20000', 23994);
INSERT INTO `amount_wkyear` VALUES ('1', '20000-50000', 12389);
INSERT INTO `amount_wkyear` VALUES ('2', '20000-50000', 23445);
INSERT INTO `amount_wkyear` VALUES ('3', '20000-50000', 12334);
INSERT INTO `amount_wkyear` VALUES ('4', '20000-50000', 12333);
INSERT INTO `amount_wkyear` VALUES ('5', '20000-50000', 9000);

SET FOREIGN_KEY_CHECKS = 1;
