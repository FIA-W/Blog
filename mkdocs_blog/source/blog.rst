=============================
UVM 学习笔记
=============================


第一章 config_db 
--------------------
1.1 简介
-----------------

用途：全局变量的方式，进行数据传输?
          1.底层组件可以通过层次或类型来获取高层次的配置信息
          2.传递接口信息?
 
config_db知识思维导图

后台操作
set()通过层次和变量名，将这些信息存放到uvm_pkg唯一的全局变量uvm_pkg::uvm_resources

Code Example
============

Here is a Python code example:

.. code-block:: python

   def hello_world():
       print("Hello, World!")

1.2 传递参数
-----------------
set函数范式uvm_config_db #(传输数据类型)：：set(发送源地址，“相对于发送源的接收方地址”， “传输数据名称”，传输数据内容）；set:自顶向下set，如从top_tb向下driver设置参数,即在top_tb中进行set。
