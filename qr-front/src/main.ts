import { createApp } from 'vue'
import './style.css';
import router from './routers';
import App from './App.vue';
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { ScrollToPlugin } from "gsap/ScrollToPlugin";

gsap.registerPlugin(ScrollTrigger, ScrollToPlugin);


const app = createApp(App);


// Make sure to _use_ the router instance to make the
// whole app router-aware.
app.use(router);
app.mount('#app')
