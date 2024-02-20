import { createApp } from 'vue'
import './output.css';
import router from './routers';
import App from './App.vue';

const app = createApp(App)
// Make sure to _use_ the router instance to make the
// whole app router-aware.
app.use(router);
app.mount('#app')
