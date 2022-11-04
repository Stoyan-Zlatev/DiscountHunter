import {Component, OnInit} from '@angular/core'
import {ActivatedRoute} from '@angular/router'
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
  public transform = [{"height": "200", "width": "200", "focus": "auto"}]

  constructor(private product: ProductService, private route: ActivatedRoute) {
  }

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      this.id = params['id']
    })

    this.product.getProductById(this.id).then((data: any) => {
      this.productItem = data
    })
  }
}

