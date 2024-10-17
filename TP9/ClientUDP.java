import java.io.*;
import java.net.*;

public class ClientUDP
{
	public static void main( String[] args ) throws IOException
	{
		String s="Hello World";
		byte [ ] data = s . getBytes ();
		InetAddress addr = InetAddress.getLocalHost();
		System.out.println("adresse=" +addr.getHostName());
		DatagramPacket packet = new DatagramPacket (data, data.length, addr, 1234);
		DatagramSocket sock = new DatagramSocket();
		sock.send(packet);
		sock.close();
	}
}
