# -*- coding: utf-8 -*-

"""
/***************************************************************************
 GeosysProcessingProvider
                                 A QGIS plugin
 GeosysProcessingProvider
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-03-30
        copyright            : (C) 2019 by Kartoza Pty. Ltd
        email                : rohmat@kartoza.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt5.QtGui import QIcon
from qgis.core import QgsProcessingProvider
from geosys.processing.geosys_processing_algorithm import MapCoverageDownloader
from geosys.utilities.resources import resources_path

__copyright__ = "Copyright 2019, Kartoza"
__license__ = "GPL version 3"
__email__ = "rohmat@kartoza.com"
__revision__ = "$Format:%H$"


class GeosysProcessingProvider(QgsProcessingProvider):

    def __init__(self):
        QgsProcessingProvider.__init__(self)

        # Icon path
        self._icon = resources_path('img', 'icons', 'icon.png')

    def unload(self):
        """
        Unloads the provider. Any tear-down steps required by the provider
        should be implemented here.
        """
        pass

    def loadAlgorithms(self):
        """
        Loads all algorithms belonging to this provider.
        """
        self.addAlgorithm(MapCoverageDownloader())

    def id(self):
        """
        Returns the unique provider id, used for identifying the provider. This
        string should be a unique, short, character only string, eg "qgis" or
        "gdal". This string should not be localised.
        """
        return 'geosys'

    def name(self):
        """
        Returns the provider name, which is used to describe the provider
        within the GUI.

        This string should be short (e.g. "Lastools") and localised.
        """
        return 'GEOSYS'

    def longName(self):
        """
        Returns the a longer version of the provider name, which can include
        extra details such as version numbers. E.g. "Lastools LIDAR tools
        (version 2.2.1)". This string should be localised. The default
        implementation returns the same string as name().
        """
        return self.name()

    def icon(self):
        return QIcon(self._icon)
