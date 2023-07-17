-- Удаление таблиц, если они существуют
drop table if exists Peers cascade;
drop table if exists Tasks cascade;
drop type if exists check_state cascade;
drop table if exists Checks cascade;
drop table if exists P2P cascade;
drop table if exists Verter cascade;
drop table if exists TransferredPoints cascade;
drop table if exists Friends cascade;
drop table if exists Recommendations cascade;
drop table if exists XP cascade;
drop table if exists TimeTracking cascade;

-- Создание всех заданных таблиц
create table Peers (
            Nickname    varchar not null primary key,
            Birthday    date not null
);

create table Tasks (
                       Title       varchar not null primary key,
                       ParentTask   varchar,
                       MaxXP       integer not null,
                       foreign key ( ParentTask ) references Tasks ( Title )
);

create table Checks (
                        ID      integer primary key not null,
                        Peer    varchar not null,
                        Task    varchar not null,
                        Date    date not null,
                        foreign key ( Peer ) references Peers ( Nickname ),
                        foreign key ( Task ) references Tasks ( Title )
);

create type check_state as enum ( 'Start', 'Success', 'Failure' );

create  table P2P (
                      ID              integer primary key not null,
                      "Check"         integer not null,
                      CheckingPeer    varchar not null,
                      State           check_state not null,
                      Time            time not null,
                      foreign key ( "Check" ) references Checks ( ID ),
                      foreign key ( CheckingPeer ) references Peers ( Nickname )
);

create table Verter (
                        ID      integer primary key not null,
                        "Check" integer not null,
                        State   check_state not null,
                        Time    time not null,
                        foreign key ( "Check" ) references Checks ( ID )
);

create table TransferredPoints (
                                   ID              integer primary key not null,
                                   CheckingPeer    varchar not null,
                                   CheckedPeer     varchar not null,
                                   PointsAmount    bigint not null,
                                   foreign key ( CheckingPeer ) references Peers ( Nickname ),
                                   foreign key ( CheckedPeer ) references Peers ( Nickname )
);

create table Friends (
                         ID      integer primary key not null,
                         Peer1   varchar not null,
                         Peer2   varchar not null,
                         foreign key ( Peer1 ) references Peers ( Nickname ),
                         foreign key ( Peer2 ) references Peers ( Nickname )
);

create table Recommendations (
                                 ID              integer primary key not null,
                                 Peer            varchar not null,
                                 RecommendedPeer varchar not null,
                                 foreign key ( Peer ) references Peers ( Nickname ),
                                 foreign key ( RecommendedPeer ) references Peers ( Nickname )
);

create table XP (
                    ID          integer primary key not null,
                    "Check"     integer not null,
                    XPAmount    integer not null,
                    foreign key ( "Check" ) references Checks ( ID )
);

create table TimeTracking (
                              ID  integer primary key not null,
                              Peer    varchar not null,
                              "Date"  date not null,
                              "Time"  time not null,
                              State   int2 not null check ( State in ( 1, 2 ) ),
                              foreign key ( Peer ) references Peers ( Nickname )
);

-- Заполнение таблиц данными
insert into Peers ( Nickname, Birthday )
    values ( 'achanel', '1992-02-02' ),
           ( 'mmonarch', '1991-10-20' ),
           ( 'rhoke', '1993-01-13' ),
           ( 'fbeatris', '1994-09-28' ),
           ( 'ikathrin', '1997-03-14' ),
           ( 'ikael', '1998-01-07' ),
           ( 'wsei', '1997-08-23' ),
           ( 'bgenia', '1996-06-09' );

