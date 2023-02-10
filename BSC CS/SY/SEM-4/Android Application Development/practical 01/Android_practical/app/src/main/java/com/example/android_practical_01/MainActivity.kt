package com.example.android_practical_01

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast

class MainActivity : AppCompatActivity() {
    lateinit var etUserName:EditText
    lateinit var etPassword:EditText
    lateinit var btnLogin:Button


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        etUserName = findViewById(R.id.et_user_name)
        etPassword = findViewById(R.id.et_password)
        btnLogin = findViewById(R.id.btn_login)

        if(etUserName.text.toString().equals(etPassword.text.toString())){
            Toast.makeText(this,"successfully login!",Toast.LENGTH_SHORT).show()
        }
        else{
            Toast.makeText(this,"Login Unsuccessfully!",Toast.LENGTH_SHORT).show()
        }

    }


}
