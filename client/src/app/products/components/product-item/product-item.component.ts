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
    this.route.params.subscribe((params) => {
      this.id = params['id']
    })
    this.product.getProductById(this.id).then((data: any) => {
      this.productItem = data
      console.log(data)
    })
  }

  onBack(): void {
    // this.route.parent?.paramMap.subscribe((param:ParamMap)=>{
    //   console.log(param.keys)
    // })
    this.route.queryParams.subscribe((param) => {
      console.log(param)
      this.router.navigateByUrl(`/?search=${param["search"]}&page=${param["page"]}`)
    })

  }
}

