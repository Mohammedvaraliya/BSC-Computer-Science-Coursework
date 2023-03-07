package com.example.gallery_application_pract_03_a

import android.os.Bundle
import android.widget.Gallery
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {


    private lateinit var gallery: Gallery
    private lateinit var adapter: ImageGalleryAdapter
    private lateinit var selectedImage: ImageView

    private var images = intArrayOf(
        R.drawable.image_1,
        R.drawable.image_2,
        R.drawable.image_3,
        R.drawable.image_4,
        R.drawable.image_5,
        R.drawable.image_6,
        R.drawable.image_7,
        R.drawable.image_8,
        R.drawable.image_9,
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        gallery = findViewById(R.id.gallery_image_slide)
        selectedImage = findViewById(R.id.iv_show)
        adapter = ImageGalleryAdapter(this, images)
        gallery.adapter = adapter

        gallery.setOnItemClickListener { _, _, position, _ ->
            selectedImage.setImageResource(images[position])
        }
    }
}