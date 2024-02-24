<template>
  <div class="bg-slate-100">
    <div class="max-w-[90%] mx-auto h-[100vh] ">
      <div class="flex w-full gap-3 items-center justify-center pt-4">
        <input v-model="table_number" class="w-full focus:outline-0 rounded-lg p-3 text-4xl text-center" type="number"
          placeholder="Введите столик" />
        <button @click="assign" class="p-3 bg-orange-400 rounded-lg h-full text-4xl">
          <ChevronRightIcon class="w-[36px]  text-white h-[36px]"></ChevronRightIcon>
        </button>
      </div>
      <div class="grid grid-cols-3 mt-5 gap-3">
        <div @click="table_number = i"
          class="p-3 py-5 hover:bg-orange-400 cursor-pointer bg-white border-2 text-center rounded-sm h-full text-4xl"
          v-for="i in numberList2">{{ i }}</div>
      </div>
    </div>
  </div>
</template>
<script lang="ts" setup>
import { instance } from "@/plugins/axios-instance";
import { ChevronRightIcon } from "@heroicons/vue/24/outline";
import { computed, ref } from "vue";
import { useRoute, useRouter } from "vue-router";

const numberList = Array.from({ length: 100 }, (_, index) => index + 1);
const table_number = ref<number | null>(null);
const route = useRoute();
const router = useRouter();

const assign = async () => {
  try {
    await instance.post('/table/assign/', {
      id: route.params.id,
      table: table_number.value
    });
    router.push({name: 'home'});
  }
  catch (e) {
    console.log(e);
  }

}

const numberList2 = computed(() => {
  if (table_number.value === null) {
    return numberList;
  }
  else {
    return numberList.filter(i => i.toString().startsWith(table_number.value!.toString()));
  }
})
</script>