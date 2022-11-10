# SpiderExample

## 介绍

此项目是爬虫框架[Spider](https://github.com/Boris-code/feapder) 学习用例。

对网易新闻`https://news.163.com/domestic/`进行数据爬取。 使用Selenium采集动态页面（Ajax渲染的页面）,xpath解析文档路径,获取目标数据后进行入库。

## 数据库设计

```sql
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for spider_data
-- ----------------------------
DROP TABLE IF EXISTS `spider_data`;
CREATE TABLE `spider_data` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `img_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `detail_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `content` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=214 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

SET FOREIGN_KEY_CHECKS = 1;
```
