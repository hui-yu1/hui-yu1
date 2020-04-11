<template>
  <div id="app">
    <h2>购物清单</h2>
    <!-- 添加购物车 -->
    <div class="input-group">
      <input type="text" class="js-new-item form-control" placeholder="输入你要购买的物品" />
      <span>
        <button class="js-add btn btn-default">添加到购物车</button>
      </span>
    </div>
    <!-- 购物车列表 -->
    <ul>
      <li>
        <div class="checkbox">
          <label for>
            <input class="js-item" type="checkbox" />妮寇
          </label>
        </div>
      </li>
      <li>
        <div class="checkbox">
          <label for>
            <input class="js-item" type="checkbox" />铲子
          </label>
        </div>
      </li>
      <li>
        <div class="checkbox">
          <label for>
            <input class="js-item" type="checkbox" />大剑
          </label>
        </div>
      </li>
    </ul>
    <!-- 修改标题 -->
    <div class="footer">
      <hr />
      <span>修改标题</span>
      <input type="text" class="js-change-title" value="购物清单" />
    </div>
  </div>
</template>

<script>

</script>

<style>
#app {
  width: 50%;
  margin: 7% auto;
}
.removed {
  color: gray;
}
.removed label {
  text-decoration: line-through;
}
ul {
  border: 1px solid black;
  margin-top: 30px;
}
ul li {
  list-style: none;
}
</style>
