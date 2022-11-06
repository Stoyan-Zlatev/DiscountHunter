import {formatDate} from "@angular/common";

export class Product {

  data: any = null

  constructor(data: any) {
    console.log(data)
    this.data = new ProductData(data.id, data)
  }
}

export class ProductData {
  name: string = ''
  price: number = 0
  oldPrice: number = 0
  image?: string = ''
  id: string = ''
  subtitle: string = ''
  basePrice: string = ''
  quantity: string = ''
  discountPhrase: string = ''
  description: string = ''
  title: string = ''
  store: string = ''
  promotionStart: string = ''
  promotionEnd: string = ''
  storeLogo: any

  constructor(id: any, data: any) {
    console.log('id: ', typeof id)
    console.log("data:", data)
    this.id = id
    this.name = data.name || data.title
    this.title = data.title
    this.subtitle = data.sub_title
    this.price = data.new_price
    this.image = data.image_url || ''
    this.oldPrice = data.old_price
    this.basePrice = data.base_price
    this.quantity = data.quantity
    this.discountPhrase = data.discount_phrase
    this.description = data.description
    this.store = data.store
    this.promotionStart = formatDate(data.promotion_starts, 'dd/MM/yyyy', 'en-US')
    this.promotionEnd = formatDate(data.promotion_expires, 'dd/MM/yyyy', 'en-US')
    this.storeLogo = this.get_store_logo();
  }

  public get_store_logo(): any {
    switch (this.store) {
      case 'Kaufland':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Kaufland_Logo.svg/1200px-Kaufland_Logo.svg.png';
        break;
      case 'Lidl':
        return 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Lidl-Logo.svg/2048px-Lidl-Logo.svg.png';
        break;
      case 'Billa':
        return 'https://cdn.yox.bg/images/a47fffb8-a48b-434a-baf7-a7024604848a/%D0%BB%D0%BE%D0%B3%D0%BE-%D0%BD%D0%B0-%D0%B1%D0%B8%D0%BB%D0%BB%D0%B0-%D0%B1%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D0%B8%D1%8F-e%D0%BE%D0%BE%D0%B4.png';
        break;
    }
  }
}
