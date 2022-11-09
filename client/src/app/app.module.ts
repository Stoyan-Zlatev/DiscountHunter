import {BrowserModule} from '@angular/platform-browser'
import {NgModule} from '@angular/core'

import {AppRoutingModule} from './app-routing.module'
import {AppComponent} from './app.component'
import {BrowserAnimationsModule} from '@angular/platform-browser/animations'

import {HttpClientModule} from '@angular/common/http';
import {ProductItemComponent} from './products/components/product-item/product-item.component';
import {ProductListComponent} from './products/components/product-list/product-list.component';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {NgxImageCompressService} from "ngx-image-compress";
import {NgxPaginationModule} from 'ngx-pagination';
import {DatePickerModule, DateRangePickerModule, MaskedDateTimeService} from '@syncfusion/ej2-angular-calendars'

@NgModule({
  declarations: [AppComponent, ProductItemComponent, ProductListComponent],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    NgxPaginationModule,
    FormsModule,
    ReactiveFormsModule,
    DatePickerModule,
    DateRangePickerModule
  ],
  providers: [NgxImageCompressService, MaskedDateTimeService],
  bootstrap: [AppComponent],
})

export class AppModule {
  transform = [{"height": "300", "width": "300", "focus": "auto"}]
}
