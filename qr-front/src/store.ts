import { reactive } from 'vue'
import {Food, Store} from './api/main';

export const store = reactive<{
    store: Store | undefined,
    setStore: Function,
    getProductById: Function
}>({
    store: undefined,
    getProductById(id: number): Food | null {
        this.store?.categories.forEach((category)=>{
            category.foods.forEach(food=>{
                if (food.id == id) {
                    return food;
                }
            });
        });
        return null;
    },
    setStore(store: Store) {
        this.store = store;
    }
});



