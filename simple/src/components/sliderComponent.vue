<template>
    <div class="slider-wrapper" @mouseover="clearInv" @mouseout="runInv">
        <!-- 四张图片 -->
        <div class="slider-item item1">1</div>
        <div class="slider-item item2">2</div>
        <div class="slider-item item3">3</div>
        <div class="slider-item item4">4</div>

        <!-- 下方圆点 -->
        <ul class="slider-dots">
            <li>&lt;</li>
            <li></li>
            <li></li>
            <li></li>
            <li></li>
            <li>&gt;</li>
        </ul>
    </div>
</template>

<script>
export default {
    props:{
        inv:{
            type:Number,
            default:1000
        }
    },
    data() {
        return {
            
        }
    },
    methods: {
        runInv(){
            setInterval(()=>{

            },this.inv)
        },
        clearInv(){

        }
    },
}
</script>

<style scoped>

.slider-wrapper{
    width:900px;
    height:500px;
    background:rgb(233, 99, 99);
    position: relative;
}
.slider-item{
    width:900px;
    height:500px;
    text-align: center;
    line-height: 500px;
    font-size: 40px;
    position: absolute;
}
.item1{
    z-index:4;
}
.item1{
    z-index:3;
}
.item1{
    z-index:2;
}
.item1{
    z-index:1;
}

.slider-dots{
    position: absolute;
    right:50px;
    bottom:20px;
}

.slider-dots li{
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background:#726363;
    color: white;
    text-align: center;
    line-height: 20px;
    float: left;
    margin: 0 10px;
    opacity: 0.8;
}


</style>
