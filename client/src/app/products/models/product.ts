export class Product {

  data: any = null

  constructor(data: any) {
    console.log(data)
    this.data = new ProductData(data.id, data)
  }
}

export class ProductData {
  name: string = ''
  description: string = ''
  price: number = 0
  quantity: number = 0
  storehouse: any = null
  backorderLimit: number = 0
  backordered = false
  image?: string = ''
  id: string = ''

  constructor(id: any, data: any) {
    console.log('id: ', typeof id)
    this.id = id
    this.name = data.name
    // this.description = data.description
    this.price = data.new_price
    // this.quantity = data.quantity
    // this.storehouse = data.storehouse
    // this.backorderLimit = data.backorderLimit
    // this.backordered = data.backordered
    this.image = data.image_url || ''
  }
}
