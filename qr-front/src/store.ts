import { reactive } from 'vue'
import {Store} from './api/main';

export const store = reactive<{
    store: Store | undefined,
    setStore: Function
}>({
    store: undefined,
    setStore(store: Store) {
        this.store = store;
    }
});



