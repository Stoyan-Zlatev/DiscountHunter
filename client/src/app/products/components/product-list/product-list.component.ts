import { Component, OnInit } from '@angular/core'
import { ProductService } from '../../service/product.service'
import { Product, ProductData } from '../../models/product'

@Component({
	selector: 'product-list',
	templateUrl: './product-list.component.html',
	styleUrls: ['./product-list.component.scss'],
})
export class ProductListComponent implements OnInit {
	products: ProductData[] = []
  public transform = [{"height": "200", "width": "200", "focus": "auto"}]

	constructor(private product: ProductService) {}

	ngOnInit(): void {
		this.product.getProducts().then((products: any) => {
			this.products = products
		})
	}
}
