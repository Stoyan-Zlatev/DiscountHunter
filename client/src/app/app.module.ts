import {BrowserModule} from '@angular/platform-browser'
import {NgModule} from '@angular/core'

import {AppRoutingModule} from './app-routing.module'
import {AppComponent} from './app.component'
import {BrowserAnimationsModule} from '@angular/platform-browser/animations'

import {HttpClientModule} from '@angular/common/http';
import {ProductItemComponent} from './products/components/product-item/product-item.component';
import {ProductListComponent} from './products/components/product-list/product-list.component';
import {FormsModule} from "@angular/forms";
import {ImagekitioAngularModule} from "imagekitio-angular";
import {NgxImageCompressService} from "ngx-image-compress";
import {NgxPaginationModule} from 'ngx-pagination';

import {environment} from "../environments/environment";

@NgModule({
  declarations: [AppComponent, ProductItemComponent, ProductListComponent],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    NgxPaginationModule,
    ImagekitioAngularModule.forRoot({
      publicKey: 'public_oXZdj3cM/LMDPIkyaO4/53RBr/8=',
      urlEndpoint: 'https://ik.imagekit.io/0ddkb3lir',
      authenticationEndpoint: "http://www.yourserver.com/auth",
    }), FormsModule,
  ],
  providers: [NgxImageCompressService],
  bootstrap: [AppComponent],
})

export class AppModule {
  transform = [{"height": "300", "width": "300", "focus": "auto"}]
}
