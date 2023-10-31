import Vue from "vue";
import App from "./App.vue";
import VueCytoscape from "vue-cytoscape";
import VueI18n from "vue-i18n";
Vue.config.productionTip = false;
Vue.use(VueCytoscape);
Vue.use(VueI18n);

const messages = {
  es: require('./assets/es.json'),
  en: require('./assets/en.json'),
  // Agrega más idiomas y archivos de traducción según sea necesario
};

// Configura vue-i18n
const i18n = new VueI18n({
  locale: 'es', // Idioma predeterminado
  fallbackLocale: 'es', // Idioma de respaldo
  messages,
});



new Vue({
  render: (h) => h(App),
  i18n,
}).$mount("#app");
