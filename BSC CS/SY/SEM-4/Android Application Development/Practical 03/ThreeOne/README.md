Aim: ```Create an application to create Image Flipper and Image Gallery. On click on the image display the information about the image.```

1. Layout file - `practical_three.xml`
    
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        android:layout_width="match_parent"
        android:layout_height="match_parent">
    
        <ImageView
            android:id="@+id/iv_show"
            android:layout_width="match_parent"
            android:layout_height="0dp"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toTopOf="parent"
            app:layout_constraintBottom_toTopOf="@+id/gallery_image_slide"
            android:layout_marginBottom="32dp"
            android:scaleType="fitXY"
            android:contentDescription="@string/app_name" />
    
        <Gallery
            android:id="@+id/gallery_image_slide"
            android:layout_width="match_parent"
            android:layout_height="100dp"
            android:animationDuration="2000"
            android:padding="10dp"
            android:spacing="5dp"
            android:unselectedAlpha="50"
            android:layout_marginBottom="32dp"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent" />
    
    </androidx.constraintlayout.widget.ConstraintLayout>
    ```
    

1. Activity File - `PracticialThree.kt`
    
    ```kotlin
    package `in`.three.one
    
    import android.os.Bundle
    import android.widget.Gallery
    import android.widget.ImageView
    import androidx.appcompat.app.AppCompatActivity
    import `in`.locate365.mvlucollege.R
    
    class PracticalThreeOne : AppCompatActivity() {
    
        private lateinit var gallery: Gallery
        private lateinit var adapter: ImageGalleryAdapter
        private lateinit var selectedImage: ImageView
    
        private var images = intArrayOf(
            R.drawable.img1,
            R.drawable.img2,
            R.drawable.img3,
            R.drawable.img4,
            R.drawable.img5,
            R.drawable.img6,
            R.drawable.img7,
            R.drawable.img8
        )
    
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            setContentView(R.layout.practical_three_one)
    
            gallery = findViewById(R.id.gallery_image_slide)
            selectedImage = findViewById(R.id.iv_show)
            adapter = ImageGalleryAdapter(this, images)
            gallery.adapter = adapter
    
            gallery.setOnItemClickListener { _, _, position, _ ->
                selectedImage.setImageResource(images[position])
            }
        }
    }
    ```
    
2. `imageGalleryAdapter.kt`
    
    ```kotlin
    package `in`.three.one
    
    import android.content.Context
    import android.view.View
    import android.view.ViewGroup
    import android.widget.BaseAdapter
    import android.widget.Gallery
    import android.widget.ImageView
    
    class ImageGalleryAdapter(private val context: Context, private val images: IntArray) : BaseAdapter() {
    
        // returns the number of images
        override fun getCount(): Int {
            return images.size
        }
    
        // returns the Item of an item
        override fun getItem(position: Int): Any {
            return position
        }
    
        // returns the ID of an item
        override fun getItemId(position: Int): Long {
            return position.toLong()
        }
    
        // returns an ImageView view
        override fun getView(position: Int, convertView: View?, parent: ViewGroup): View {
            // position argument will indicate the location of image
            // create a ImageView programmatically
            val imageView = ImageView(context)
    
            // set image in ImageView
            imageView.setImageResource(images[position])
    
            // set ImageView param
            imageView.layoutParams = Gallery.LayoutParams(200, 200)
            return imageView
        }
    }
    ```
    

## Output

