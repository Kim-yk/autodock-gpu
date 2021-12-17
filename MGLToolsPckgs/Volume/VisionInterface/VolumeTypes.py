########################################################################
#
# Date: April 2006 Authors: Guillaume Vareille, Michel Sanner
#
#    sanner@scripps.edu
#    vareille@scripps.edu
#
#       The Scripps Research Institute (TSRI)
#       Molecular Graphics Lab
#       La Jolla, CA 92037, USA
#
# Copyright: Guillaume Vareille, Michel Sanner and TSRI
#
# revision:
#
#########################################################################
#
# $Header: /mnt/raid/services/cvs/Volume/VisionInterface/VolumeTypes.py,v 1.3 2006/04/12 23:20:36 vareille Exp $
#
# $Id: VolumeTypes.py,v 1.3 2006/04/12 23:20:36 vareille Exp $
#

from NetworkEditor.datatypes import AnyType


class Grid3DType(AnyType):
    def __init__(self):
        AnyType.__init__(self)
        self.data['name'] = 'Grid3D'
        self.data['color'] = '#995699'
        self.data['shape'] = 'diamond'
        from Volume.Grid3D import Grid3D
        self.data['class'] = Grid3D

    def validate(self, data):
        from Volume.Grid3D import Grid3D
        return isinstance(data, Grid3D)

    def cast(self, data):
        return False, data
    

class Grid3DDType(AnyType):
    def __init__(self):
        AnyType.__init__(self)
        self.data['name'] = 'Grid3DD'
        self.data['color'] = 'magenta'
        self.data['shape'] = 'diamond'
        from Volume.Grid3D import Grid3DD
        self.data['class'] = Grid3DD

    def validate(self, data):
        from Volume.Grid3D import Grid3DD
        return isinstance(data, Grid3DD)

    def cast(self, data):
        return False, data


class Grid3DFType(AnyType):
    def __init__(self):
        AnyType.__init__(self)
        self.data['name'] = 'Grid3DF'
        self.data['color'] = 'green'
        self.data['shape'] = 'diamond'
        from Volume.Grid3D import Grid3DF
        self.data['class'] = Grid3DF

    def validate(self, data):
        from Volume.Grid3D import Grid3DF
        return isinstance(data, Grid3DF)

    def cast(self, data):
        return False, data
    
    
class Grid3DIType(AnyType):
    def __init__(self):
        AnyType.__init__(self)
        self.data['name'] = 'Grid3DI'
        self.data['color'] = 'yellow'
        self.data['shape'] = 'diamond'
        from Volume.Grid3D import Grid3DI
        self.data['class'] = Grid3DI

    def validate(self, data):
        from Volume.Grid3D import Grid3DI
        return isinstance(data, Grid3DI)

    def cast(self, data):
        return False, data
    

class Grid3DSIType(AnyType):
    def __init__(self):
        AnyType.__init__(self)
        self.data['name'] = 'Grid3DSI'
        self.data['color'] = 'yellow'
        self.data['shape'] = 'diamond'
        from Volume.Grid3D import Grid3DSI
        self.data['class'] = Grid3DSI

    def validate(self, data):
        from Volume.Grid3D import Grid3DSI
        return isinstance(data, Grid3DSI)

    def cast(self, data):
        return False, data
    
    
class Grid3DUIType(AnyType):
    def __init__(self):
        AnyType.__init__(self)
        self.data['name'] = 'Grid3DUI'
        self.data['color'] = 'yellow'
        self.data['shape'] = 'diamond'
        from Volume.Grid3D import Grid3DUI
        self.data['class'] = Grid3DUI

    def validate(self, data):
        from Volume.Grid3D import Grid3DUI
        return isinstance(data, Grid3DUI)

    def cast(self, data):
        return False, data
    

class Grid3DUSIType(AnyType):
    def __init__(self):
        AnyType.__init__(self)
        self.data['name'] = 'Grid3DUSI'
        self.data['color'] = 'yellow'
        self.data['shape'] = 'diamond'
        from Volume.Grid3D import Grid3DUSI
        self.data['class'] = Grid3DUSI

    def validate(self, data):
        from Volume.Grid3D import Grid3DUSI
        return isinstance(data, Grid3DUSI)

    def cast(self, data):
        return False, data
    
    
class Grid3DUCType(AnyType):
    def __init__(self):
        AnyType.__init__(self)
        self.data['name'] = 'Grid3DUC'
        self.data['color'] = 'cyan'
        self.data['shape'] = 'diamond'
        from Volume.Grid3D import Grid3DUC
        self.data['class'] = Grid3DUC

    def validate(self, data):
        from Volume.Grid3D import Grid3DUC
        return isinstance(data, Grid3DUC)

    def cast(self, data):
        return False, data
