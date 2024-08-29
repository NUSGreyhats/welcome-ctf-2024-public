package com.greyhats.skibidi.toilet;

import static android.provider.Contacts.SettingsColumns.KEY;

import android.util.Base64;
import android.util.Log;

import java.nio.charset.StandardCharsets;
import java.security.InvalidAlgorithmParameterException;
import java.security.InvalidKeyException;
import java.security.Key;
import java.security.NoSuchAlgorithmException;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
public class Rizz {
    private static String KEY_STRING = "zsfuxwCqcUOfaXNhHxYvJfPIOEoPMiyL";
    private static String IV = "W644i2IVQjBBeth9";
    private static String RIZZ = "D7NQV/ledSLBd0zF11CPuPAz8y6D8kt/rQ4j5vNOWhFrlwjMsb40Hg4pEhoeVf3s";

    public static boolean do_you_have_rizz(String msg) {
        return encrypt(msg).equals(RIZZ);
    }
    public static String encrypt(String message) {
        try {
            byte[] srcBuff = message.getBytes(StandardCharsets.UTF_8);
            SecretKeySpec skeySpec = new SecretKeySpec(KEY_STRING.getBytes(), "AES");
            IvParameterSpec ivSpec = new IvParameterSpec(IV.getBytes());
            Cipher cipher = null;
            cipher = Cipher.getInstance("AES/CBC/PKCS7Padding");
            cipher.init(Cipher.ENCRYPT_MODE, skeySpec, ivSpec);
            return Base64.encodeToString(cipher.doFinal(srcBuff), Base64.NO_WRAP);

        } catch (NoSuchAlgorithmException | IllegalBlockSizeException | NoSuchPaddingException |
                 BadPaddingException | InvalidKeyException| InvalidAlgorithmParameterException e) {
            throw new RuntimeException(e);
        }

    }
//    public static String decrypt(String encrypted){
//        try {
//            SecretKeySpec skeySpec = new SecretKeySpec(KEY_STRING.getBytes(), "AES");
//            IvParameterSpec ivSpec = new IvParameterSpec(IV.getBytes());
//            Cipher cipher = Cipher.getInstance("AES/CBC/PKCS7Padding");
//            cipher.init(Cipher.DECRYPT_MODE, skeySpec, ivSpec);
//            byte[] raw = Base64.decode(encrypted, Base64.NO_WRAP);
//            return new String(cipher.doFinal(raw), StandardCharsets.UTF_8);
//        } catch (NoSuchAlgorithmException | IllegalBlockSizeException | NoSuchPaddingException |
//        BadPaddingException | InvalidKeyException| InvalidAlgorithmParameterException e) {
//            throw new RuntimeException(e);
//        }
//    }
}