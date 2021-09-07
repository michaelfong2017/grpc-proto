package com.michael.fileupload;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.util.Log;

import com.google.protobuf.ByteString;

import java.io.ByteArrayOutputStream;
import java.util.Arrays;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.michael.fileupload.File;
import io.grpc.michael.fileupload.FileServiceGrpc;
import io.grpc.michael.fileupload.FileUploadRequest;
import io.grpc.michael.fileupload.FileUploadResponse;
import io.grpc.michael.fileupload.MetaData;
import io.grpc.stub.StreamObserver;

public class MainActivity extends AppCompatActivity {
    private ManagedChannel channel;
    private FileServiceGrpc.FileServiceStub fileServiceStub;

    public void setup(){
        this.channel = ManagedChannelBuilder.forAddress("localhost", 50051)
                .usePlaintext()
                .build();
        this.fileServiceStub = FileServiceGrpc.newStub(channel);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        setup();

        StreamObserver<FileUploadRequest> streamObserver = this.fileServiceStub.upload(new FileUploadObserver());

        // build metadata
        FileUploadRequest metadata = FileUploadRequest.newBuilder()
                .setMetadata(MetaData.newBuilder()
                        .setName("output")
                        .setType("png").build())
                .build();
        streamObserver.onNext(metadata);

        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        Bitmap bm = BitmapFactory.decodeResource(getResources(), R.raw.test);
        bm.compress(Bitmap.CompressFormat.PNG, 100, baos);

        byte[] bytes = baos.toByteArray();

        Log.d("test", "bytes " + bytes.length);

        int chunkSize = 4096;
        int remaining = bytes.length;
        int to;

        do {
            if (remaining < chunkSize) {
                to = bytes.length;
            } else {
                to = bytes.length - remaining + chunkSize;
            }
            FileUploadRequest uploadRequest = FileUploadRequest.newBuilder()
                    .setFile(File.newBuilder().setContent(ByteString.copyFrom(Arrays.copyOfRange(bytes, bytes.length - remaining, to))).build())
                    .build();
            streamObserver.onNext(uploadRequest);
        } while ((remaining = remaining - chunkSize) > 0);

        streamObserver.onCompleted();
    }
}

class FileUploadObserver implements StreamObserver<FileUploadResponse> {

    @Override
    public void onNext(FileUploadResponse fileUploadResponse) {
        System.out.println(
                "File upload status :: " + fileUploadResponse.getStatus()
        );
    }

    @Override
    public void onError(Throwable throwable) {

    }

    @Override
    public void onCompleted() {

    }

}