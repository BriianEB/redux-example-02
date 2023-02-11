import axios from 'axios';

import { uiActions } from './ui-slice';
import { cartActions } from './cart-slice';

const API_URL = 'http://localhost:5000/';


export function sendCart(cart) {
  return async function (dispatch) {
    dispatch(uiActions.showNotification({
      status: 'pending',
      title: 'Sending...',
      message: 'Sending cart data!'
    }));

    async function sendCart() {
      var url = API_URL + 'carts/1';
      await axios.put(url, cart);

      dispatch(uiActions.showNotification({
        status: 'success',
        title: 'Success!',
        message: 'Sent cart data successfully!'
      }));
    }

    sendCart().catch(function (e) {
      dispatch(uiActions.showNotification({
        status: 'error',
        title: 'Error!',
        message: 'Sending cart data failed!'
      }));
    });
  }
}

export function fetchCart() {
    return async function (dispatch) {
        async function fetchCart() {
            var url = API_URL + 'carts/1?full=true';
            var response = await axios.get(url);

            return response;
        }

        var cart_data = await fetchCart().catch(function (e) {
            dispatch(uiActions.showNotification({
              status: 'error',
              title: 'Error!',
              message: 'Fetching cart data failed!'
            }));
        });

        dispatch(cartActions.replaceCart(cart_data.data));
    }
}
