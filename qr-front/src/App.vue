<template>
<div class="relative">
  <router-view v-slot="{ Component }">
      <component :is="Component" />
</router-view>
  <Dialog v-model="cardStorage.isActive.value" title="Корзина">
      <UserCard></UserCard>
    </Dialog>
  <div @click="cardStorage.isActive.value = true" class="fixed cursor-pointer rounded-bl-xl flex gap-4 items-center rounded-tl-xl bottom-[100px] right-0 p-6 bg-slate-700 z-10" v-if="cardStorage.goods.value.length > 0">
    <ShoppingCartIcon class="h-8 w-8 text-white"></ShoppingCartIcon>
    <div class="text-white text-xl">Корзина {{cardStorage.goods.value.length}}</div>
  </div>
</div>
</template>
<script setup lang="ts">
import { onMounted } from 'vue';
import {CardStorage} from "@/storages/card-storage.ts";
import {ShoppingCartIcon} from "@heroicons/vue/24/outline";
import Dialog from "@/components/Dialog/index.ts";
import UserCard from "@/components/UserCard.vue";

const cardStorage = CardStorage.getInstance();

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
  opacity: 0;
}
</style>
