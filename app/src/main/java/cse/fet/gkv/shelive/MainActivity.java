package cse.fet.gkv.shelive;

import android.app.Activity;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

public class MainActivity extends Activity {
    TextView t1,t2,t3,tr;
    EditText e1,e2,e3;
    Button b1,b2;
    String[] sr,dr;
    float[][] f= new float[10][3];
    int i=0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        sr= new String[]{"radius", "texture", "perimeter", "area", "smoothness", "compactness", "concavity", "concave points", "symmetry", "fractal dimension"};
        dr= new String[]{"_mean", "_se", "_worst"};
        t1=findViewById(R.id.tv1);
        t2=findViewById(R.id.tv2);
        tr=findViewById(R.id.tvr);
        t3=findViewById(R.id.tv3);
        e1=findViewById(R.id.et1);
        e2=findViewById(R.id.et2);
        e3=findViewById(R.id.et3);
        b1=findViewById(R.id.button);
        b2=findViewById(R.id.button2);
        set(i);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(i<10){
                    f[i][0]=Float.parseFloat(e1.getText().toString());
                    f[i][1]=Float.parseFloat(e2.getText().toString());
                    f[i][2]=Float.parseFloat(e3.getText().toString());
                    e1.setText("");
                    e2.setText("");
                    e3.setText("");
                    set(++i);
                    if(i==9){
                        b2.setClickable(true);
                        b1.setClickable(false);
                    }
                }
            }
        });
        b2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try {
                    Socket s=new Socket("13.233.225.36",50000);
                    OutputStream os=s.getOutputStream();
                    DataOutputStream ds=new DataOutputStream(os);
                    StringBuilder ln=new StringBuilder();
                    for (int j = 0; j <3 ; j++)
                        for (int k = 0; k <10 ; k++)
                        ln.append(f[k][j]+",");

                    ds.writeUTF(ln.toString());

                    InputStream is=s.getInputStream();
                    DataInputStream d=new DataInputStream(is);
                    tr.setText(d.readUTF());
                    s.close();
                }
                catch (Exception e){
                    e.printStackTrace();
                }
            }
        });
    }
    private void set(int i){
        if(i==10)
            return;
        t1.setText(sr[i]+dr[0]);
        t2.setText(sr[i]+dr[1]);
        t3.setText(sr[i]+dr[2]);
    }
}
