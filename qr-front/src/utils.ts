export function formattedPrice(price?: number | string) {
    const nPrice = parseFloat(price!.toString());
    if (nPrice == undefined) {
        return '0';
    }
    return nPrice!.toLocaleString().replace(/,/g, ' ');
}