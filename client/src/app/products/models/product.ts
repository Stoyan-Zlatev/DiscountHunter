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
  description:string = ''

  constructor(id: any, data: any) {
    console.log('id: ', typeof id)
    this.id = id
    this.name = data.name || data.title
    this.subtitle = data.subtitle
    this.price = data.new_price
    this.image = data.image_url || ''
    this.oldPrice = data.old_price
    this.basePrice = data.basePrice
    this.quantity = data.quantity
    this.discountPhrase = data.discount_phrase
    this.description = data.description
  }
}
