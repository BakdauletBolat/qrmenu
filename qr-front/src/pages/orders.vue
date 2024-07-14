<template>
    <div class="bg-slate-100 min-h-[100vh] pt-5">
        <Dialog v-model="isOpen" title="Детально">
            <TableDetail :table="currentTable"></TableDetail>
        </Dialog>
        <div class="container mx-auto">
            <div class="flex justify-between items-center">
                <h1 class="text-2xl font-bold ">Заказы</h1>
                <RouterLink :to="{
                    name: 'qr'
                }" class="flex gap-2 items-center cursor-pointer hover:primary-background p-2 rounded-sm hover:text-white">
                    <div class="text-sm">Сканировать для клиента</div>
                    <QrCodeIcon class="w-7 h-7"></QrCodeIcon>
                </RouterLink>
            </div>
            <div class="mt-5 flex flex-col gap-2">
                <div @click="onClickDetail(index)"
                    class="bg-white border rounded-sm flex justify-between p-3 cursor-pointer hover:bg-slate-50"
                    v-for="(item, index) in orders">
                    <div class="flex lg:items-center flex-col lg:flex-row lg:gap-2">
                        <div>Столик {{ item.table }}</div>
                        <div>( {{ item.food_items.map((item:any) => item.food.name).toString() }} )</div>
                    </div>
                    <div class="flex items-end gap-1 lg:items-center flex-col lg:flex-row  lg:gap-4">
                        <div class="font-bold">{{ item.total_cost }}₸</div>
                        <div>
                            <CheckBadgeIcon class="w-7 h-7 bg-lime-500 text-white rounded p-1" v-if="!item.is_active">
                            </CheckBadgeIcon>
                            <ForwardIcon v-else class="w-7 h-7 bg-orange-500 text-white rounded p-1"></ForwardIcon>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup lang="ts">
import { instance } from '@/plugins/axios-instance';
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { CheckBadgeIcon, ForwardIcon, QrCodeIcon } from '@heroicons/vue/24/outline';
import Dialog from '@/components/Dialog';
import TableDetail from '@/components/table-detail.vue';
const orders = ref<any[]>([]);

const currentTable = ref(null);
const route = useRoute();
const router = useRouter();
const isOpen = ref(false);

onMounted(() => {
    getTables();
});

const onClickDetail = (id: number) => {
    isOpen.value = true;
    currentTable.value = orders.value[id];
}

const getTables = () => {
    instance.get('/table/').then(res => {
        orders.value = res.data;
    }).catch((e) => {
        if (e.response.status === 401) {
            localStorage.removeItem('token');
            router.push({
                name: 'login',
                query: {
                    redirect: route.name?.toString()
                }
            })
        }
    })
}


</script>