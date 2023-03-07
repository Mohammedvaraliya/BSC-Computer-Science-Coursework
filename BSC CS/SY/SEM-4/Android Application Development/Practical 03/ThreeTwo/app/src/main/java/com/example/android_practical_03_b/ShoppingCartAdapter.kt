package com.example.android_practical_03_b

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import android.widget.ImageView
import android.widget.TextView

class ShoppingCartAdapter (context: Context, shoppingCardList: ArrayList<ShoppingCart?>) :
    ArrayAdapter<ShoppingCart?>(context, 0, shoppingCardList) {

    override fun getView(position: Int, convertView: View?, parent: ViewGroup): View {

        var listitemView = convertView
        if (listitemView == null) {
            // Layout Inflater inflates each item to be displayed in GridView.
            listitemView = LayoutInflater.from(context).inflate(R.layout.item_shopping_cart, parent, false)
        }

        val shoppingCart: ShoppingCart? = getItem(position)
        val productImage = listitemView!!.findViewById<ImageView>(R.id.iv_product_image)
        val productName = listitemView.findViewById<TextView>(R.id.tv_product)

        if (shoppingCart != null) {
            productName.text = shoppingCart.productName
            productImage.setImageResource(shoppingCart.imageId)
        }
        return listitemView
    }
}