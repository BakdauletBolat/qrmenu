<template>
  <RouterLink :to="{
    name: 'food',
    params: {
      id: food.id
    }
  }" :id="food.id" class="bg-white relative tr rounded hover:cursor-pointer" >
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
    <!-- <add-to-card class="p-3" :food="food"></add-to-card> -->
  </RouterLink>
</template>
<script lang="ts" setup>
defineProps(['food']);



</script>
<style>
.transparent-gradient {
  background: rgb(0,0,0);
  background: linear-gradient(180deg, rgb(0, 0, 0) 0%, rgba(0,0,0,0.19) 50%);
}
.tr {
  transition: all .3s ease;
}
</style>