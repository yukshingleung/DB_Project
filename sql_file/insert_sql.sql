# create database
create database shopDB;
use shopDB;

# create table
create table shop(
 sid char(10),
 sname varchar(25) not null,
 rating int not null,
 location varchar(25) not null,
 primary key (sid));

create table item(
iid char(10),
iname varchar(25) not null,
price double not null,
kw1 varchar(25),
kw2 varchar(25),
kw3 varchar(25),
qty int not null,
sid char(10),
primary key (sid, iid),
constraint fk_sid foreign key (sid) references shop (sid));

create table customer(
cid char(10),
cname varchar(11) not null,
tel varchar(11) not null,
addr varchar(25) not null,
primary key (cid));

create table orderlist(
oid int not null,
cid char(10),
iid char(10),
sid char(10),
qty int not null,
primary key (oid, iid, sid),
constraint fk_cid foreign key (cid) references customer (cid),
constraint fk_sid_iid foreign key (sid, iid) references item (sid, iid));

# insert data
insert into shop (sid, sname, rating, location) values
('S1', 'Fruit shop', 5, 'Lok Fu'),
('S2', 'Phone shop', 5, 'Mong Kok'),
('S3', 'Book shop', 4, 'Kowloon Tong');
insert into customer values
('C1', 'HUANG', '1111', 'Tuen Mun'),
('C2', 'LIANG', '2222', 'Diamond Hill'),
('C3', 'LIU', '3333', 'Tai Wai');
insert into item (iid, iname, price, kw1, kw2, kw3, qty, sid) values
('I1', 'Apple', 10, 'Red', 'Sweet', null, 200, 'S1'),
('I2', 'Orange', 8, 'Yellow', 'Fresh', 'Australia', 100, 'S1'),
('I3', 'Apple', 8000, 'Red', '256G', null, 50, 'S2'),
('I4', 'Samsung', 7000, 'Black', '128G', 'Folding', 20, 'S2'),
('I5', 'DB', 500, 'Paperback', 'Relational', 'SQL', 90, 'S3'),
('I3', 'AI', 400, 'Paperback', 'Deep Learning', 'Python', 95, 'S3');
delimiter ||
# trigger1
create trigger tg1
after insert on orderlist
for each row
begin
	update item set qty=qty-new.qty where iid = new.iid and sid = new.sid;
end
||
# trigger2
create trigger tg2
after delete on orderlist
for each row
begin
	update item set qty=qty+old.qty where iid = old.iid and sid = old.sid;
end

# trigger3
||
create trigger tg3
after update on orderlist
for each row
begin
	update item set qty=qty-(new.qty-old.qty) where iid = new.iid and sid = new.sid;
end