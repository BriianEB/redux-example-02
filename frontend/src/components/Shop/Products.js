import ProductItem from './ProductItem';
import classes from './Products.module.css';

import axios from 'axios';
import { useEffect, useState } from 'react';

const API_URL = 'http://localhost:5000/';


const Products = (props) => {
  const [products, setProducts] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState();

  useEffect(function () {
    async function getProducts() {
      var url = API_URL + 'products';
      var response = await axios.get(url);
      var products = response.data;
      setProducts(products);
      setIsLoading(false);
    }

    getProducts().catch(function (e) {
      setIsLoading(false);
      setError(e.message);
    });
  }, []);

  if (error) {
    return (
      <section className={classes['meals-error']}>
        <p>Error</p>
      </section>
    );
  }

  if (isLoading) {
    return (
      <section className={classes['meals-loading']}>
        <p>Loading...</p>
      </section>
    );
  }

  return (
    <section className={classes.products}>
      <h2>Buy your favorite products</h2>
      <ul>
        {products.map((product) => (
          <ProductItem
            key={product.id}
            id={product.id}
            title={product.name}
            price={product.price}
            description={product.description}
          />
        ))}
      </ul>
    </section>
  );
};

export default Products;
