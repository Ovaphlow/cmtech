# -*- coding:utf-8 -*-

import sys
import globalvars
import jshdw
import staff
import pgdw
import xmfzr
import zhuanjia
import phase
import phase_log
import phase_a4
import phase_a5
import phase_a6

reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == '__main__':
  print globalvars.get_time(), '开始运行'

  #jshdw.run()

  #staff.run()

  #pgdw.run()

  #xmfzr.run()

  #zhuanjia.run()

  phase.run()

  #phase_log.run()

  #phase_a4.run()

  #phase_a5.run()

  #phase_a6.run()

  print globalvars.get_time(), '所有数据添加完毕'
