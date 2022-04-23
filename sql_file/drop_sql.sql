drop trigger if exists tg1;
drop trigger if exists tg2;
drop trigger if exists tg3;

alter table orderlist drop constraint fk_cid;
alter table orderlist drop constraint fk_sid_iid;

alter table item drop constraint fk_sid;

drop table orderlist;
drop table customer;
drop table item;
drop table shop;
drop database shopDB;