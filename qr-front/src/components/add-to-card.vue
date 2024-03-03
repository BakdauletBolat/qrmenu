<template>
  <div @click="addToCard" class="text-nowrap bg-orange-400 hover:border-orange-400 flex items-center mt-2 justify-center gap-3 hover:border-white border border-transparent rounded-md text-center p-3 text-white text-sm">
    <shopping-cart-icon class="w-6 h-6" :class="{
      'h-5 w-5': big
    }"></shopping-cart-icon>
    Добавить в корзину
  </div>
</template>
<script lang="ts" setup>
import {ShoppingCartIcon} from "@heroicons/vue/24/outline";
import {CardStorage} from "@/storages/card-storage.ts";
const cardStorage = CardStorage.getInstance()
 const props = defineProps(['food','big']);
const addToCard = () => {
    cardStorage.addGood({
      id: props.food.id,
      price: props.food.discount_price ? props.food.discount_price : props.food.price,
      picture_url: props.food.images.length > 0 ? props.food.images[0].image : null,
      name: props.food.name,
      quantity: 1
    })
  cardStorage.isActive.value = true;
}
</script>