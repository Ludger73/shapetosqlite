# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ShapeToSQLite
                                 A QGIS plugin
 The plugin is for saving shapefiles into a SQLite database
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-06-21
        copyright            : (C) 2018 by x
        email                : x@y.de
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ShapeToSQLite class from file ShapeToSQLite.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .shape_to_sqlite import ShapeToSQLite
    return ShapeToSQLite(iface)
