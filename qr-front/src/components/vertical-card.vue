<template>
  <div class="relative grid grid-cols-[120px_1fr] items-center gap-4 rounded hover:cursor-pointer">
    <img
      class="h-[120px] w-full rounded-lg object-cover"
      :src="food.images.length > 0 ? food.images[0].image : 'https://media.istockphoto.com/id/1409329028/vector/no-picture-available-placeholder-thumbnail-icon-illustration-design.jpg?s=612x612&w=0&k=20&c=_zOuJu755g2eEUioiOUdz_mHKJQJn-tDgIAhQzyeKUQ='"
    />
    <div class="py-4 w-full px-1 mt-2 gap-1 flex flex-col justify-between">
      <div>
        <h3 class="font-medium leading-5">
          {{ food.name }}
        </h3>
        <div class="mt-1 text-xs font-normal leading-4 text-gray-500">
          {{ food.description }}
        </div>
      </div>
      <div class="flex flex-col gap-1">
        <p
          class="whitespace-nowrap text text-lg"
          :class="[food.discount_price ? '' : 'hidden']"
        >
          {{ food.price }} ₸
        </p>
        <p
          class="text whitespace-nowrap text-lg"
          :class="[food.discount_price ? 'line-through text-sm' : '']"
        >
          {{ food.price }} ₸
        </p>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { Food } from "../api/main";
defineProps<{
  food: Food;
}>();
</script>
