<script setup lang="ts">
import NoImage from '@/assets/no-image.jpeg';

defineProps<{
  url?: string,
  alt?: string
}>()
</script>

<template>
<div class="overflow-hidden">
  <img v-if="url" class="w-full h-full object-cover" :alt="alt" :src="url"/>
  <img :src="NoImage" v-else :alt="alt">
</div>
</template>

<style scoped>

</style>