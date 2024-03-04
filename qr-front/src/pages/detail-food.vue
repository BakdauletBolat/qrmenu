<template>
    <div v-if="food" :id="food.id.toString()" class="bg-white relative tr rounded hover:cursor-pointer" >
      <div class="w-full h-[250px] rounded-lg overflow-hidden relative">
          <div class="w-full h-full transparent-gradient absolute"></div>
          <img :alt="food.name" class="w-full h-full object-cover"
           :src="food.images.length > 0 ? food.images[0].image : 'https://media.istockphoto.com/id/1409329028/vector/no-picture-available-placeholder-thumbnail-icon-illustration-design.jpg?s=612x612&w=0&k=20&c=_zOuJu755g2eEUioiOUdz_mHKJQJn-tDgIAhQzyeKUQ='"/>
      </div>
      <div class="py-4 px-1 mt-2 w gap-6 flex justify-between w-full" >
        <div>
          <h3 class="font-medium text-xl leading-5 shantell-sans-regular text-orange-400">
            {{ food.name }}
          </h3>
          <p class="mt-2 text-xs font-normal leading-4 text-gray-500">
            {{ food.description }}
          </p>
        </div>
        <div class="flex flex-col gap-1 items-center">
          <p
              class="whitespace-nowrap shantell-sans-regular text-lg"
              :class="[food.discount_price ? '' : 'hidden']">
            {{ food.discount_price }} ₸
          </p>
          <p
              class="text whitespace-nowrap shantell-sans-regular text-lg"
              :class="[
                        food.discount_price
                          ? 'line-through text-gray-500 text-sm'
                          : '',
                      ]">
            {{ food.price }} ₸
          </p>
        </div>
      </div>
    </div>
  </template>
  <script lang="ts" setup>
import { useRoute } from 'vue-router';
import { store } from "../store";
import { onMounted, ref } from 'vue';
import { Food } from '@/api/main';

const route = useRoute();

const food = ref<Food | null>(null);

onMounted(()=>{
  console.log( store.getProductById(parseInt(route.params.id.toString())) )
 food.value = store.getProductById(parseInt(route.params.id.toString()));
});

  </script>