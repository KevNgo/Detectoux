
<template>
  <div class="test1">
    <div class="test1_wrapper">
      <div class="test1_wrapper_rectangle">
        <div class="test1_wrapper_rectangle_form">
          <div class="test1_wrapper_rectangle_form_texte">
            <p>
              Pour commencer, veuillez renseigner quelques informations à votre
              sujet :
            </p>
          </div>
          <div class="test1_wrapper_rectangle_form_fum">
            <label for="fum">Fumeur :&nbsp;</label>
            <select id="fum" v-model.trim="modeldata.smoker" v-model="smoker" required>
              <!-- <option value="">- Choix -</option> -->
              <option value="oui">Oui</option>
              <option value="non">Non</option>
            </select>
          </div>
          <br />
          <div class="test1_wrapper_rectangle_form_ant">
            <label for="med">Antécedents médicaux :&nbsp;</label>
            <select id="med" v-model.trim="modeldata.medhist" v-model="medhist" required>
              <!-- <option value="">- Choix -</option> -->
              <option value="diabete">Diabète avec complications</option>
              <option value="asthme">
                Asthme ou maladie pulmonaire chronique
              </option>
              <option value="ins-card">
                Insuffisance cardiaque congestive
              </option>
              <option value="aucun">Aucun</option>
            </select>
          </div>
          <br />
          <div class="test1_wrapper_rectangle_form_sympt">
            <label for="symp">Symptômes :&nbsp;</label>
            <select id="symp" v-model.trim="modeldata.symp" v-model="symp" required>
              <!-- <option value="">- Choix -</option> -->
              <option value="toux">Toux nouvelle ou aggravée</option>
              <option value="mdg">Mal de gorge</option>
              <option value="ess">Essoufflement</option>
              <option value="ess_mdg_mdc">
                Essoufflement, mal de gorge, maux de corps
              </option>
              <option value="ess_toux">
                Essoufflement, toux nouvelle ou aggravée
              </option>
              <option value="mdg_pdg_pdo">
                Mal de gorge, perte du goût, perte de l'odorat
              </option>
              <option value="fvr_fr_toux_mdg">
                Fièvre, frissons ou sueurs, toux nouvelle ou aggravée, mal de
                gorge
              </option>
              <option value="fvr_fr_ess_toux_mdg_pdg_pdo">
                Fièvre, frissons ou sueurs, essoufflement, toux nouvelle ou
                aggravée, mal de gorge, perte de goût, perte d'odorat
              </option>
              <option value="aucun">Aucun</option>
            </select>
          </div>
          <p>
            Ensuite, appuyez sur le bouton <b>Enregistrer </b>, vous aurez alors
            1 seconde pour enregistrer votre toux. L'enregistrement s'arrêtera
            automatiquement, vous pourrez alors cliquer sur le bouton<b>
              Accéder au diagnostic</b
            >. Attention, vous ne pourrez garder qu'un seul enregistrement.
          </p>
          <div class="test1_wrapper_rectangle_form_audio">
            <canvas class="visualizer" height="60px"></canvas>

            <button id="record" @click="record()">Enregistrer</button>

            <section id="sound_clips"></section>
            <div class="replay_choix">
              <div class="replay_choix_button">
                <button @click="predict()">
                  <b>Accéder au diagnostic</b>
                </button>
              </div>
            </div>
            <br />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: "Test1",
    components: {},
    data() {
      return {
        modeldata: {
                smoker: null,
                medhist: null,
                symp: null,
                audio: null,
                maxmfcc:null,
                stdmfcc: null,
                maxmagspec: null,
                meanmagspec: null,
                maxfreqmagspec: null,
                maxfreqreg: null,
                maxfreqfft: null
            },
        APIResult : []
      }
    },
    mounted() {
      console.log(navigator)
    },
    methods: {
      //Function to use the microphone and record sound
      record() {
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
          navigator.mediaDevices.getUserMedia({
            audio: true
          })

            // Success callback
            .then(stream => {
              let mediaRecorder = new MediaRecorder(stream);
              mediaRecorder.start();
              console.log(mediaRecorder.state);
              console.log("recorder started");
              record.style.background = "red";
              record.style.color = "black";
              let chuck = []

              mediaRecorder.addEventListener("dataavailable", e => {
                chuck.push(e.data)
              })

              mediaRecorder.addEventListener("stop", e => {
                console.log("recorder stopped");
                const clipContainer = document.createElement('article');
                const deleteButton = document.createElement('button');

                clipContainer.classList.add('clip');
                let blob = new Blob(chuck, {
                  'type': 'audio/mpeg-3;'
                })
                let audio_url = URL.createObjectURL(blob)
                this.modeldata.audio = new Audio(audio_url)

                this.modeldata.audio.setAttribute("controls", 1)

                console.log(this.modeldata.audio.src)
                deleteButton.innerHTML = "Supprimer";

                clipContainer.appendChild(this.modeldata.audio);
                clipContainer.appendChild(deleteButton);
                sound_clips.appendChild(clipContainer);
                console.log(this.donnee)
                deleteButton.onclick = function (e) {
                  let evtTgt = e.target;
                  evtTgt.parentNode.parentNode.removeChild(evtTgt.parentNode);
                }
              })
              setTimeout(() => {
                mediaRecorder.stop();
              }, 2000);
            })
            // Error callback
            .catch(function (err) {
              console.log('The following getUserMedia error occurred: ' + err);
            });
        }
      },
      
      mp3Build() {
        try {
            var process = new ffmpeg('sound.data');
            process.then(function (audio) {
                // Callback mode.
                audio.fnExtractSoundToMP3('sound.mp3', function (error, file) {
                    if (!error) {
                        console.log('Audio file: ' + file);
                //audioDownload.href = player.src;
                audioDownload.href = player.srcObject;
                audioDownload.download = 'sound.mp3';
                audioDownload.innerHTML = 'Download';
              } else {
                console.log('Error-fnExtractSoundToMP3: ' + error);
              }
                });
            }, function (err) {
                console.log('Error: ' + err);
            });
        } catch (e) {
            console.log(e.code);
            console.log(e.msg);
        }
      },

      //prediction of Covid
      async predict(){
        const prediction = await axios.get('http://127.0.0.1:5000/model', {
          params:{
            smoker: this.modeldata.smoker,
            medhist: this.modeldata.medhist,
            symp: this.modeldata.symp,
            maxmfcc:this.modeldata.maxmfcc,
            stdmfcc: this.modeldata.stdmfcc,
            maxmagspec: this.modeldata.maxmagspec,
            meanmagspec: this.modeldata.meanmagspec,
            maxfreqmagspec: this.modeldata.maxfreqmagspec,
            maxfreqreg: this.modeldata.maxfreqreg,
            maxfreqfft: this.modeldata.maxfreqfft
          }
        })
        prediction = prediction.data
        console.log(prediction)

        /* console.log("Recieved data successfully");
        this.modeldata.APIResult = response.data;
        console.log(response.data);
        if (this.modeldata.APIResult==1) this.$router.push('/Test3_1')
        else this.$router.push('/Test3_2') */
      },
      async sigTreat() {
        const res = await axios.get('http://127.0.0.1:5000/signal', {
          params:{
            audio: this.modeldata.audio
          }
        })
        res = res.data
        console.log(res)
      }
    },
    computed:{
      donnee:function(){
        //change string value to numeric value for model interpretation
        //medical history to num
        switch(this.modeldata.medhist){
          case "diabete":
            this.modeldata.medhist=1;
            break;
          case 'asthme':
            this.modeldata.medhist=2
            break;
          case 'ins-card':
            this.modeldata.medhist=3;
            break;
          default:
            this.modeldata.medhist=0;
            break;
        }
        //Smoker to num
        switch(this.modeldata.smoker){
          case "oui":
            this.modeldata.smoker=1;
            break;
          default:
            this.modeldata.smoker=0;
            break;
        }
        //Symptom to num
        switch(this.modeldata.symp){
          case 'toux':
            this.modeldata.symp=1;
            break;
          case 'mdg':
            this.modeldata.symp=2;
            break;
          case 'ess':
            this.modeldata.symp=3;
            break;
          case 'ess_mdg_mdc':
            this.modeldata.symp=4;
            break;
          case 'ess_toux':
            this.modeldata.symp=5;
            break;
          case 'mdg_pdg_pdo':
            this.modeldata.symp=6;
            break;
          case 'fvr_fr_toux_mdg':
            this.modeldata.symp=7;
            break;
          case 'fvr_fr_toux_mdg_pdg_pdo':
            this.modeldata.symp=8;
            break;
          default:
            this.modeldata.symp=0;
            break;
        }

        /*
        getAPI
          .get("/signal",{
            params:{
              audio : this.modeldata.audio,
            }
          })
          .then(response =>{
            console.log("Received audio successfully")
            this.modeldata.maxmfcc, this.modeldata.stdmfcc, this.modeldata.maxmagspec, this.modeldata.meanmagspec, this.modeldata.maxfreqmagspec, this.modeldata.maxfreqreg, this.modeldata.maxfreqfft=response.data
            console.log(response.data)
          })
          .catch(err=>{
                    console.log(err);
                });*/


        return [this.modeldata.smoker,this.modeldata.medhist,this.modeldata.symp,this.modeldata.maxmfcc, this.modeldata.stdmfcc, this.modeldata.maxmagspec, this.modeldata.meanmagspec, this.modeldata.maxfreqmagspec, this.modeldata.maxfreqreg, this.modeldata.maxfreqfft]
      },
      modeldataaudio:function() {
        return this.modeldata.audio
      }      
    },
    watch: {
      modeldataaudio: function () {
        console.log('wassup')
        if(this.modeldata.audio) this.sigTreat()
      }
    }
  }
