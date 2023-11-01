<template>
  <div>
    <b-container class="ml-3 w-100">
      <b-row>
        <label style="font-weight: bold">ingrese su palabra:</label>
      </b-row>
      <b-row>
        <input v-model="inputString" type="text" />
      </b-row>
      <b-row class="mt-2">
        <b-button @click="validateWorld" variant="success">verificar</b-button>
      </b-row>
      <b-row class="mt-2">
        <b-alert show>{{ worldValidate ? 'palabra valida' : 'no valida'}}</b-alert>
      </b-row>
    </b-container>
   
  </div>
</template>

<script>
import { Stack } from "@/assets/stack.js";
export default {
  data() {
    return {
      inputString: "",
      stack: new Stack(),
      worldValidate: '',
    };
  },
  methods: {
    validateWorld() {
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
          this.recorrido()
          return
        }
      }

      this.stack.pushState(2);
      this.worldValidate = true;
      this.recorrido()
      return

    },
    recorrido(){
        const estados = this.stack.states;
        const i=0
        this.$emit('start-simulation', estados,i);
        
    }
  },
};
</script>

<style></style>
