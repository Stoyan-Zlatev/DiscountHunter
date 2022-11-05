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

  constructor(private route: ActivatedRoute, private product: ProductService) {
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
    this.product.getProducts(this.p).then((products: any) => {
      this.products = products
    })
    this.route.paramMap.subscribe((params: ParamMap) => {
      params.keys
    });
  }
}
