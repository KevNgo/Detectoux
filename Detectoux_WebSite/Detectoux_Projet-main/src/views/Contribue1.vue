<template>
  <div class="contribue1">
    <div class="contribue1_étape1">
      <p><b>Etape 1</b></p>
    </div>
    <div class="contribue1_wrapper">
      <div class="contribue1_wrapper_rectangle">
        <div class="contribue1_wrapper_rectangle_form">
          <div class="contribue1_wrapper_rectangle_form_texte">
            <p>
              Pour commencer, veuillez renseigner quelques informations à votre
              sujet :
            </p>
          </div>
          <div class="contribue1_wrapper_rectangle_form_ddn">
            <label for="ddn">Date de naissance :&nbsp;</label>
            <input type="date" id="ddn" required />
          </div>
          <br />
          <div class="contribue1_wrapper_rectangle_form_sexe">
            <label for="sexe">Sexe :&nbsp;</label>
            <select id="sexe" required>
              <option value="">Choix</option>
              <option value="femme">Femme</option>
              <option value="homme">Homme</option>
            </select>
          </div>
          <br />
          <div class="contribue1_wrapper_rectangle_form_test">
            <label for="test">Test au Covid-19 :&nbsp;</label>
            <select id="test" required>
              <option value="">Choix</option>
              <option value="positif">Positif</option>
              <option value="negatif">Négatif</option>
            </select>
          </div>
          <br />
          <div class="contribue1_wrapper_rectangle_form_button">
            <router-link to="/Replay">
              <button>
                <b>Etape suivante</b>
              </button>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
</script>

<style scoped>
.contribue1 {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 90vh;
  width: 100vw;
  flex-direction: column;
}

.contribue1_étape1 {
  width: 25vw;
  height: 7vh;
  background: #f1895c;
  box-shadow: 6px 8px 8px #2e3244;
  font-weight: bold;
  display: flex;
  flex-direction: column;
  margin: 20px;
}

.contribue1_wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50vh;
  width: 90vw;
  margin: 80px;
}

.contribue1_wrapper_rectangle {
  box-shadow: 6px 8px 8px #2e3244;
  background: #c4c4c4;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 60px;
}

.contribue1_wrapper_rectangle_form {
  display: flex;
  align-items: center;
  flex-direction: column;
}

.contribue1_wrapper_rectangle_form_texte {
  display: flex;
  justify-content: center;
  align-items: center;
}

.contribue1_wrapper_rectangle_form_ddn {
  display: flex;
  justify-content: center;
  align-items: center;
}

.contribue1_wrapper_rectangle_form_test {
  display: flex;
  align-items: center;
  justify-content: center;
}

button {
  background: #f1895c;
  margin: 5px;
  height: 6vh;
  width: 50vw;
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
    "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
  color: #2e3244;
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