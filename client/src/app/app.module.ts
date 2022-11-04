import { BrowserModule } from '@angular/platform-browser'
import { NgModule } from '@angular/core'

import { AppRoutingModule } from './app-routing.module'
import { AppComponent } from './app.component'
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'

import { HttpClientModule } from '@angular/common/http';
import { ProductItemComponent } from './products/components/product-item/product-item.component';
import { ProductListComponent } from './products/components/product-list/product-list.component';
@NgModule({
	declarations: [AppComponent, ProductItemComponent, ProductListComponent],
	imports: [BrowserModule, HttpClientModule, AppRoutingModule, BrowserAnimationsModule],
	providers: [],
	bootstrap: [AppComponent],
})
export class AppModule {}
