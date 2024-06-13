<template>
    <div class="w-full" v-if="!isQrLoaded">
        <div class="grid grid-cols-1 gap-5" v-if="cardStorage.goods.value.length > 0">
            <BasketCard v-for="item in cardStorage.goods.value" :key="item.name" :item="item"></BasketCard>
        </div>
        <div v-else class="text-center p-2">Пока что пусто</div>
        <div class="border-t bg-white w-full py-5 mt-5 text-lg font-medium">
            <div class="flex w-full justify-between">
                <div>Общая стоимость</div>
                <div>{{ cardStorage.totalCost }} ₸</div>
            </div>
        </div>

    </div>
    <div v-if="isQrLoaded" class="mt-3 mb-5">
        <div class="flex text-slate-500 items-center justify-center font-light w-full mb-3">
            <div class="text-center">Покажите QR официанту</div>
        </div>
        <qrcode-vue class="w-full" :size="300" :render-as="renderAs" :value="qrValue"></qrcode-vue>
    </div>
</template>
<script setup lang="ts">
import { CardStorage } from '@/storages/card-storage.ts';
import BasketCard from './BasketCard.vue';
import QrcodeVue, { RenderAs } from 'qrcode.vue'
import { onMounted, ref } from 'vue';
import { instance } from '@/plugins/axios-instance';
const cardStorage = CardStorage.getInstance();
const renderAs = ref<RenderAs>('svg')
const isQrLoaded = ref(false);
const isLoadingQr = ref(false);
const qrValue = ref('');
const getTableId = async () => {
    isLoadingQr.value = true;
    try {
        const res = await instance.post('/table/create/', {
            user_uuid: localStorage.getItem('user_uuid'),
            food_items: cardStorage.goods.value.map((item: any) => {
                return {
                    qty: item.quantity,
                    food_id: item.id,
                    price: item.price
                }
            })
        });
        qrValue.value = `{"table_id":"${res.data.id}"}`;
        isQrLoaded.value = true;
    }
    catch (e) {
        console.log(e);
    }
    finally {
        isLoadingQr.value = false;
    }
}
onMounted(() => {

});

</script>