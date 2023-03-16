package com.example.question_4

import android.media.MediaPlayer
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button

class MainActivity : AppCompatActivity() {

    lateinit var btnStop: Button
    lateinit var btnPlay : Button
    lateinit var btnPause: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        initComponent()
        initClick()
    }

    private fun initComponent() {
        btnStop = findViewById(R.id.btn_stop)
        btnPlay = findViewById(R.id.btn_play)
        btnPause = findViewById(R.id.btn_pause)
    }

    private fun initClick() {
        val mediaPlayer: MediaPlayer = MediaPlayer.create(applicationContext, R.raw.animals_matrin_garrix)

        btnStop.setOnClickListener{
            mediaPlayer.stop()
            mediaPlayer.prepare()
        }

        btnPlay.setOnClickListener{
            mediaPlayer.start()
        }

        btnPause.setOnClickListener{
            mediaPlayer.pause()
        }
    }
}