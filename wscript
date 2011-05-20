import Options, Utils
from os import unlink, symlink, chdir
from os.path import exists

srcdir = '.'
blddir = 'build'
VERSION = '0.0.2'

def set_options(opt):
  opt.tool_options('compiler_cxx')

def configure(conf):
  conf.check_tool('compiler_cxx')
  conf.check_tool('node_addon')

  conf.env.append_unique('CPPFLAGS', ["-I/usr/local/include -g"])
  conf.env.append_unique('CXXFLAGS', ["-Wall -g"])

  conf.env.append_unique('LINKFLAGS', ["-L/usr/local/lib"])


def build(bld):
  obj = bld.new_task_gen('cxx', 'shlib', 'node_addon')
  obj.target = 'radius-ng'
  obj.source = './src/radius-ng.cc'
  obj.lib = ['radiusclient-ng']

#def shutdown():
  # HACK to get bindings.node out of build directory.
  # better way to do this?
  #t = 'ldapsearch.node'
  #symlink('build/default/' + t, t)

