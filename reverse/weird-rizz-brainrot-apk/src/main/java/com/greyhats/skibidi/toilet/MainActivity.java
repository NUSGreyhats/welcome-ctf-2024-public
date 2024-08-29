package com.greyhats.skibidi.toilet;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.view.inputmethod.InputMethodManager;
import android.widget.ImageView;
import android.widget.Toast;

import com.google.android.material.textfield.TextInputEditText;
import com.bumptech.glide.Glide;

import java.util.Objects;


public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void onClickBtn(View v)
    {
        InputMethodManager imm = (InputMethodManager)getSystemService(Context.INPUT_METHOD_SERVICE);
        TextInputEditText pw = findViewById(R.id.password);
        ImageView imageView = findViewById(R.id.imageview);
        imm.hideSoftInputFromWindow(pw.getWindowToken(), 0);
        if (Rizz.do_you_have_rizz(Objects.requireNonNull(pw.getText()).toString())) {
            imageView.setVisibility(View.GONE);
            Toast.makeText(this, "skibidi", Toast.LENGTH_SHORT).show();
        } else {
            imageView.setVisibility(View.VISIBLE);
            Glide.with(this)
                    .asGif()
                    .load(R.raw.skibidi)
                    .fitCenter()
                    .centerCrop()
                    .into(imageView);
            Toast.makeText(this, "no rizz", Toast.LENGTH_SHORT).show();
        }
    }
}