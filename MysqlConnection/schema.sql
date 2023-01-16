CREATE DATABASE IF NOT EXISTS cricinfosystem2;
USE cricinfoSystem2;

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS person;
CREATE TABLE person
(
  DOB DATE NOT NULL DEFAULT (DATE(DATE_SUB(NOW(), INTERVAL ROUND(RAND()*15300) DAY))),
  image_url  varchar(23),
  Country varchar(46) NOT NULL,
  ID INT NOT NULL AUTO_INCREMENT,
  First_name varchar(60) NOT NULL,
  Last_Name varchar(60) NOT NULL,
  PRIMARY KEY (ID)
);

DROP TABLE IF EXISTS player;
CREATE TABLE player
(
  player_id INT NOT NULL ,
  First_name varchar(60) NOT NULL,
  Last_Name varchar(60) NOT NULL,
  Country varchar(60) NOT NULL,
  DOB DATE NOT NULL DEFAULT (DATE(DATE_SUB(NOW(), INTERVAL ROUND(RAND()*15300) DAY))),
  Batting_style varchar(60),
  Bowling_style varchar(60),
  fk_ID INT NOT NULL,
  PRIMARY KEY (player_id)
);

DROP TABLE IF EXISTS Umpire;
CREATE TABLE Umpire
(
umpire_id INT NOT NULL AUTO_INCREMENT,
matches_ODI INT NOT NULL,
matches_T20 INT NOT NULL,
matches_Test int not null,
  fk_ID INT NOT NULL,
  PRIMARY KEY (umpire_id),
  FOREIGN KEY (fk_ID) REFERENCES person(ID)
);

DROP TABLE IF EXISTS team;
CREATE TABLE team
(
  team_id int not null,
  image_url varchar(23),
  team_name varchar(46) NOT NULL,
  isInternational boolean default 1,
  PRIMARY KEY (team_id,team_name)
);


DROP TABLE IF EXISTS awards;
CREATE TABLE awards
(
  award_name INT NOT NULL,
  award_year INT NOT NULL,
  fk_player_id INT NOT NULL,
  PRIMARY KEY (award_name, award_year),
  FOREIGN KEY (fk_player_id) REFERENCES player(player_id)
);

DROP TABLE IF EXISTS Location;
Create table Location(
locationId int not null,
StadiumName varchar(34) not null,
StadiumCapacity int not null,
CityName varchar(34) not null,
CountryName varchar(34) not null,
primary key (locationId)

);

Drop Table if exists Series;
Create table Series(
series_id int not null auto_increment,
isTournament boolean,
Title varchar(46),
season varchar(46),
player_of_series int,
primary key(series_id)

);

drop table if exists tournamentstanding;
create table tournamentstanding(
series_id int not null,
team_id int not null,
played int,
win int ,
lost int,
foreign key(series_id) references Series(series_id),
foreign key(team_id) references team(team_id)
);

DROP TABLE IF EXISTS MatchFixture;
Create table MatchFixture(
Match_id int not null,
series_id int not null,
match_type varchar(60) not null,
MatchDate date ,
event_name varchar(60) not null,
event_stage varchar(60) not null,
field_umpire_1 varchar(60) not null,
field_umpire_2 varchar(60) not null,
TV_empire varchar(60) not null,
fk_team_1_id int not null,
fk_team_2_id int not null,
Matchwinner int,
Matchwinner_desc varchar(600),
player_of_match int not null,
primary key(Match_id),
foreign key(fk_team_1_id) references team(team_id),
foreign key(fk_team_2_id) references team(team_id),
foreign key(series_id) references series(series_id),
CONSTRAINT wc_valid_winner CHECK 
   (
    (Matchwinner = fk_team_1_id OR Matchwinner = fk_team_2_id OR Matchwinner = NULL)
   )
);

DROP TABLE IF EXISTS Inning;
Create Table Inning(
Inning_id int not null,
Inning_Number int not null,
fk_match_id int not null,
overs int not null ,
TotalRunsScored int not null default 0,
RemainingWickets int not null default 10,
primary key(Inning_id),
foreign key (fk_match_id) references MatchFixture(Match_id)
);

Drop table if exists Balls;
Create Table Balls(
Match_id  int default 0,
inning  int default 0,
BallNumber int,
OverNumber int,
extra_runs int,
scored_runs int,
bowler int not null,
batter int not null,
foreign key(Match_id) references matchfixture(Match_id),
primary key(Match_id,inning,OverNumber,BallNumber)
);

DROP TABLE IF EXISTS BatterStatsInInning;
Create Table BatterStatsInInning(
fk_Match_Id int not null,
InningNumber int not null,
fk_batter_id int not null,
runs_scored int not null default 0,
ballfaced int not null default 0,
Primary key(fk_Match_Id,InningNumber,fk_batter_id),
foreign key(fk_Match_id) references matchfixture(match_id)
);

DROP TABLE IF EXISTS BowlerStatsInInning;
Create Table BowlerStatsInInning(
fk_Match_Id int not null,
InningNumber int not null,
fk_bowler_id int not null,
runs int not null default 0,
deliveries int not null default 0,
Primary key(fk_Match_Id,InningNumber,fk_bowler_id),
foreign key(fk_Match_id) references matchfixture(match_id)
);

drop table if exists wicketstatsinnings;
Create Table wicketstatsinnings(
BatterId int,
BowlerId int,
InningNumber int,
fk_match_id int,
OverNumber int,
BallNumber int,
WicketDescription varchar(60),
foreign key(fk_Match_id) references matchfixture(match_id),
primary key(fk_match_id,InningNumber,BowlerId,BatterId)
);
