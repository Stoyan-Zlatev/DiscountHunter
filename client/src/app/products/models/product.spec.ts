import { Product } from './product';

describe('Product', () => {
  it('should create an instance', (data:any) => {
    expect(new Product(data)).toBeTruthy();
  });
});
