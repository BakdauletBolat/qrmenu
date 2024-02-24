<template>
    <div class="flex justify-between items-center text-lg font-bold mb-4">
        <div>
            Заказ выполнен ?
        </div>
        <div>
            <label class="flex items-center cursor-pointer">
                <input @click="update" type="checkbox" class="sr-only peer" :checked="!table.is_active">
                <div
                    class="relative w-11 h-6 bg-gray-200 rounded-full peer peer-focus:ring-4  dark:bg-gray-400 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-orange-600">
                </div>
            </label>
        </div>
    </div>
    <div class="flex flex-col gap-3">
        <div v-for="fooditem in table.food_items">
            <div class="grid grid-cols-[100px_1fr] gap-3 rounded-sm">
                <div class="h-[100px] block">
                    <img class="rounded w-full h-full object-cover"
                        :src="fooditem.food.images.length > 0 ? fooditem.food.images[0].length : 'https://demofree.sirv.com/nope-not-here.jpg'"
                        :alt="fooditem.food.name">
                </div>
                <div class="">
                    <div class="flex flex-col justify-between w-full">
                        <div class="text-lg">{{ fooditem.food.name }}</div>
                        <span class=" ">{{ fooditem.price }} ₸</span>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="flex justify-between mt-5 font-bold text-lg">
        <div>Общая сумма </div>
        <div>{{ table.total_cost }}₸</div>
    </div>
</template>
<script setup lang="ts">
import { instance } from '@/plugins/axios-instance';


const {table} = defineProps(['table']);

const update = () => {
    try {
        instance.post('/table/update/', {
            id: table.id,
            status: !table.is_active
        })
    }
    catch (e) {
        console.log(e);
    }
}

</script>