Aim: ```Create an application to use Gridview for shopping cart application.```

1. Layout file - `practical_three_two.xml`
    
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        android:layout_width="match_parent"
        android:layout_height="match_parent">
    
        <!-- android:numColumns=2 is the number of columns for Grid View
             android:horizontalSpacing is the space between horizontal grid items -->
        <GridView
            android:id="@+id/gv_shopping_cart"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:horizontalSpacing="6dp"
            android:numColumns="2"
            android:verticalSpacing="6dp" />
    
    </androidx.constraintlayout.widget.ConstraintLayout>
    ```


1. Layout file - `item_shopping_cart.xml`
    
    ```xml
    <?xml version="1.0" encoding="utf-8"?><!-- XML implementation of Card Layout -->
    <androidx.cardview.widget.CardView
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        android:layout_width="match_parent"
        android:layout_height="120dp"
        android:layout_gravity="center"
        android:layout_margin="5dp"
        app:cardCornerRadius="5dp"
        app:cardElevation="5dp">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical">

            <ImageView
                android:id="@+id/iv_product_image"
                android:layout_width="100dp"
                android:layout_height="100dp"
                android:layout_gravity="center"
                android:src="@mipmap/ic_launcher" />

            <TextView
                android:id="@+id/tv_product"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:text="@string/app_name"
                android:textSize="16sp"
                android:textStyle="bold"
                android:textAlignment="center" />
        </LinearLayout>
    </androidx.cardview.widget.CardView>

    ```
    

1. Activity file - `PracticalThreeTwo.kt`
    
    ```kotlin
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
    ```
    

1. `ShoppingCartAdapter.kt`
    
    ```kotlin
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
    ```
    

1. `ShoppingCart.kt`
    
    ```kotlin
    package com.example.android_practical_03_b

    data class ShoppingCart(var productName: String, var imageId: Int)
    ```
    

## Output

