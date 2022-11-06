import {NgModule} from '@angular/core'
import {Routes, RouterModule} from '@angular/router'
import {ProductListComponent} from './products/components/product-list/product-list.component'
import {ProductItemComponent} from './products/components/product-item/product-item.component'

const routes: Routes = [
  {
    path: '?search=:search&page=:id',
    component: ProductListComponent,
  }, {
    path: ':id',
    component: ProductListComponent,
  }, {
    path: '',
    component: ProductListComponent,
  }, {
    path: 'product/:id',
    component: ProductItemComponent,
  }
]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {
}
