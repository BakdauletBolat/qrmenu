import { instance } from '../plugins/axios-instance';

export interface Food {
    name: string;
    description: string;
    price: string;
    discount_price: string;
    images: Image[];
}

interface Image {
    image: string;
}

export interface Category {
    id: number;
    image: string | null;
    order: number;
    title: string;
    parent: string | null;
    foods: Food[];
}

export interface Store {
    name: string;
    address: string;
    image: string;
    categories: Category[];
}

export const getStore = (slug: string) => {
    return instance.get<Store>(`/store/${slug}`);
}