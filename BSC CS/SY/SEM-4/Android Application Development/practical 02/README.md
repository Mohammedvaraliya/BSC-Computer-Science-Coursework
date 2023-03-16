#### Aim: 
        i. Create an Android application to design screens using different layouts and UI including Button, Edittext, Textview, Radio Button etc.
        ii. Write an android application demonstrating response to event/user interaction for
            a. Checkbox
            b. Radio button
            c. Button
            d. Spinner

1. Layout file - `practical_two.xml`
    
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        android:layout_width="match_parent"
        android:layout_height="match_parent">
    
        <EditText
            android:id="@+id/et_first_name"
            android:layout_width="match_parent"
            android:layout_height="@android:dimen/app_icon_size"
            android:layout_marginStart="16dp"
            android:layout_marginTop="56dp"
            android:layout_marginEnd="16dp"
            android:hint="@string/first_name"
            android:inputType="text"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toTopOf="parent" />
    
        <EditText
            android:id="@+id/et_last_name"
            android:layout_width="match_parent"
            android:layout_height="@android:dimen/app_icon_size"
            android:layout_marginStart="16dp"
            android:layout_marginTop="16dp"
            android:layout_marginEnd="16dp"
            android:hint="@string/last_name"
            android:inputType="text"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toBottomOf="@+id/et_first_name" />
    
        <RadioGroup
            android:id="@+id/rg_gender"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginStart="16dp"
            android:layout_marginTop="16dp"
            android:layout_marginEnd="16dp"
            android:checkedButton="@id/rb_male"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toBottomOf="@+id/et_last_name">
    
            <RadioButton
                android:id="@+id/rb_male"
                android:layout_width="match_parent"
                android:layout_height="match_parent"
                android:text="@string/male"
                android:textSize="16sp" />
    
            <RadioButton
                android:id="@+id/rb_female"
                android:layout_width="match_parent"
                android:layout_height="match_parent"
                android:text="@string/female"
                android:textSize="16sp" />
        </RadioGroup>
    
        <CheckBox
            android:id="@+id/cb_age_check"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginStart="16dp"
            android:layout_marginTop="16dp"
            android:layout_marginEnd="16dp"
            android:gravity="start|center"
            android:text="@string/are_you_18"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toBottomOf="@+id/rg_gender" />
    
        <Spinner
            android:id="@+id/spinner_hobbies"
            android:layout_width="match_parent"
            android:layout_height="@android:dimen/app_icon_size"
            android:layout_marginStart="16dp"
            android:layout_marginTop="16dp"
            android:layout_marginEnd="16dp"
            android:entries="@array/hobbies"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toBottomOf="@+id/cb_age_check"/>
    
        <Button
            android:id="@+id/btn_save"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginStart="16dp"
            android:layout_marginTop="32dp"
            android:layout_marginEnd="16dp"
            android:text="@string/save"
            android:textSize="22sp"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toBottomOf="@+id/spinner_hobbies"/>
    
    </androidx.constraintlayout.widget.ConstraintLayout>
    ```
    

1. Activity File - `PracticialTwo.kt`
    
    ```kotlin
    package com.example.android_practical_02
    
    import android.os.Bundle
    import android.widget.Button
    import android.widget.CheckBox
    import android.widget.EditText
    import android.widget.RadioGroup
    import android.widget.Spinner
    import android.widget.Toast
    import androidx.appcompat.app.AppCompatActivity
    
    class PracticalTwo : AppCompatActivity() {
        private lateinit var etFirstName: EditText
        private lateinit var etLastName: EditText
        private lateinit var rgGender: RadioGroup
        private lateinit var cbAgeCheck: CheckBox
        private lateinit var spinnerHobbies: Spinner
        private lateinit var btnSave: Button
        private var isMale: Boolean = true
        private var areYou18: Boolean = false
    
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            setContentView(R.layout.practical_two)
            initComponent()
            onClick()
        }
    
        private fun onClick() {
    
            rgGender.setOnCheckedChangeListener { _, checkedId ->
                /*if (checkedId == R.id.rb_male) {
                    isMale = true
                } else if (checkedId == R.id.rb_female) {
                    isMale = false
                }*/
                when (checkedId) {
                    R.id.rb_male -> isMale = true
                    R.id.rb_female -> isMale = false
                }
            }
    
            cbAgeCheck.setOnCheckedChangeListener { _, isChecked ->
                areYou18 = isChecked
            }
    
            btnSave.setOnClickListener {
                val builder: StringBuilder = StringBuilder("First Name: ")
                builder.append(etFirstName.text.toString()).append("\n")
                builder.append(" Last Name: ")
                builder.append(etLastName.text.toString()).append("\n")
                builder.append(" Gender: ")
                builder.append(if (isMale) "Male" else "Female").append("\n")
                builder.append(" Are you 18+: ")
                builder.append(if (areYou18) "Yes" else "No").append("\n")
                builder.append(" Hobbies: ")
                builder.append(spinnerHobbies.selectedItem.toString())
    
                Toast.makeText(this,builder.toString(),Toast.LENGTH_SHORT).show()
            }
        }
    
        private fun initComponent() {
            etFirstName = findViewById(R.id.et_first_name)
            etLastName = findViewById(R.id.et_last_name)
            rgGender = findViewById(R.id.rg_gender)
            cbAgeCheck = findViewById(R.id.cb_age_check)
            spinnerHobbies = findViewById(R.id.spinner_hobbies)
            btnSave = findViewById(R.id.btn_save)
        }
    
    }
    ```
    
2. Adding the layout to the `manifest.xml`
    
    ```kotlin
    <activity android:name=".two.PracticalTwo"/>
    ```
    

## Output

### Overview

![Frame 3](https://user-images.githubusercontent.com/95087498/221181553-f2dc0d31-df06-4cfa-8035-82889d5bc03f.png)


