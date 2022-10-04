from ck_maptier import ck_maptier
from ck_zones import ck_zones
# read css maps
cssmaps = []
with open('cssmaps.txt') as f:
    for line in f:
        cssmaps.append(line.replace('\n', ''))

mapnamelist = [i[0] for i in ck_maptier]
maps = list(set(cssmaps) & set(mapnamelist))
notcommon = [value for value in cssmaps if value not in mapnamelist]

print(len(maps))

# maptiers


def add_maptiers():
    maptiers = """
DROP TABLE IF EXISTS `maptiers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `maptiers` (
  `map` varchar(255) NOT NULL,
  `tier` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`map`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;
INSERT INTO `maptiers` VALUES """

    for m in maps:
        item = [value for value in ck_maptier if m in value][0]
        maptiers += (f"('{item[0]}', {item[1]}),")

    maptiers = maptiers[:-1]+';'

    with open('bhoptimer/maptiers.sql', 'w') as f:
        f.write(maptiers)
# add_maptiers()

# zones


def add_zones():
    mapzones = """
DROP TABLE IF EXISTS `mapzones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mapzones` (
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;
INSERT INTO `mapzones` VALUES """
    i = 0
    for m in maps:

        items = [value for value in ck_zones if m in value]
        if items:
            for item in items:
                i += 1
                # map zonetypes surftimer (index) - bhoptimer (value)
                zonetypes = [3, 0, 1, 12, -1, -1, 2, -1, -1]
                if item[2] < 9 and zonetypes[item[2]] != -1:
                    mapzones += (
                        f"({i}, '{item[0]}', {zonetypes[item[2]]}, {item[3]}, {item[4]}, {item[5]}, {item[6]}, {item[7]}, {item[8]}, {item[9]}, 0, 0, 0, 0, 0, 0, '' ),")

    mapzones = mapzones[:-1]+';'

    with open('bhoptimer/mapzones.sql', 'w') as f:
        f.write(mapzones)


add_maptiers()
add_zones()
