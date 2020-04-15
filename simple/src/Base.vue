<template>
  <div>
    <div class="app-head">
      <div class="app-head-inner">
        <img src="./assets/logo.png" alt="">
        <div class="head-nav">
          <ul class="nav-list">
            <li>登录</li>
            <li class="nav-pile">|</li>
            <li>注册</li>
            <li class="nav-pile">|</li>
            <li>关于</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="app-content">
      <router-view></router-view>
    </div>
    <div class="app-footer">
      <p> &copy; 1903c —— 2020 </p>
    </div>
  </div>
</template>

<script>
export default {
  
}
</script>

<style scoped>
/* reset重置样式 */
html,body,h1,h2,h3,h4,h5,h6,div,dl,dt,dd,ul,ol,li,p,blockquote,pre,hr,figure,table,caption,th,td,form,fieldset,legend,input,button,textarea,menu{margin:0;padding:0;}
header,footer,section,article,aside,nav,hgroup,address,figure,figcaption,menu,details{display:block;}
table{border-collapse:collapse;border-spacing:0;}
caption,th{text-align:left;font-weight:normal;}
html,body,fieldset,img,iframe,abbr{border:0;}
i,cite,em,var,address,dfn{font-style:normal;}
[hidefocus],summary{outline:0;}
li{list-style:none;}
h1,h2,h3,h4,h5,h6,small{font-size:100%;}
sup,sub{font-size:83%;}
pre,code,kbd,samp{font-family:inherit;}
q:before,q:after{content:none;}
textarea{overflow:auto;resize:none;}
label,summary{cursor:default;}
a,button{cursor:pointer;}
h1,h2,h3,h4,h5,h6,em,strong,b{font-weight:bold;}
del,ins,u,s,a,a:hover{text-decoration:none;}
body,textarea,input,button,select,keygen,legend{font:12px/1.14 arial,\5b8b\4f53;color:#333;outline:0;}
body{background:#fff;}
a,a:hover{color:#333;}

/* Base样式 */
.app-head{
  background: #363636;
  color:white;
  height:90px;
  line-height: 90px;
  width: 100%;
}
.app-head-inner{
  width: 1200px;
  margin: 0 auto;
}
.app-head-inner img{
  float: left;
  width: 50px;
  margin-top: 20px;
}
.head-nav{
  float: right;
}
.head-nav li {
  float: left;
  cursor: pointer;
}
.nav-pile{
  padding: 0 10px;
}

.app-footer{
  text-align: center;
  height: 80px;
  line-height: 80px;
  width: 100%;
  background: #e3e4e8;
  margin-top:30;
}
.app-content{
  width: 1200px;
  margin: 0 auto;
}

</style>>



</style>
