import { Component, OnInit } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { ProductService } from './products/service/product.service'

@Component({
	selector: 'app-root',
	templateUrl: './app.component.html',
	styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
	title = 'discount_hunter'

	constructor(private http: HttpClient) {}

	ngOnInit() {}
}
