<script setup lang="ts">
import {Category} from "@/api/main.ts";
import ImageComponent from "@/components/image-component.vue";

defineProps<{
  item: Category
}>();
</script>

<template>
  <div class="bg-white cursor-pointer rounded overflow-hidden relative" >
    <ImageComponent class="h-[200px] w-full" :url="item.image" :alt="item.title"></ImageComponent>
    <div class="w-full absolute top-0 left-0 h-[200px] bg-black-gradient"></div>
    <div class="p-4 absolute bottom-0 w-full text-white text-center font-medium shantell-sans-regular">{{item.title}}</div>
  </div>
</template>

<style scoped>
.bg-black-gradient {
  background: rgb(0,0,0);
  background: linear-gradient(0deg, rgba(0,0,0,0.5) 0%, rgba(0,0,0,0.1) 100%);
}
</style>