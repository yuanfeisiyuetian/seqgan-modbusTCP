# -*- coding: utf_8 -*-
import sys
import logging
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import random
logger = modbus_tk.utils.create_logger("console")
if __name__ == "__main__":
    try:

        # 连接MODBUS TCP从机
        master = modbus_tcp.TcpMaster(host="127.0.0.1")
        master.set_timeout(5.0)
        logger.info("connected")

        # 读保持寄存器03
        # logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 127))

        for start in range(0, 126):
            for quatity in range(1, 126 - start):
                logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, start, quatity))
        '''
        # 读输入寄存器04
        logger.info(master.execute(1, cst.READ_INPUT_REGISTERS, 0, 125))

        for start in range(0, 125):
            for quatity in range(1, 125 - start):
                logger.info(master.execute(1, cst.READ_INPUT_REGISTERS, start, quatity))
        
        # 读线圈寄存器01
        logger.info(master.execute(1, cst.READ_COILS, 0, 256))

        for start in range(0, 256):
            for quatity in range(1, 256 - start):
                logger.info(master.execute(1, cst.READ_COILS, start, quatity))

        
        # 读离散输入寄存器02
        logger.info(master.execute(1, cst.READ_DISCRETE_INPUTS, 0, 256))

        for start in range(0, 256):
            for quatity in range(1, 256 - start):
                logger.info(master.execute(1, cst.READ_DISCRETE_INPUTS, start, quatity))
       
        # 单个读写寄存器操作
        # 写寄存器地址为0的保持寄存器06
        logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, 125, output_value=-32768))
        #logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 10))
        for addr in range(0, 125):
            for i in range(0, 100):
                value = random.randint(-32768, 65535)
                logger.info(master.execute(1, cst.WRITE_SINGLE_REGISTER, addr, output_value=value))
        
        # 写寄存器地址为0的线圈寄存器，写入内容为0（位操作）05
        logger.info(master.execute(1, cst.WRITE_SINGLE_COIL, 255, output_value=0))
        #logger.info(master.execute(1, cst.READ_COILS, 0, 1))
        for addr in range(0, 255):
            for i in range(0, 40):
                value = random.randint(0, 1)
                logger.info(master.execute(1, cst.WRITE_SINGLE_COIL, addr, output_value=value))
        '''
        # 多个寄存器读写操作(这两个应该只涉及数据大小的问题，但是怎么构造数据呢，这可以有很多种,这个数据报长度一下就变了)
        # 写寄存器起始地址为0的保持寄存器，操作寄存器个数为4 16
        logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0, output_value=[20,21,22,23]))
        logger.info(master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 4))
        '''
        # 写寄存器起始地址为0的线圈寄存器 15
        logger.info(master.execute(1, cst.WRITE_MULTIPLE_COILS, 0, output_value=[0,0,0,1,1,0,1,1]))
        logger.info(master.execute(1, cst.READ_COILS, 0, 8))
        '''



    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))