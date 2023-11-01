<template>
  <div id="app">
    <hello-world class="header" :msj="'Automata de pila'" />
    <div class="container-main">
      <cytoscape
        class="cytoscape_style"
        ref="cyRef"
        :config="config"
        :preConfig="preConfig"
        :afterCreated="afterCreated"
      />
      <input-world @start-simulation="onStartSimulation"></input-world>
      <div>
        <label for="demo-sb">Spin Button</label>
        <b-form-spinbutton
          id="demo-sb"
          v-model="value"
          min="100"
          max="1000"
          step="100"
        ></b-form-spinbutton>
        <p>Value: {{ value }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import COSEBilkent from "cytoscape-cose-bilkent";
import helloWorld from "@/components/HeaderComponents.vue";
import inputWorld from "@/components/InputPalabra.vue";

export default {
  components: {
    helloWorld,
    inputWorld,
  },
  data: () => ({
    cy: [],
    value:500,
    elements: [
      { data: { id: "q0", label: "q0" } },
      { data: { id: "q1", label: "q1" } },
      { data: { id: "q2", label: "q2" } },

      {
        data: { id: "e0", source: "q0", target: "q0" },
      },
      {
        data: { id: "e1", source: "q0", target: "q1", label: "b , b / λ" },
      },
      {
        data: { id: "e2", source: "q0", target: "q1", label: "a , a / λ" },
      },
      {
        data: { id: "e3", source: "q1", target: "q1", label: "a , a / λ" },
      },
      {
        data: { id: "e4", source: "q1", target: "q1", label: "b , b / λ" },
      },
      {
        data: { id: "e5", source: "q1", target: "q2", label: "λ , # / #" },
      },
    ],
    config: {
      style: [
        {
          selector: "node",
          style: {
            "background-color": "#fff",
            color: "white",
            label: "data(id)",
          },
        },
        {
          selector: "edge#e4",
          style: {
            "padding-top": "5px",
            color: "red",
          },
        },
        {
          selector: "edge",
          style: {
            width: 2,
            "line-color": "#9998",
            color: "white",
            "curve-style": "bezier", 
            "target-arrow-shape": "triangle",
            label: "data(label)",
            "text-rotation": "autorotate",
          },
        },
        {
          selector: "#q2",
          style: {
            "border-color": "green", // Color del borde
            "border-width": "2px", // Grosor del borde
            "background-color": "white", // Color de fondo
            "border-opacity": "1",
            shape: "ellipse", // Forma del nodo
            "text-outline-color": "green", // Color del texto
            "text-outline-width": "2px", // Grosor del texto
          },
        },
      ],
    },
  }),
  methods: {
    preConfig(Cytoscape) {
      Cytoscape.use(COSEBilkent);
    },
    afterCreated(cy) {
      // this.cy.push(cy)
      cy.add(this.elements)
        .layout({ name: "grid", rows: 1, spacingFactor: 1.5 })
        .run();
    },
    onStartSimulation(estados, i) {
      if (i > estados.length) {
        return;
      }
      const estadoActual = estados[i];
      this.$refs.cyRef.instance.nodes().style({ "background-color": "white" });
      this.$refs.cyRef.instance
        .$(`#q${estadoActual}`)
        .style({ "background-color": "blue" });
      setTimeout(
        function () {
          this.onStartSimulation(estados, i + 1);
        }.bind(this),
        this.value
      ); // Cambia el tiempo de espera según tus preferencias
    },
  },
  mounted() {},
};
</script>

<style>
.cytoscape_style {
  width: 50%;
  height: 40%;
  background-color: black;
  border-radius: 5px;
}

.header {
  height: 60px;
  border-radius: 5px;
  margin-bottom: 2px;
}
.container-main {
  display: flex;
}
</style>
