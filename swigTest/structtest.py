# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_structtest', [dirname(__file__)])
        except ImportError:
            import _structtest
            return _structtest
        if fp is not None:
            try:
                _mod = imp.load_module('_structtest', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _structtest = swig_import_helper()
    del swig_import_helper
else:
    import _structtest
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _structtest.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _structtest.SwigPyIterator_value(self)
    def incr(self, n = 1): return _structtest.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _structtest.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _structtest.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _structtest.SwigPyIterator_equal(self, *args)
    def copy(self): return _structtest.SwigPyIterator_copy(self)
    def next(self): return _structtest.SwigPyIterator_next(self)
    def __next__(self): return _structtest.SwigPyIterator___next__(self)
    def previous(self): return _structtest.SwigPyIterator_previous(self)
    def advance(self, *args): return _structtest.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _structtest.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _structtest.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _structtest.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _structtest.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _structtest.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _structtest.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _structtest.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class Intvector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Intvector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Intvector, name)
    __repr__ = _swig_repr
    def iterator(self): return _structtest.Intvector_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _structtest.Intvector___nonzero__(self)
    def __bool__(self): return _structtest.Intvector___bool__(self)
    def __len__(self): return _structtest.Intvector___len__(self)
    def pop(self): return _structtest.Intvector_pop(self)
    def __getslice__(self, *args): return _structtest.Intvector___getslice__(self, *args)
    def __setslice__(self, *args): return _structtest.Intvector___setslice__(self, *args)
    def __delslice__(self, *args): return _structtest.Intvector___delslice__(self, *args)
    def __delitem__(self, *args): return _structtest.Intvector___delitem__(self, *args)
    def __getitem__(self, *args): return _structtest.Intvector___getitem__(self, *args)
    def __setitem__(self, *args): return _structtest.Intvector___setitem__(self, *args)
    def append(self, *args): return _structtest.Intvector_append(self, *args)
    def empty(self): return _structtest.Intvector_empty(self)
    def size(self): return _structtest.Intvector_size(self)
    def clear(self): return _structtest.Intvector_clear(self)
    def swap(self, *args): return _structtest.Intvector_swap(self, *args)
    def get_allocator(self): return _structtest.Intvector_get_allocator(self)
    def begin(self): return _structtest.Intvector_begin(self)
    def end(self): return _structtest.Intvector_end(self)
    def rbegin(self): return _structtest.Intvector_rbegin(self)
    def rend(self): return _structtest.Intvector_rend(self)
    def pop_back(self): return _structtest.Intvector_pop_back(self)
    def erase(self, *args): return _structtest.Intvector_erase(self, *args)
    def __init__(self, *args): 
        this = _structtest.new_Intvector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _structtest.Intvector_push_back(self, *args)
    def front(self): return _structtest.Intvector_front(self)
    def back(self): return _structtest.Intvector_back(self)
    def assign(self, *args): return _structtest.Intvector_assign(self, *args)
    def resize(self, *args): return _structtest.Intvector_resize(self, *args)
    def insert(self, *args): return _structtest.Intvector_insert(self, *args)
    def reserve(self, *args): return _structtest.Intvector_reserve(self, *args)
    def capacity(self): return _structtest.Intvector_capacity(self)
    __swig_destroy__ = _structtest.delete_Intvector
    __del__ = lambda self : None;
Intvector_swigregister = _structtest.Intvector_swigregister
Intvector_swigregister(Intvector)

class s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, s, name)
    __repr__ = _swig_repr
    __swig_setmethods__["i"] = _structtest.s_i_set
    __swig_getmethods__["i"] = _structtest.s_i_get
    if _newclass:i = _swig_property(_structtest.s_i_get, _structtest.s_i_set)
    __swig_setmethods__["v"] = _structtest.s_v_set
    __swig_getmethods__["v"] = _structtest.s_v_get
    if _newclass:v = _swig_property(_structtest.s_v_get, _structtest.s_v_set)
    def __init__(self): 
        this = _structtest.new_s()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _structtest.delete_s
    __del__ = lambda self : None;
s_swigregister = _structtest.s_swigregister
s_swigregister(s)


def make_struct():
  return _structtest.make_struct()
make_struct = _structtest.make_struct
# This file is compatible with both classic and new-style classes.


