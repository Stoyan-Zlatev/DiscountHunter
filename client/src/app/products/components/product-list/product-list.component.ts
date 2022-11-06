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
    this.route.paramMap.subscribe((params: ParamMap) => {
      this.p = params.get('id') || 1;
    });
    this.product.getProductsCount().then((pagesCount: any) => {
      this.productsCount = pagesCount
      if (this.p > pagesCount || this.p < 1) {
        this.p = 1
      }
    })
    this.product.getProducts(this.p).then((products: any) => {
      this.products = products
    })
  }

  reload(event: any): void {
    this.p = event
    if (this.searchName == '') {
      this.product.getProducts(this.p).then((products: any) => {
        this.products = products
      })
    } else {
      this.product.getFilteredProducts(this.p, this.searchName).then((products: any) => {
        this.products = products
      })
    }
    this.route.paramMap.subscribe((params: ParamMap) => {
      params.keys
    });
    this.changingQueryParams()
  }

  setValue(searchName: string) {
    this.searchName = searchName;
    this.product.getFilteredProductsCount(this.searchName).then((productsCount: any) => {
      this.productsCount = productsCount
      this.pagesCount = Math.ceil(this.productsCount / this.itemsPerPage)
      console.log("Pages count: p", this.pagesCount, this.p)
      if (this.p > this.pagesCount || this.p < 1) {
        this.p = 1
      }
      console.log(this.p)
      this.product.getFilteredProducts(this.p, this.searchName).then((products: any) => {
        this.products = products
      })
      this.changingQueryParams()
    })
  }
}
