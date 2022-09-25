# bhoptimer

https://github.com/shavitush/bhoptimer

## Tables

### maptiers

`map` varchar(255) NOT NULL,
`tier` int(11) NOT NULL DEFAULT '1',
PRIMARY KEY (`map`)

### mapzones

`id` int(11) NOT NULL AUTO_INCREMENT,
`map` varchar(255) NOT NULL,
`type` int(11) DEFAULT NULL,
`track` tinyint(4) NOT NULL,
`corner1_x` float DEFAULT NULL,
`corner1_y` float DEFAULT NULL,
`corner1_z` float DEFAULT NULL,
`corner2_x` float DEFAULT NULL,
`corner2_y` float DEFAULT NULL,
`corner2_z` float DEFAULT NULL,
`destination_x` float NOT NULL DEFAULT '0',
`destination_y` float NOT NULL DEFAULT '0',
`destination_z` float NOT NULL DEFAULT '0',
`flags` int(11) NOT NULL DEFAULT '0',
`data` int(11) NOT NULL DEFAULT '0',
`form` tinyint(4) DEFAULT NULL,
`target` varchar(63) DEFAULT NULL,

### startpositions

`auth` int(11) NOT NULL,
`track` tinyint(4) NOT NULL,
`map` varchar(255) NOT NULL,
`pos_x` float DEFAULT NULL,
`pos_y` float DEFAULT NULL,
`pos_z` float DEFAULT NULL,
`ang_x` float DEFAULT NULL,
`ang_y` float DEFAULT NULL,
`ang_z` float DEFAULT NULL,
`angles_only` tinyint(1) DEFAULT NULL,


