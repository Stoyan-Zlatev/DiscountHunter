import {Component, OnInit} from '@angular/core'
import {ProductService} from '../../service/product.service'
import {Product, ProductData} from '../../models/product'
import {ActivatedRoute, ParamMap, Router} from '@angular/router'
import {formatDate} from "@angular/common";


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
  search: string = ''
  store: string = ''
  storeWrapper: string = "Супермаркети"
  itemsPerPage: number = 15
  pagesCount: number = 1
  currentDate: any = formatDate(new Date(), 'yyyy-MM-dd', 'en')

  constructor(private route: ActivatedRoute, private product: ProductService, private router: Router,) {
  }

  public changingQueryParams() {
    this.router.navigate(
      [],
      {
        relativeTo: this.route,
        replaceUrl: true,
        queryParams: {page: this.p, search: this.search, store: this.store},
        queryParamsHandling: 'merge', // remove to replace all query params by provided
      });
  }

  ngOnInit(): void {
    this.route.queryParams.subscribe((param) => {
      if(param["search"]) {
        this.search = param["search"]
      }
      if (param["store"]) {
        this.store = param["store"]
      }
      if (param["page"]) {
        this.p = param["page"]
      }
      this.reload(this.p,  this.search, this.currentDate, this.store)
    })
  }

  reload(event: any, search: any, startDate: any, store: any): void {
      window.scroll({
        top: 0,
        left: 0,
        behavior: 'smooth'
      });
    this.p = event
    this.search = search
    this.store = store
    if (this.store != '') {
      this.storeWrapper = this.store
    } else {
      this.storeWrapper = "Супермаркети"
    }
    this.product.getFilteredProductsCount(this.search, startDate, this.store).then((productsCount: any) => {

      this.productsCount = productsCount
      this.pagesCount = Math.ceil(this.productsCount / this.itemsPerPage)
      if (this.p > this.pagesCount || this.p < 1) {
        this.p = 1
      }
      this.product.getFilteredProducts(this.p, this.search, startDate, this.store).then((products: any) => {
        this.products = products.map((x: Product) => {
          var product: ProductData = x.data
          return {
            name: product.name.substring(0, 42),
            id: product.id,
            image: product.image+"?MYRAVRESIZE=200",
            price: product.price,
            promotionStart: product.promotionStart,
            promotionEnd: product.promotionEnd,
            store: product.store
          }
        })
      })
      this.route.paramMap.subscribe((params: ParamMap) => {
        params.keys
      });
      this.changingQueryParams()
    })
  }
}
