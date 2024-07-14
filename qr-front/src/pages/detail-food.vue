<template>
    <LoadingComponent :is-loading="isLoading"></LoadingComponent>
    <AppHeaderComponent title="О блюде"></AppHeaderComponent>
    <div v-if="food" :id="food.id.toString()" class="bg-white min-h-[100vh] relative rounded" >
      <div class="w-full pt-4 max-w-[800px] px-4 mx-auto">
        <div class="flex flex-col md:flex-row gap-4">
          <div class="h-[250px] w-full md:w-[300px]">
          <ImageComponent class="w-full rounded h-full object-cover" :alt="food.name" :url="food.images.length > 0 ? food.images[0].image : undefined"></ImageComponent>
        </div>
        <div>
          <div class="font-medium text-2xl leading-5">{{ food.name }}</div>
          <div class="flex mt-4 gap-1 items-center">
          <p class="whitespace-nowrap  text-lg"
              :class="[food.discount_price ? '' : 'hidden']">
            {{ food.discount_price }} ₸
          </p>
          <p class="text whitespace-nowrap  text-lg"
              :class="[
                        food.discount_price
                          ? 'line-through text-gray-500 text-sm'
                          : '',
                      ]">
            {{ food.price }} ₸
          </p>
        </div>
          <div v-if="cardStorage.checkInBasket(food.id)">
              <section class="flex mt-4 items-center gap-3 justify-between">
                  <div class="w-full flex items-center gap-4 text-center py-2 ">
                    <div @click="cardStorage.decreaseGood(food.id)" class="cursor-pointer p-1 rounded-lg"><MinusIcon  class="w-5 h-5"></MinusIcon></div>
                    <div>{{cardStorage.getFromBasket(food.id).quantity}}</div>
                    <div @click="cardStorage.increaseGood(food.id)" class="cursor-pointer p-1 rounded-lg"><PlusIcon class="w-5 h-5"></PlusIcon></div>
                  </div>
                  <div class="font-medium  white-space-pre text-nowrap">
                    {{formattedPrice(food.price * cardStorage.getFromBasket(food.id).quantity)}} ₸
                  </div>
                </section>
            </div>
            <section v-else @click="addToCard" class="mt-4 w-full">
                <div class="cursor-pointer w-full text-white primary-background text-center flex justify-center items-center py-2 font-medium rounded">
                  <div class="flex justify-center items-center gap-2">
                    <ShoppingCartIcon class="h-6 w-6"></ShoppingCartIcon>
                    <span class="flex gap-1"><span class="md:block hidden">Добавить в корзину</span> {{formattedPrice(food.price)}} ₸</span>
                  </div>
                </div>
            </section>
        </div>
        </div>
        <div class="mt-4 gap-2 flex items-start flex-col w-full" >
        <div>
          <h3 class="font-medium text-xl leading-5">
            Описание
          </h3>
          <p class="mt-2 font-light leading-4 text-gray-500">
            {{ food.description }}
          </p>
        </div>
      </div>
      </div>
    </div>
  </template>
  <script lang="ts" setup>
import { useRoute } from 'vue-router';
import { onMounted, ref } from 'vue';
import { Food } from '@/api/main';
import {instance} from "@/plugins/axios-instance.ts";
import AppHeaderComponent from "@/components/app-header-component.vue";
import ImageComponent from "@/components/image-component.vue";
import {formattedPrice} from "@/utils.ts";
import {MinusIcon, PlusIcon} from "@heroicons/vue/16/solid";
import {CardStorage} from "@/storages/card-storage.ts";
import LoadingComponent from "@/components/loading-component.vue";
import {ShoppingCartIcon} from "@heroicons/vue/24/outline";

const route = useRoute();

const food = ref<Food | null>(null);
const isLoading = ref<boolean>(false);


const cardStorage = CardStorage.getInstance();


function addToCard() {
  cardStorage.addGood({
    id: food.value!.id,
    name: food.value!.name,
    picture_url: food.value!.images.length > 0 ? food.value!.images[0].image : undefined,
    price: food.value!.price,
    quantity: 1
  })
}
function loadFood() {
  isLoading.value = true;
  instance.get('/food/'+route.params.id)
      .then(res=>{
        food.value = res.data;
      }).catch(e=>{
        console.log(e);
  }).finally(()=>{
    isLoading.value = false;
  })
}

onMounted(()=>{
  loadFood();
  window.scrollTo({
    top: 0
  })
});

  </script>