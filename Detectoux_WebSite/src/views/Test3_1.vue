<template>
  <div class="test">
    <div class="test_resultats">
      <p><b>Résultats</b></p>
    </div>
    <div class="test_wrapper">
      <div class="test_wrapper_analyse">
        <div class="test_wrapper_analyse_texte">
          <p>
            Après analyse de votre toux, vous
            êtes<strong>&nbsp;négatif&nbsp;</strong>au Covid-19.
          </p>
        </div>
      </div>
    </div>
    <div class="test_message">
      <p>
        Nous rappelons qu’il est important de continuer à
        <b> &nbsp;respecter les gestes barrières&nbsp; </b>
        !
      </p>
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
.test {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 75vh;
  width: 100vw;
  flex-direction: column;
}

.test_resultats {
  width: 25vw;
  height: 7vh;
  background: #f1895c;
  box-shadow: 6px 8px 8px #2e3244;
  font-weight: bold;
  display: flex;
  flex-direction: column;
  margin: 15px;
}

.test_wrapper_analyse {
  width: 90vw;
  height: 20vh;
  background: #c4c4c4;
  box-shadow: 6px 8px 8px #2e3244;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin: 10px;
}

.test_wrapper_analyse_texte {
  padding: 0px;
}

.test_message {
  width: 90vw;
  height: 20vh;
  background: #c4c4c4;
  box-shadow: 6px 8px 8px #2e3244;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin: 20px;

  border-color: #f1895c;
  border-style: solid;
}

p {
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
    "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
  font-style: normal;
  text-align: center;
  color: #2e3244;
  font-weight: normal;
  align-items: center;
  justify-content: center;
}

button {
  background: #f1895c;
  margin: 10px;
  height: 6vh;
  width: 30vw;
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
    "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
  color: #2e3244;
  box-shadow: 6px 8px 8px #2e3244;
}

button:hover,
button:focus {
  height: 6vh;
  width: 51vw;
}
</style>