insert into Tasks ( Title, ParentTask, MaxXP )
    values ( 'C2_SimpleBashUtils', NULL, 250 ),
           ( 'C3_s21_string+', 'C2_SimpleBashUtils', 500 ),
           ( 'C4_s21_math', 'C2_SimpleBashUtils', 300 ),
           ( 'C5_s21_decimal', 'C4_s21_math', 350 ),
           ( 'C6_s21_matrix', 'C5_s21_decimal', 200 ),
           ( 'C7_SmartCalc_v1.0', 'C6_s21_matrix', 500 ),
           ( 'C8_3DViewer_v1.0', 'C7_SmartCalc_v1.0', 750 ),
           ( 'DO1_Linux', 'C3_s21_string+', 300 ),
           ( 'DO2_Linux Network', 'DO1_Linux', 250 ),
           ( 'DO3_LinuxMonitoring v1.0', 'DO2_Linux Network', 350 ),
           ( 'DO4_LinuxMonitoring v2.0', 'DO3_LinuxMonitoring v1.0', 350 ),
           ( 'DO5_SimpleDocker', 'DO3_LinuxMonitoring v1.0', 300 ),
           ( 'DO6_CICD', 'DO5_SimpleDocker', 300 ),
           ( 'CPP1_s21_matrix+', 'C8_3DViewer_v1.0', 300 ),
           ( 'CPP2_s21_containers', 'CPP1_s21_matrix+', 350 ),
           ( 'CPP3_SmartCalc_v2.0', 'CPP2_s21_containers', 600 ),
           ( 'CPP4_3DViewer_v2.0', 'CPP3_SmartCalc_v2.0', 750 ),
           ( 'CPP5_3DViewer_v2.1', 'CPP4_3DViewer_v2.0', 600 ),
           ( 'CPP6_3DViewer_v2.2', 'CPP4_3DViewer_v2.0', 800 ),
           ( 'CPP7_MLP', 'CPP4_3DViewer_v2.0', 700 ),
           ( 'CPP8_PhotoLab_v1.0', 'CPP4_3DViewer_v2.0', 450 ),
           ( 'CPP9_MonitoringSystem', 'CPP4_3DViewer_v2.0', 1000 ),
           ( 'A1_Maze', 'CPP4_3DViewer_v2.0', 300 ),
           ( 'A2_SimpleNavigator v1.0', 'A1_Maze', 400 ),
           ( 'A3_Parallels', 'A2_SimpleNavigator v1.0', 300 ),
           ( 'A4_Crypto', 'A2_SimpleNavigator v1.0', 350 ),
           ( 'A5_s21_memory', 'A2_SimpleNavigator v1.0', 400 ),
           ( 'A6_Transactions', 'A2_SimpleNavigator v1.0', 700 ),
           ( 'A7_DNA Analyzer', 'A2_SimpleNavigator v1.0', 800 ),
           ( 'A8_Algorithmic trading', 'A2_SimpleNavigator v1.0', 800 ),
           ( 'SQL1_Bootcamp', 'C8_3DViewer_v1.0', 1500 ),
           ( 'SQL2_Info21 v1.0', 'SQL1_Bootcamp', 500 ),
           ( 'SQL3_RetailAnalitycs v1.0', 'SQL2_Info21 v1.0', 600 );

insert into Checks ( ID, Peer, Task, Date )
    values ( 1, 'bgenia', 'SQL1_Bootcamp', '2023-06-09' ),
           ( 2, 'rhoke', 'A6_Transactions', '2022-12-14' ),
           ( 3, 'wsei', 'A3_Parallels', '2023-01-06' ),
           ( 4, 'fbeatris', 'CPP9_MonitoringSystem', '2023-02-26' ),
           ( 5, 'ikathrin', 'CPP6_3DViewer_v2.2', '2023-01-20' ),
           ( 6, 'mmonarch', 'CPP2_s21_containers', '2022-06-30' ),
           ( 7, 'achanel', 'DO1_Linux', '2022-05-09' ),
           ( 8, 'rhoke', 'A7_DNA Analyzer', '2022-11-09' ),
           ( 9, 'achanel', 'DO2_Linux Network', '2022-11-30' );

insert into P2P ( ID, "Check", CheckingPeer, State, Time )
    values ( 1, 1, 'achanel', 'Start', '18:30:21' ),
           ( 2, 1, 'achanel', 'Success', '19:01:12' ),

           ( 3, 2, 'mmonarch', 'Start', '13:02:01' ),
           ( 4, 2, 'mmonarch', 'Success', '13:10:01' ),

           ( 5, 3, 'ikathrin', 'Start', '09:11:45' ),
           ( 6, 3, 'ikathrin', 'Failure', '11:06:23' ),

           ( 7, 4, 'rhoke', 'Start', '19:10:45' ),
           ( 8, 4, 'rhoke', 'Success', '20:06:23' ),

           ( 9, 5, 'ikael', 'Start', '20:11:45' ),
           ( 10, 5, 'ikael', 'Success', '20:15:23' ),

           ( 11, 6, 'wsei', 'Start', '00:00:00' ),

           ( 12, 7, 'bgenia', 'Start', '11:11:45' ),
           ( 13, 7, 'bgenia', 'Success', '11:15:23' ),

           ( 14, 8, 'achanel', 'Start', '10:51:45' ),
           ( 15, 8, 'achanel', 'Success', '11:15:13' );

