"""
This class is used to propagate changes to a parent item. This is
used for when an AWeberEntry has a dict item as on of the attributes
in _data.  When changes are made to an item in this data dict, __setattr__
gets called on the parent with the new state of the dict.
"""
class DataDict(dict):

    def __init__(self, data, name, parent):
        super(DataDict, self).__init__(data)
        self.parent = parent
        self.name = name

    def __setitem__(self, key, value):
        super(DataDict, self).__setitem__(key, value)
        self.parent.__setattr__(self.name, self.data)

    #Backwards compatible - do not remove
    @property
    def data(self):
        return self
