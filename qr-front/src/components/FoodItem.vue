<script setup lang="ts">
import {Food} from "@/api/main.ts";
import ImageComponent from "@/components/image-component.vue";
import {formattedPrice} from "../utils.ts";
import {CardStorage} from "@/storages/card-storage.ts";
import {MinusIcon, PlusIcon} from "@heroicons/vue/16/solid";
const {item} = defineProps<{
  item: Food
}>();

const cardStorage = CardStorage.getInstance();
function addToCard() {
  cardStorage.addGood({
    id: item.id,
    name: item.name,
    picture_url: item.images.length > 0 ? item.images[0].image : undefined,
    price: item.price,
    quantity: 1
  })
}
</script>

<template>
  <article class="bg-white p-4 gap-4 rounded flex">
        <RouterLink :to="{
          name: 'food',
          params: {
            id: item.id
          }
        }">
             <ImageComponent class="h-[180px] w-[180px] rounded-xl" :url="item.images.length > 0 ? item.images[0].image : undefined" :alt="item.name"></ImageComponent>
        </RouterLink>
        <div class="flex flex-col justify-between w-full">
            <div>
                <h3 class="">{{ item.name }}</h3>
                <p class="text-[#66666E] mt-2 text-sm">{{ item.description }}</p>
            </div>
            <div v-if="cardStorage.checkInBasket(item.id)">
              <section class="flex items-center justify-between">
                  <div class="w-full flex items-center gap-4 text-center py-2 ">
                    <div @click="cardStorage.decreaseGood(item.id)" class="bg-white cursor-pointer p-1 rounded-lg"><MinusIcon  class="w-5 h-5"></MinusIcon></div>
                    <div>{{cardStorage.getFromBasket(item.id).quantity}}</div>
                    <div @click="cardStorage.increaseGood(item.id)" class="bg-white cursor-pointer p-1 rounded-lg"><PlusIcon class="w-5 h-5"></PlusIcon></div>
                  </div>
                  <div class="font-medium  white-space-pre text-nowrap">
                    {{formattedPrice(item.price * cardStorage.getFromBasket(item.id).quantity)}} ₸
                  </div>
                </section>
            </div>
            <section v-else @click="addToCard" class="mt-4 w-full">
                <div class="cursor-pointer w-full text-white bg-slate-700 text-center flex justify-center items-center py-2 font-medium rounded">
                  <div class="">{{formattedPrice(item.price)}} ₸</div>
                </div>
            </section>
        </div>
    </article>
</template>

<style scoped>

</style>