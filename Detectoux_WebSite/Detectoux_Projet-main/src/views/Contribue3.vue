<template>
  <div class="contribue3">
    <div class="contribue3_rectangle">
      <p>Nous vous remercions de votre contribution !</p>
    </div>
    <div class="test_button">
      <router-link to="/">
        <button>
          <b>Accueil</b>
        </button>
      </router-link>
    </div>
  </div>
</template>

<script>
</script>

<style scoped>
.contribue3 {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 90vh;
  width: 100vw;
  flex-direction: column;
}

.contribue3_rectangle {
  height: 30vh;
  width: 90vw;
  margin: 30px;
  box-shadow: 6px 8px 8px #2e3244;
  background: #c4c4c4;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
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

button {
  background: #f1895c;
  margin: 50px;
  height: 6vh;
  width: 30vw;
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
    "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
  color: #2e3244;
  box-shadow: 6px 8px 8px #2e3244;
}
</style>