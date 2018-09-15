create table user(
city varchar(20),
user_id varchar(20) primary key,
name varchar(20),
user_url varchar(50),
attention int,
register_time date,
sex varchar(10),
fans int,
contribution int,
inter int
);

load data local infile 'D:\\user.CSV' into table user character set utf8 fields terminated by ',';


create table comment(
star int,
shop_url varchar(40),
comment_id varchar(20) primary key,
support_num varchar(10),
shop_name varchar(40),
content text,
shop_id varchar(20), 
shop_kind varchar(20),
comment_time varchar(20),
user_id varchar(20)
)


load data local infile 'D:\\comment.CSV' into table comment character set utf8 fields terminated by ',' optionally enclosed by '"' escaped by '"';