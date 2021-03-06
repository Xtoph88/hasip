from lib.base.modules import *

class Cmddemo(Basemodule, Switch):

  # ################################################################################
  # initialization of module and optional load of config files
  # ################################################################################
  def __init__(self, instance_queue, global_queue):
    #
    # "cmddemo|port|command or action"
    #
    self.queue_identifier = 'cmddemo'     # this is the 'module address'  
    self.instance_queue = instance_queue  # worker queue to receive jobs 
    self.global_queue = global_queue      # queue to communicate back to main thread
    self.ports = [                        # internal port names
      { 
        'id'      : 0,
        'type'    : 'switch',
        'status'  : 'on'
      }, { 
        'id'      : 1,
        'type'    : 'switch',
        'status'  : 'unknown'
      }, {}, {}, {} ] # defining internal ports here (...)


  # ################################################################################
  # main thread of this module file which runs in background and constanly
  # checks working queue for new tasks. 
  # ################################################################################
  def worker(self):
    while True:
      instance_queue_element = self.instance_queue.get(True)

      _senderport = instance_queue_element.get("module_from_port")
      _sender	  = instance_queue_element.get("module_from")
      _port       = instance_queue_element.get("module_addr")
      _action     = instance_queue_element.get("cmd")
      _optargs    = instance_queue_element.get("opt_args")

      options = {
        "get_status"    : self.get_status,
        "set_on"        : self.set_on,
        "set_off"       : self.set_off
      }
      options[_action](_sender, _senderport, _port, _optargs)

  # ################################################################################
  #
  # "private" methods from here on...
  #
  # ################################################################################

  # ################################################################################
  # shows status of port provided by argument
  #
  # @arguments:  port
  # @return:     -
  # ################################################################################
  def get_status(self, sender, senderport, port, optargs):
     #print "Cmddemo :: status(" + str(port) + ") => " + self.ports[port]['status']
     pass

  # ################################################################################
  # sets the port provided by @argument to on
  #
  # @arguments:  port
  # @return:     -
  # ################################################################################
  def set_on(self, sender, senderport, port, optargs):
    self.ports[port]['status'] = 'on'
    print "Cmddemo :: set_on(" + str(port) + ")"

  # ################################################################################
  # sets the port provided by @agrument to off
  #
  # @arguments:  port
  # @return:     -
  # ################################################################################
  def set_off(self, sender, senderport, port, optargs):
    self.ports[port]['status'] = 'on'
    print "Cmddemo :: set_off(" + str(port) + ")"
