<template>
  <router-view>
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
