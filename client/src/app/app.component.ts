import { Component } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  constructor(private http: HttpClient) {
    this.loadProducts();
  }

  products = []
  loadProducts() {
     this.http.get('http://127.0.0.1:8888/api/products/').subscribe((data) => console.log(data));
  }
}
