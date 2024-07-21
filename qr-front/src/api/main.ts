import { instance } from '../plugins/axios-instance';

export interface Food {
    id: number;
    name: string;
    description: string;
    price: number;
    category: Category;
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
    categories: Category[],
    params: {
        adaptive: boolean,
        style: string,
        mainColor: string
    }
}

export const getStore = (slug: string) => {
    return instance.get<Store>(`/store/${slug}`);
}