<template>
<div class="relative">
  <router-view v-slot="{ Component }">
      <component :is="Component" />
</router-view>
  <Dialog v-model="cardStorage.isActive.value" title="Корзина">
      <UserCard></UserCard>
    </Dialog>
  <div class="px-4 fixed bottom-4 w-full">
    <div @click="cardStorage.isActive.value = true"
       class="primary-background cursor-pointer flex gap-4 items-center rounded-lg w-full p-4 z-10" v-if="cardStorage.goods.value.length > 0">
    <div>
      <p class="text-sm text-slate-100"><strong>{{cardStorage.goods.value.length}}</strong> блюдо на <strong>{{cardStorage.totalCost}}₸</strong></p>
      <p class="text-white text-lg font-medium">Перейти в корзину</p>
    </div>
  </div>
  </div>
</div>
</template>
<script setup lang="ts">
import { onMounted } from 'vue';
import {CardStorage} from "@/storages/card-storage.ts";
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
