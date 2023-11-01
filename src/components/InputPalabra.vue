<template>
  <div>
    <b-container class="w-100">
      <b-row>
        <label style="font-weight: bold">ingrese su palabra:</label>
      </b-row>
      <b-row class="mb-1">
        <b-form-input
          id="input-live"
          v-model="inputString"
          :state="inputString != '' ? true : false"
          aria-describedby="input-live-help input-live-feedback"
          placeholder="Enter your word"
          trim
        ></b-form-input>
      </b-row>
      <b-row class="mb-1">
        <b-button @click="validateWorld" variant="success">verificar</b-button>
      </b-row>
      <b-row>
        <b-alert
          :show="dismissCountDown"
          dismissible
          :variant="worldValidate ? 'success' : 'danger'"
          @dismissed="dismissCountDown = 0"
          @dismiss-count-down="countDownChanged"
        >
          <h3>
            {{ worldValidate ? "es palindromo es " : "no es palindromo" }}
          </h3>
          <P>{{ dismissCountDown }} seconds...</P>
        </b-alert>
      </b-row>

      <b-row>
        <stack-components :items="stack"></stack-components>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import { Stack } from "@/assets/stack.js";
import stackComponents from "@/components/Stack.vue";
export default {
  components: {
    stackComponents,
  },
  data() {
    return {
      dismissSecs: 3,
      dismissCountDown: 0,
      inputString: "",
      stack: new Stack(),
      worldValidate: "",
    };
  },
  methods: {
    validateWorld() {
      if (this.inputString == "") {
        return;
      }
      // Crear una pila vacía
      this.stack.clear();

      // Procesar la mitad izquierda de la cadena y empujarla a la pila
      let halfLength = Math.floor(this.inputString.length / 2);
      for (let i = 0; i < halfLength; i++) {
        this.stack.pushState(0);
        this.stack.push(this.inputString[i]);
      }

      // Verificar si la longitud de la cadena es impar
      if (this.inputString.length % 2 === 1) {
        halfLength++;
      }

      // Comparar la segunda mitad de la cadena con la pila
      for (let i = halfLength; i < this.inputString.length; i++) {
        this.stack.pushState(1);
        if (this.stack.isEmpty() || this.inputString[i] !== this.stack.pop()) {
          this.worldValidate = false;
          this.recorrido();
          return;
        }
      }

      this.stack.pushState(2);
      this.worldValidate = true;
     
      this.recorrido();
      return;
    },
   
    recorrido() {
      const estados = this.stack.states;
      const i = 0;
      this.$emit("start-simulation", estados, i);
      this.showAlert();
      setTimeout(() => {
        this.stack.world.name=this.inputString
        this.stack.world.accepted=this.worldValidate
        this.inputString = "";
      }, 500);
    },
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
    showAlert() {
      this.dismissCountDown = this.dismissSecs;
    },
  },
};
</script>

<style></style>
