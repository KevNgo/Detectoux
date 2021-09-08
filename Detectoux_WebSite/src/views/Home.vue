<template>
  <div class="home">
    <div class="home_"></div>
    <div class="home_wrapper">
      <div class="home_wrapper_rectangle">
        <p>
          Bienvenue sur<b> Detectoux</b> ! <br /><br />
          En quelques étapes, obtenez un diagnostic rapide sur la présence de
          la<b> Covid-19</b>.<br /><br />
          <!-- Si vous possédez un test Covid-19, qu’il soit positif ou négatif, vous
          pouvez nous aider à améliorer le diagnostic en contribuant à notre
          base de données. -->
        </p>
      </div>
    </div>
    <div class="home_choix">
      <div class="home_choix_button">
        <router-link to="/Test1">
          <button>
            <b>Je me teste</b>
          </button>
        </router-link>
      </div>
      <!-- <div class="home_choix_button">
        <router-link to="/Contribue0">
          <button><b>Je contribue</b></button>
        </router-link>
      </div> -->
    </div>
  </div>
</template>

<script>
</script>

<style scoped>
.home {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
  width: 100vw;
  flex-direction: column;
}

.home_ {
  margin: 10px;
}

.home_wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 40vh;
  width: 90vw;
}

.home_wrapper_rectangle {
  box-shadow: 6px 8px 8px #2e3244;
  background: #c4c4c4;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 30px;
  width: 90vw;
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
  box-shadow: 6px 8px 8px #2e3244;
  background: #f1895c;
  margin: 10px;
  height: 6vh;
  width: 50vw;
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
    "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
  color: #2e3244;
}

button:hover,
button:focus {
  height: 6vh;
  width: 51vw;
}

.home_choix {
  margin: 70px;
}
</style>