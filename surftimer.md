# surftimer

## Tables

### ck_maptier

**mapname** varchar(54) NOT NULL,
**tier** int(12) NOT NULL,
**maxvelocity** float NOT NULL DEFAULT '3500',
**announcerecord** int(11) NOT NULL DEFAULT '0',
**gravityfix** int(11) NOT NULL DEFAULT '1',
**ranked** int(11) NOT NULL DEFAULT '1',
**stages** int(11) DEFAULT NULL,
**bonuses** int(11) DEFAULT NULL,
**mapper** varchar(64) DEFAULT 'N/A',
PRIMARY KEY (**mapname**)

### ck_zones

`mapname` varchar(54) NOT NULL,
`zoneid` int(12) NOT NULL DEFAULT '-1',
`zonetype` int(12) DEFAULT '-1',
`zonetypeid` int(12) DEFAULT '-1',
`pointa_x` float DEFAULT '-1',
`pointa_y` float DEFAULT '-1',
`pointa_z` float DEFAULT '-1',
`pointb_x` float DEFAULT '-1',
`pointb_y` float DEFAULT '-1',
`pointb_z` float DEFAULT '-1',
`vis` int(12) DEFAULT '0',
`team` int(12) DEFAULT '0',
`zonegroup` int(11) NOT NULL DEFAULT '0',
`zonename` varchar(128) DEFAULT NULL,
`hookname` varchar(128) DEFAULT 'None',
`targetname` varchar(128) DEFAULT 'player',
`onejumplimit` int(12) NOT NULL DEFAULT '1',
`prespeed` int(64) NOT NULL DEFAULT '350',
PRIMARY KEY (`mapname`,`zoneid`)
