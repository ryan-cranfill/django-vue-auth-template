<template>
  <div id="app">
    <navbar v-if="isAuthenticated"></navbar>
<!--    <h1>Django VueJs Template</h1>-->
<!--    <div id="nav">-->
<!--     <router-link :to="{ name: 'home' }">Vue</router-link> |-->
<!--     <router-link :to="{ name: 'messages' }">Django Rest</router-link>-->
<!--    </div>-->
    <router-view/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import Navbar from './components/Navbar';

export default {
  name: 'app',
  components: {
    Navbar,
  },
  computed: mapGetters('auth', [
    'isAuthenticated',
  ]),
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
