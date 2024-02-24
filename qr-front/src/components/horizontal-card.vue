<template>
  <li class="relative rounded hover:cursor-pointer">
    <div class="w-full h-[250px] rounded-lg overflow-hidden relative">
        <div class="w-full h-full transparent-gradient absolute"></div>
        <img :alt="food.name" class="w-full h-full object-cover"
         :src="food.images.length > 0 ? food.images[0].image : 'https://media.istockphoto.com/id/1409329028/vector/no-picture-available-placeholder-thumbnail-icon-illustration-design.jpg?s=612x612&w=0&k=20&c=_zOuJu755g2eEUioiOUdz_mHKJQJn-tDgIAhQzyeKUQ='"/>
    </div>
    <div class="py-4 px-1 mt-2 gap-6 flex justify-between">
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
        <add-to-card :food="food" class="top-2 right-2 absolute"></add-to-card>
      </div>
    </div>
  </li>
</template>
<script lang="ts" setup>
import AddToCard from "@/components/add-to-card.vue";
defineProps(['food']);
</script>
<style>
.transparent-gradient {

  background: rgb(0,0,0);
background: linear-gradient(180deg, rgba(0,0,0,1) 0%, rgba(0,0,0,0.19) 50%);

}
</style>