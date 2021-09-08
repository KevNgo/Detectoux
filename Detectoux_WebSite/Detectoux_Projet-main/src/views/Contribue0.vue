<template>
  <div class="contribue0">
    <div class="contribue0_rectangle">
      <div class="contribue0_rectangle_p">
        <p>J’accepte de partager mes données avec l’équipe Detectoux</p>
      </div>
      <div class="contribue0_rectangle_button">
        <router-link to="/Contribue1">
          <button></button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
</script>

<style scoped>
.contribue0 {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
  width: 100vw;
  flex-direction: row;
}

.contribue0_rectangle {
  width: 60vw;
  height: 30vh;
  box-shadow: 6px 8px 8px #2e3244;
  background: #f1895c;
  display: flex;
  flex-direction: column;
}

.contribue0_rectangle_p {
  margin: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.contribue0_rectangle_button {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 10px;
}

button {
  width: 21px;
  height: 21px;
  background: #ffffff;
}

p {
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
    "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
  font-style: normal;
  font-weight: normal;
  float: left;
  color: #2e3244;
  text-align: center;
  align-items: center;
  justify-content: center;
}
</style>