insert into Verter ( ID, "Check", State, Time )
    values ( 1, 1, 'Start', '19:21:12' ),
           ( 2, 1, 'Success', '19:51:12' ),

           ( 3, 2, 'Start', '13:30:01' ),
           ( 4, 2, 'Success', '14:00:01' ),

           ( 5, 4, 'Start', '20:26:23' ),
           ( 6, 4, 'Success', '20:56:23' ),

           ( 7, 5, 'Start', '19:21:12' ),
           ( 8, 5, 'Success', '19:51:12' ),

           ( 9, 7, 'Start', '11:35:23' ),
           ( 10, 7, 'Failure', '12:05:23' ),

           ( 11, 8, 'Start', '11:35:13' ),
           ( 12, 8, 'Success', '12:05:13' );

insert into TransferredPoints ( ID, CheckingPeer, CheckedPeer, PointsAmount )
    values ( 1, 'achanel', 'bgenia', 1),
           ( 2, 'mmonarch', 'rhoke', 1),
           ( 3, 'ikathrin', 'wsei', 1),
           ( 4, 'rhoke', 'fbeatris', 1),
           ( 5, 'ikael', 'ikathrin', 1),
           ( 6, 'bgenia', 'achanel', 1),
           ( 7, 'achanel', 'rhoke', 1);

insert into Friends ( ID, Peer1, Peer2 )
    values ( 1, 'achanel', 'mmonarch' ),
           ( 2, 'achanel', 'ikathrin' ),
           ( 3, 'ikael', 'wsei' ),
           ( 4, 'ikathrin', 'mmonarch' ),
           ( 5, 'mmonarch', 'rhoke' ),
           ( 6, 'fbeatris', 'wsei' ),
           ( 7, 'wsei', 'achanel' ),
           ( 8, 'bgenia', 'rhoke' );

insert into Recommendations ( ID, Peer, RecommendedPeer )
    values ( 1, 'achanel', 'mmonarch'),
           ( 2, 'achanel', 'rhoke'),
           ( 3, 'rhoke', 'wsei'),
           ( 4, 'ikael', 'fbeatris'),
           ( 5, 'mmonarch', 'bgenia'),
           ( 6, 'bgenia', 'ikathrin'),
           ( 7, 'ikael', 'achanel'),
           ( 8, 'mmonarch', 'achanel');

insert into XP ( ID, "Check", XPAmount )
    values ( 1, 1, 1500),
           ( 2, 2, 700),
           ( 3, 4, 1000),
           ( 4, 5, 800),
           ( 5, 8, 800);

insert into TimeTracking ( ID, Peer, "Date", "Time", State )
    values ( 1, 'mmonarch', '2023-01-30', '11:05:16', 1 ),
           ( 2, 'mmonarch', '2023-01-30', '20:15:22', 2 ),
           ( 3, 'achanel', '2023-02-01', '17:13:01', 1 ),
           ( 4, 'achanel', '2023-02-01', '03:10:12', 2 ),
           ( 5, 'rhoke', '2022-09-03', '12:45:38', 1 ),
           ( 6, 'rhoke', '2022-09-03', '22:43:56', 2 ),
           ( 7, 'ikathrin', '2022-12-23', '08:00:00', 1 ),
           ( 8, 'ikathrin', '2023-12-23', '21:00:00', 2 ),
           ( 9, 'wsei', '2020-01-02', '00:00:00', 1 );


CREATE INDEX idx_person_visits_person_id ON person_visits (person_id);
CREATE INDEX idx_person_visits_pizzeria_id ON person_visits (pizzeria_id);
CREATE INDEX idx_menu_pizzeria_id ON menu (pizzeria_id);
CREATE INDEX idx_person_order_person_id ON person_order (person_id);
CREATE INDEX idx_person_order_menu_id ON person_order (menu_id);
