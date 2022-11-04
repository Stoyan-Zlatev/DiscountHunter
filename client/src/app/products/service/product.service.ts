import {Injectable} from '@angular/core'
import {HttpClient} from '@angular/common/http'
import {Product, ProductData} from '../models/product'
import {environment} from 'src/environments/environment'

@Injectable({
  providedIn: 'root',
})
export class ProductService {
  constructor(private http: HttpClient) {
  }

  public async getProducts(): Promise<ProductData[] | null | undefined> {
    let products = null
    let productsWithImages = null
    try {
      products = await this.http.get<any>(environment.apiUrl + 'products/').toPromise()
      console.log(products)
      productsWithImages = products.results.map((productItem: any) => new Product(this.getProductImage(productItem)).data)
    } catch (error) {
      console.error(error)
    }
    return productsWithImages
  }

  public async getProductById(id:any): Promise<ProductData | null> {
    if (!id) return null
    const product = await this.http.get<Product>(environment.apiUrl + 'product/' + id).toPromise()
    return new Product(this.getProductImage(product)).data
  }

  private getProductImage(product: any): Product {
    const tempProduct = {...product}

    console.log('tempProduct:', tempProduct)
    return tempProduct
  }
}
