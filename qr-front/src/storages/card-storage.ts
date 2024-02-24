import { ref } from "vue";

interface Good {
    id: number;
    name: string;
    picture_url?: string;
    price: number;
    quantity: number;
}

abstract class AbstractCardStorage {
    goods = ref<Good[]>([]);
    isActive = ref<boolean>(false);
    constructor() {
        if (localStorage.getItem('goods') != null) {
            this.goods.value = JSON.parse(localStorage.getItem('goods')!);
        }
    }
    abstract addGood(good: Good): any;
    abstract increaseGood(id: number): any;
    abstract decreaseGood(id: number): any;
    abstract removeGood(id: number): any;
    abstract get totalCost(): number;
    abstract save(): any;
}

class LocalCardStorage extends AbstractCardStorage {
    constructor() {
        super();
    }
    get totalCost() {
        let total = 0;
        this.goods.value.forEach((item)=>{
            total += item.price * item.quantity;
        });
        return total;
    }
    addGood(good: Good) {
        const exists = this.goods.value.filter(item=>item.id == good.id);
        if (exists.length == 0) {
            this.goods.value.push(good);
        }
        else {
            exists[0].quantity += 1;
        }
        this.save();
    }
    increaseGood(id: number) {
        const exists = this.goods.value.filter(item=>item.id == id);
        if (exists.length) {
            exists[0].quantity += 1;
            this.save();
        }
    }
    decreaseGood(id: number) {
        const exists = this.goods.value.filter(item=>item.id == id);
        if (exists.length) {
            if (exists[0].quantity <= 1) {
                this.removeGood(id);
                return;
            }
            exists[0].quantity -= 1;
            this.save();
            return;
        }
    }
    removeGood(id: number) {
        const exists = this.goods.value.findIndex(item=>item.id == id);
        if (exists != -1) {
            this.goods.value.splice(exists, 1);
            this.save();
        }
    }
    save() {
        localStorage.setItem('goods', JSON.stringify(this.goods.value));
    }
}
export const CardStorage = (function () {
    let instance: LocalCardStorage;
    function createInstance() {
      return new LocalCardStorage();
    }
    return {
      getInstance: function () {
        if (!instance) {
          instance = createInstance();
        }
        return instance;
      },
    };
  })();