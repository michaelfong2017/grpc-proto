package com.michael.fileupload;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;

import androidx.test.platform.app.InstrumentationRegistry;
import androidx.test.ext.junit.runners.AndroidJUnit4;

import com.google.protobuf.ByteString;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.junit.runner.RunWith;
import org.mockito.MockedStatic;
import org.mockito.Mockito;
import org.mockito.junit.jupiter.MockitoExtension;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.Arrays;

import io.grpc.michael.fileupload.*;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.stub.StreamObserver;

@RunWith(AndroidJUnit4.class)
@ExtendWith(MockitoExtension.class)
public class FileUploadTest {
    private ManagedChannel channel;
    private FileServiceGrpc.FileServiceStub fileServiceStub;

    @Before
    public void setup() {
        this.channel = ManagedChannelBuilder.forAddress("localhost", 50051)
                .usePlaintext()
                .build();
        this.fileServiceStub = FileServiceGrpc.newStub(channel);
    }

    @Test
    public void unaryServiceTest() throws InterruptedException, IOException {
        Context context = InstrumentationRegistry.getInstrumentation().getTargetContext();

        StreamObserver<FileUploadRequest> streamObserver = this.fileServiceStub.upload(new FileUploadObserver());

        // build metadata
        FileUploadRequest metadata = FileUploadRequest.newBuilder()
                .setMetadata(MetaData.newBuilder()
                        .setName("output")
                        .setType("png").build())
                .build();
        streamObserver.onNext(metadata);


        try (MockedStatic<BitmapFactory> mockedStatic = Mockito.mockStatic(BitmapFactory.class)) {
            mockedStatic.when(() -> BitmapFactory.decodeResource(null, -1)).thenReturn(null);

            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            Bitmap bm = BitmapFactory.decodeResource(context.getResources(), R.raw.test);
            bm.compress(Bitmap.CompressFormat.PNG, 100, baos);

            byte[] bytes = baos.toByteArray();

            System.out.println(bytes.length);
        }


        ByteArrayOutputStream baos = new ByteArrayOutputStream();
//        Bitmap bm = BitmapFactory.decodeStream(fis);
//        bm.compress(Bitmap.CompressFormat.PNG, 100, baos);

        byte[] bytes = baos.toByteArray();

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

    @After
    public void teardown() {
        this.channel.shutdown();
    }

    private static class FileUploadObserver implements StreamObserver<FileUploadResponse> {
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
}
