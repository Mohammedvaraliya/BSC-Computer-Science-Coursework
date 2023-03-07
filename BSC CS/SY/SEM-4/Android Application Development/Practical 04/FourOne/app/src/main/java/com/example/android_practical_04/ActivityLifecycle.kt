package com.example.android_practical_04

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class ActivityLifecycle: AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_life_cycle)
    }
}