package com.example.android_practical_03_b

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.GridView

class MainActivity : AppCompatActivity() {

    private lateinit var gvShoppingCart: GridView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        gvShoppingCart = findViewById(R.id.gv_shopping_cart)
        val shoppingCartList: ArrayList<ShoppingCart?> = ArrayList()

        shoppingCartList.add(ShoppingCart("Fruits", R.drawable.image_1))
        shoppingCartList.add(ShoppingCart("Tracking", R.drawable.image_2))
        shoppingCartList.add(ShoppingCart("Chips", R.drawable.image_3))
        shoppingCartList.add(ShoppingCart("Oranges", R.drawable.image_4))
        shoppingCartList.add(ShoppingCart("Sun Set", R.drawable.image_5))
        shoppingCartList.add(ShoppingCart("Animal", R.drawable.image_6))
        shoppingCartList.add(ShoppingCart("scenary", R.drawable.image_7))
        shoppingCartList.add(ShoppingCart("Coconut", R.drawable.image_8))
        shoppingCartList.add(ShoppingCart("Mangos", R.drawable.image_9))

        val adapter = ShoppingCartAdapter(this, shoppingCartList)
        gvShoppingCart.adapter = adapter
    }

}