import java.io.*;
import java.net.*;

public class ServeurTCP3
{
	public static void main(String[] args)
	{
		try 
		{
			// ServeurTCP1.java
			ServerSocket socketserver = new ServerSocket (2016);
			while(true)
			{
				System.out.println("serveur en attente");
				Socket socket = socketserver.accept();
				System.out.println("Connection d'un client");
				DataInputStream dIn = new DataInputStream (socket.getInputStream());
				String msg = dIn.readUTF();
				System.out.println("Message: " + msg);
				String rev = new StringBuilder(msg).reverse().toString();
				DataOutputStream dOut= new DataOutputStream (socket.getOutputStream());
				dOut.writeUTF(rev);
				socket.close();
			}
			//socketserver.close();
		}
		catch (Exception ex) 
		{
			System.out.println("Erreur: ");
		}
	}
}

