package be.desmottes.mangerveggie;

import android.Manifest;
import android.app.Activity;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AlertDialog;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.Window;
import android.view.WindowManager;
import android.webkit.ConsoleMessage;
import android.webkit.GeolocationPermissions;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;

import vegout.desmottes.be.vegout.BuildConfig;
import vegout.desmottes.be.vegout.R;


public class MainActivity extends Activity implements ActivityCompat.OnRequestPermissionsResultCallback {

    private WebView webView;
    //these fields are needed to work around the new permission system in android 6
//    private GeolocationPermissions.Callback geoPermCallback = null;
//    private String origin;
    final int GEOLOC_PERM_REQUEST_CODE = 123;
    //end of workaround


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        //Remove title bar
        this.requestWindowFeature(Window.FEATURE_NO_TITLE);

        //Remove notification bar
        this.getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);

        setContentView(R.layout.activity_main);
        webView = (WebView) findViewById(R.id.activity_main_webView);
        // Enable Javascript
        WebSettings webSettings = webView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        webSettings.setGeolocationEnabled(true);
        webSettings.setLoadWithOverviewMode(true);
        webSettings.setUseWideViewPort(true);
        webSettings.setJavaScriptCanOpenWindowsAutomatically(true);
        webSettings.setAppCacheEnabled(false);

        webSettings.setDomStorageEnabled(true);
        webSettings.setDatabaseEnabled(true);
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.KITKAT) {
            webSettings.setDatabasePath("/data/data/" + webView.getContext().getPackageName() + "/databases/");
        }
        webSettings.setUserAgentString(webSettings.getUserAgentString() + " " + getString(R.string.app_name));


        webView.setWebChromeClient(new WebChromeClient() {
            public void onGeolocationPermissionsShowPrompt(String origin, GeolocationPermissions.Callback callback) {
                boolean hasGeolocPermission = PackageManager.PERMISSION_GRANTED ==
                        ContextCompat.checkSelfPermission(MainActivity.this,
                        Manifest.permission.ACCESS_FINE_LOCATION);

                if (!hasGeolocPermission) {
                    /*if (!ActivityCompat.shouldShowRequestPermissionRationale(MainActivity.this,
                            Manifest.permission.ACCESS_FINE_LOCATION)) {
                        showMessageOKCancel("Nous avons besoin de votre position",
                                new DialogInterface.OnClickListener() {
                                    @Override
                                    public void onClick(DialogInterface dialog, int which) {
                                        ActivityCompat.requestPermissions(MainActivity.this,
                                                new String[] {Manifest.permission.ACCESS_FINE_LOCATION},
                                                GEOLOC_PERM_REQUEST_CODE);
                                    }
                                });
                        return;
                    } else*/
                    ActivityCompat.requestPermissions(MainActivity.this,
                            new String[] {Manifest.permission.ACCESS_FINE_LOCATION},
                            GEOLOC_PERM_REQUEST_CODE);
                    callback.invoke(origin, true, true);
                    return;
                }

                hasGeolocPermission = PackageManager.PERMISSION_GRANTED ==
                        ContextCompat.checkSelfPermission(MainActivity.this,
                                Manifest.permission.ACCESS_FINE_LOCATION);

                //MainActivity.this.origin = origin;
                //geoPermCallback = callback;
                //if(hasGeolocPermission)
                callback.invoke(origin, hasGeolocPermission, true);
            }

            public boolean onConsoleMessage(ConsoleMessage msg) {
                Log.w("mangerveggie", msg.sourceId() + "[" + msg.lineNumber() + "] " + msg.message());
                return true;
            }

            public void onConsoleMessage(String message, int lineNumber, String sourceID) {
                Log.w("MyApplication", message + " -- From line "
                        + lineNumber + " of "
                        + sourceID);
            }
        });
        webView.setWebViewClient(new CustomWebViewClient());
        webView.loadUrl(BuildConfig.HOST);
    }

    private void showMessageOKCancel(String message, DialogInterface.OnClickListener okListener) {
        new AlertDialog.Builder(MainActivity.this)
                .setMessage(message)
                .setPositiveButton("OK", okListener)
                .setNegativeButton("Cancel", null)
                .create()
                .show();
    }

    private class CustomWebViewClient extends WebViewClient {
        public boolean shouldOverrideUrlLoading(WebView view, String url) {
            if (url.startsWith("tel:")) {
                Intent intent = new Intent(Intent.ACTION_DIAL,
                        Uri.parse(url));
                startActivity(intent);
                return true;
            }

            boolean handleInWebview = url.contains(BuildConfig.LOCALCHECKSTRING);
            if (handleInWebview)
                view.loadUrl(url);
            //return true if this method handled the link event
            //or false otherwise
            return handleInWebview;
        }


    }

    @Override
    public void onBackPressed() {
        if (webView.canGoBack()) {
            webView.goBack();
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
/*    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        switch (requestCode) {
            case GEOLOC_PERM_REQUEST_CODE:
                if (grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                    if(geoPermCallback != null)
                        geoPermCallback.invoke(origin, true, true);
                } else {
                    // Permission Denied
                    Toast.makeText(MainActivity.this, "GEOLOC Permission Denied", Toast.LENGTH_SHORT)
                            .show();
                }
                break;
            default:
                super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        }
    }*/
}
