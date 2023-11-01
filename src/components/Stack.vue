<template>
  <b-container fluid>
    <b-row class="caja" v-for="(item, index) in word" :key="index">
      <h2 class="W-100">
        {{ item }}
      </h2>
    </b-row>
  </b-container>
</template>

<script>

export default {
    name:'stackComponents',
  props: {
    items: Object,
  },
  computed: {
    word() {
      return this.items.world.name.split("");
    },
  },
};
</script>

<style>
.caja {
  background-color: gray;
  color: black;
  border: solid 1px black;
  text-align: center;
  padding: 1px;
}
.caja h2{
    margin: auto;
}
</style>
