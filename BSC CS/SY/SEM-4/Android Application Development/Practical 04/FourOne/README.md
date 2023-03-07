Aim: ```Create an Android application to demonstrate implicit and explicit intents```

1. Layout file - `practical_four.xml`
    
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        xmlns:app="http://schemas.android.com/apk/res-auto">
    
        <androidx.appcompat.widget.AppCompatButton
            android:id="@+id/btn_implicit_call"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_margin="16dp"
            android:text="@string/call_user_directly"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toTopOf="parent"
            app:layout_constraintVertical_bias="0.3" />
    
        <androidx.appcompat.widget.AppCompatButton
            android:id="@+id/btn_implicit_dial"
            android:layout_margin="16dp"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="@string/call_user_via_dialpad"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintTop_toBottomOf="@+id/btn_implicit_call"/>
    
        <androidx.appcompat.widget.AppCompatButton
            android:id="@+id/btn_implicit_browser"
            android:layout_margin="16dp"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="@string/go_to_google_web_page"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintTop_toBottomOf="@+id/btn_implicit_dial"/>
    
        <androidx.appcompat.widget.AppCompatButton
            android:id="@+id/btn_home"
            android:layout_margin="16dp"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintEnd_toEndOf="parent"
            android:text="@string/go_to_home_page"
            app:layout_constraintTop_toBottomOf="@+id/btn_implicit_browser"/>
    
        <androidx.appcompat.widget.AppCompatButton
            android:id="@+id/btn_activity_lifecycle"
            android:layout_margin="16dp"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintEnd_toEndOf="parent"
            android:text="@string/go_to_activity_lifecycle"
            app:layout_constraintTop_toBottomOf="@+id/btn_home"/>
    
    </androidx.constraintlayout.widget.ConstraintLayout>
    ```

2. Layout file - `activity_life_cycle.xml`

    ```kotlin
    <?xml version="1.0" encoding="utf-8"?>
    <androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        android:layout_width="match_parent"
        android:layout_height="match_parent">

        <TextView
            android:id="@+id/textView2"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="This is Activity Life Cycle"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintHorizontal_bias="0.5"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toTopOf="parent" />

    </androidx.constraintlayout.widget.ConstraintLayout>
    ```


3. Layout file - `home_activity.xml`

    ```kotlin
    <?xml version="1.0" encoding="utf-8"?>
    <androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        android:layout_width="match_parent"
        android:layout_height="match_parent">

        <TextView
            android:id="@+id/textView"
            android:layout_width="142dp"
            android:layout_height="24dp"
            android:text="This is Home Activity"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toTopOf="parent" />
    </androidx.constraintlayout.widget.ConstraintLayout>
    ```


4. Activity file - `PracticalFourOne.kt`
    
    ```kotlin
    package com.example.android_practical_04

    import android.content.Intent
    import android.content.pm.PackageManager
    import android.net.Uri
    import android.os.Bundle
    import androidx.appcompat.app.AppCompatActivity
    import androidx.appcompat.widget.AppCompatButton
    import androidx.core.app.ActivityCompat
    import androidx.core.content.ContextCompat
    import com.example.android_practical_04.HomeActivity
    import com.example.android_practical_04.R
    import com.example.android_practical_04.ActivityLifecycle


    class MainActivity : AppCompatActivity() {

        private lateinit var buttonCall: AppCompatButton
        private lateinit var buttonDial: AppCompatButton
        private lateinit var buttonBrowser: AppCompatButton
        private lateinit var buttonHome: AppCompatButton
        private lateinit var buttonActivityLifeCycle: AppCompatButton

        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            setContentView(R.layout.activity_main)
            buttonCall = findViewById(R.id.btn_implicit_call)
            buttonDial = findViewById(R.id.btn_implicit_dial)
            buttonBrowser = findViewById(R.id.btn_implicit_browser)
            buttonHome = findViewById(R.id.btn_home)
            buttonActivityLifeCycle = findViewById(R.id.btn_activity_lifecycle)


            this.buttonCall.setOnClickListener{
                if (ContextCompat.checkSelfPermission(this,android.Manifest.permission.CALL_PHONE) != PackageManager.PERMISSION_GRANTED) {
                    ActivityCompat.requestPermissions(this, arrayOf(android.Manifest.permission.CALL_PHONE),100)
                } else {
                    val intent = Intent(Intent.ACTION_CALL, Uri.parse("tel:" + "+91123456789"))
                    startActivity(intent)
                }
            }

            buttonDial.setOnClickListener{
                val intent = Intent(Intent.ACTION_DIAL, Uri.parse("tel:" + "+91123456789"))
                startActivity(intent)
            }

            buttonBrowser.setOnClickListener{
                val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://www.google.co.in/"))
                startActivity(intent)
            }

            buttonHome.setOnClickListener{
                val intent = Intent(this,HomeActivity::class.java)
                startActivity(intent)
            }

            buttonActivityLifeCycle.setOnClickListener{
                val intent = Intent(this,ActivityLifecycle::class.java)
                startActivity(intent)
            }
        }
    }
    ```


5. Activity file - `HomeActivity.kt`

    ```kotlin
    package com.example.android_practical_04

    import android.os.Bundle
    import androidx.appcompat.app.AppCompatActivity

    class HomeActivity : AppCompatActivity() {

        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            setContentView(R.layout.home_activity)
        }
    }
    ```


6. Activity file - `ActivityLifeCycle.kt`

    ```kotlin
    package com.example.android_practical_04

    import android.os.Bundle
    import androidx.appcompat.app.AppCompatActivity

    class ActivityLifecycle: AppCompatActivity() {

        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            setContentView(R.layout.activity_life_cycle)
        }
    }
    ```

    

## Output


![Frame 9](https://user-images.githubusercontent.com/95087498/223484494-4ec3529a-bdd5-4ec5-a747-fd604d8d68ad.png)

![Frame 10](https://user-images.githubusercontent.com/95087498/223484520-327f32e4-0ca5-469e-8cea-b404901cbdc6.png)

![Frame 11](https://user-images.githubusercontent.com/95087498/223484575-3a7356e9-6fba-4a39-a264-1c4d8f05ce02.png)


