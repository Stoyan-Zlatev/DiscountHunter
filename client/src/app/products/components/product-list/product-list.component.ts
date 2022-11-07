import {Component, OnInit} from '@angular/core'
import {ProductService} from '../../service/product.service'
import {Product, ProductData} from '../../models/product'
import {ActivatedRoute, ParamMap, Router} from '@angular/router'


@Component({
  selector: 'product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.scss'],
})
export class ProductListComponent implements OnInit {
  products: ProductData[] = []
  p: any = 1;
  productsCount: number = 1
  collection: any[] = [];
  searchName: string = ''
  itemsPerPage: number = 15
  pagesCount: number = 1
  startDate: any = new Date().toISOString()

  constructor(private route: ActivatedRoute, private product: ProductService, private router: Router,) {
  }

  public changingQueryParams() {
    this.router.navigate(
      [],
      {
        relativeTo: this.route,
        replaceUrl: true,
        queryParams: {page: this.p, search: this.searchName},
        queryParamsHandling: 'merge', // remove to replace all query params by provided
      });
  }

  ngOnInit(): void {
      this.route.queryParams.subscribe((param) => {
        this.reload(param["page"], param["search"], this.startDate)
    })
  }

  reload(event: any, search: any, startDate: any): void {
    this.p = event
    this.searchName = search
    this.product.getFilteredProductsCount(this.searchName, startDate).then((productsCount: any) => {
      this.productsCount = productsCount
      this.pagesCount = Math.ceil(this.productsCount / this.itemsPerPage)
      console.log("Pages count: p", this.pagesCount, this.p)
      if (this.p > this.pagesCount || this.p < 1) {
        this.p = 1
      }
      this.product.getFilteredProducts(this.p, this.searchName, startDate).then((products: any) => {
        this.products = products.map((x: Product) => {
          var product: ProductData = x.data
          return {
            name: product.name.substring(0, 20),
            id: product.id,
            image: product.image,
            price: product.price,
            promotionStart: product.promotionStart,
            promotionEnd: product.promotionEnd,
            store: product.store
          }
        })
        console.log(this.products)
      })
      this.changingQueryParams()
    })
    this.route.paramMap.subscribe((params: ParamMap) => {
      params.keys
    });
    this.changingQueryParams()
  }
}