</script>

<style scoped>

.test1 {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
  width: 100vw;
  flex-direction: column;
  /* margin: 20px; */
}

.test1_étape1 {
  width: 25vw;
  height: 7vh;
  background: #f1895c;
  box-shadow: 6px 8px 8px #2e3244;
  font-weight: bold;
  display: flex;
  flex-direction: column;
  margin: 20px;
}
.test1_wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50vh;
  width: 90vw;
  margin: 50px;
}
.test1_wrapper_rectangle {
  box-shadow: 6px 8px 8px #2e3244;
  background: #c4c4c4;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px;
}
.test1_wrapper_rectangle_form {
  display: flex;
  align-items: center;
  flex-direction: column;
}
.test1_wrapper_rectangle_form_texte {
  display: flex;
  justify-content: center;
  align-items: center;
}
.test1_wrapper_rectangle_form_fum {
  display: flex;
  justify-content: center;
  align-items: center;
}
.test1_wrapper_rectangle_form_ant {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row;
}
.test1_wrapper_rectangle_form_sympt {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row;
}
.test1_wrapper_rectangle_form_audio {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

button {
  background: #f1895c;
  margin: 5px;
  height: 6vh;
  width: 50vw;
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
    "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
  color: #2e3244;
  margin: 10px;
}
button:hover,
button:focus {
  height: 6vh;
  width: 51vw;
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
html,
body {
  height: 100%;
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 0.8rem;
}
.wrapper {
  height: 100%;
  display: flex;
  flex-direction: column;
}
h1,
h2 {
  font-size: 2rem;
  text-align: center;
  font-weight: normal;
  padding: 0.5rem 0 0 0;
}
/* Make the clips use as much space as possible, and
 * also show a scrollbar when there are too many clips to show
 * in the available space */
.sound-clips {
  flex: 1;
  overflow: auto;
}
/*
section, article {
  display: block;
}*/
.clip {
  padding-bottom: 1rem;
}
audio {
  width: 100%;
  display: block;
  margin: 1rem auto 0.5rem;
}
.clip p {
  display: inline-block;
  font-size: 1rem;
}
.clip button {
  font-size: 1rem;
  float: right;
}
button.delete {
  background: #f00;
  padding: 0.5rem 0.75rem;
  font-size: 0.8rem;
}
input[type="checkbox"] {
  position: absolute;
  top: -100px;
}
aside {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  transform: translateX(100%);
  transition: 0.3s all ease-out;
  background-color: #efefef;
  padding: 1rem;
}
/* Toggled State of information box */
input[type="checkbox"]:checked ~ aside {
  transform: translateX(0);
}
/* Cursor when clip name is clicked over */
.clip p {
  cursor: pointer;
}
/* Adjustments for wider screens */
@media all and (min-width: 800px) {
  /* Don't take all the space as readability is lost when line length
     goes past a certain size */
  .wrapper {
    width: 90%;
    max-width: 1000px;
    margin: 0 auto;
  }
}
</style>