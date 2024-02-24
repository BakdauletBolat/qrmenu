<template>
    <div v-if="data.hasOwnProperty('foods')">
        <div class="font-bold text-2xl">{{ data.title }}</div>
        <div class="flex flex-col gap-4 mt-4">
        <VerticalCard :food="food" v-for="food in data.foods"></VerticalCard>
    </div>
    </div>
    <div v-else>
        <VerticalCard :food="data"></VerticalCard>
    </div>
</template>
<script lang="ts" setup>
import VerticalCard from './vertical-card.vue';
defineProps(['data']);
</script>