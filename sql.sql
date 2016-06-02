DROP DATABASE IF EXISTS conSpider;

CREATE DATABASE conSpider;

USE conSpider;

CREATE TABLE Links (
	lid int unsigned NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name varchar(5) binary NOT NULL default '',
	linkedto varchar(255) binary NOT NULL default '',
	position varchar(255) binary NOT NULL default '',
	source varchar(255) binary NOT NULL default '',
	phone varchar(255) binary NOT NULL default '',
	email varchar(255) binary NOT NULL default '',
	address varchar(255) binary NOT NULL default '',
	li varchar(255) binary NOT NULL default '',
	fb varchar(255) binary NOT NULL default '',
);

CREATE TABLE Linkedin (
	liid int unsigned NOT NULL PRIMARY KEY AUTO_INCREMENT,
	memberslinks varchar(255) binary NOT NULL default '',
	followed char(5) binary NOT NULL default '',
);
