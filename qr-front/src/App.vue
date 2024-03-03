<template>
<router-view v-slot="{ Component }">
  <transition name="slide-fade">
    <keep-alive>
      <component :is="Component" />
    </keep-alive>
  </transition>
</router-view>
</template>
<script setup lang="ts">
import { onMounted } from 'vue';

onMounted(()=>{
  const uuid = crypto.randomUUID();
  if (!localStorage.getItem('user_uuid')) {
    localStorage.setItem('user_uuid', uuid.toString());
  }

});
</script>
<style>
.slide-fade-enter-active {
  transition: all 0.2s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.2s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
</style>
