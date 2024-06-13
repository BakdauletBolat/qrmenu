<script setup lang="ts">
import {ChevronLeftIcon} from "@heroicons/vue/24/outline";
import {useRouter} from "vue-router";
defineProps<{
  title: string
}>();
const router = useRouter();
</script>

<template>
<header class="px-6 fixed z-50 bg-white w-full">
  <div @click="router.back()" class="flex gap-4 cursor-pointer items-center p-4">
    <ChevronLeftIcon class="h-6 w-6"></ChevronLeftIcon>
    <div class="text-xl">{{title}}</div>
  </div>
</header>
  <div class="h-[60px] bg-[#F4F4F6]"></div>
</template>

<style scoped>

</style>