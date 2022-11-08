import {Component, OnInit} from '@angular/core'
import {ActivatedRoute, ParamMap, Router} from '@angular/router'
import {ProductService} from '../../service/product.service'
import {ProductData} from '../../models/product'

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.scss'],
})
export class ProductItemComponent implements OnInit {
  public id: string = ''
  public productItem: any = null

  constructor(private product: ProductService, private route: ActivatedRoute, private router: Router) {
  }

  ngOnInit(): void {
    window.scroll({
      top: 0,
      left: 0,
      behavior: 'smooth'
    });
    this.route.params.subscribe((params) => {
      this.id = params['id']
    })
    this.product.getProductById(this.id).then((data: any) => {
      data.image = data.image + "?MYRAVRESIZE=600"
      this.productItem = data
    })
  }

  onBack(): void {

    this.route.queryParams.subscribe((param) => {
      this.router.navigateByUrl(`/?search=${param["search"]}&page=${param["page"]}&store=${param["store"]}`)
    })

  }
}

