## 一、什么是前端？前端都包括哪些内容

#### 1. 前端历史

2014之前：HTML，CSS，JavaScript，jQuery（2006，JavaScript函数库），Bootstrap(UI)

2014年—2016年：NodeJS，Angular（谷歌），React（Facebook），Vue（华人，尤雨溪）

2017年之后：小程序等等

#### 2.前端代码体验

使用HTMl构建页面结构

使用CSS修饰页面的效果

使用JavaScript实现动态效果：

2.1 获取HTML元素

2.2 添加事件改变元素内容或样式

#### 3. VSCode前端环境配置

3.1 安装Beautify，它用来格式化代码

3.2 安装open in browser  右键选中可以直接在浏览器中查看页面效果

3.3 HTML Snippets 代码自动填充

3.4 Vetur  支持Vue 

3.5 Live server 浏览器实时更新

## 二、动手写一个购物车效果

#### 1. HTML，CSS，JavaScript，jQuery，Bootstrap

引入库：https://www.bootcdn.cn/

#### 2. 非工程化方式的Vue

v-model 双向数据绑定

v-for 循环遍历，渲染列表项

v-bind 绑定数据和元素属性

v-on  事件绑定

## 三、动手写一个TODOList应用

设置一个倒计时，比如说初始时间是25分钟，进入work（工作）状态，25分钟到点后就是一个5分钟的rest（休息）状态，如此反复



## 四、Vue2.X工程化环境搭建

1. 下载nodejs：https://nodejs.org/en/，npm包管理工具

   检查是否已经安装，cmd中输入node -v检查node ，npm -v 检查npm

2. 用管理员身份打开cmd或者cmder或者gitbash：运行npm install -g vue-cli，vue-cli是vue的脚手架工具  ，Mac Terminal中增强权限sudo

   如果之前安装过，可以先卸载 vue-cli：npm uninstall -g vue-cli

   输入vue --version检查是否安装成功

3. 初始化项目  vue init webpack practise

   进入到项目中  cd practise

   运行项目  npm run dev

   

4. 启动单元测试：npm run unit

5. 启动端对端测试e2e：npm run e2e，先搁置





















