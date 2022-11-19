// noinspection JSDeprecatedSymbols

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

  public async getFilteredProducts(pageNumber: any, search: any, minDate: any, store: any, promotionInterval: any): Promise<ProductData[] | null | undefined> {
    let products = null
    let productsWithImages = null
    try {
      products = await this.http.get<any>(`${environment.apiUrl}products/?search=${search}&page=${pageNumber}&promotion_expire_gte=${minDate}
      &store=${store}&promotion_expire_lte=${promotionInterval[1]}&promotion_start=${promotionInterval[0]}`).toPromise()
      productsWithImages = products.results.map((productItem: any) => new Product(productItem))
    } catch (error) {
      console.error(error)
    }
    return productsWithImages
  }

  public async getFilteredProductsCount(search: any, minDate: any, store: any, promotionInterval: any): Promise<any> {
    const productCount = await this.http.get<any>(`${environment.apiUrl}products/?search=${search}&promotion_expire_gte=${minDate}
    &store=${store}&promotion_expire_lte=${promotionInterval[1]}&promotion_start=${promotionInterval[0]}`).toPromise()
    return productCount.count
  }

  public async getProductById(id: any): Promise<ProductData | null> {
    if (!id) return null
    const product = await this.http.get<Product>(`${environment.apiUrl}product/${id}/`).toPromise()
    return new Product(product).data
  }
}
