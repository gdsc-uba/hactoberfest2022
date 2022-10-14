package condition;
import java.util.*;

public class armstrongni {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int sum=0;
		Scanner sc=new Scanner(System.in);
		System.out.println("enter the numbers");
		int n=sc.nextInt();
		int temp=n;
		while(n>0) {
			int r=n%10;
			sum=sum+(r*r*r);
			n=n/10;
			
		}
		if(sum==temp) {
			System.out.println("armstrong number");
		}
		else {
			System.out.println("not a armstrong numbers");
		}

	}

}
