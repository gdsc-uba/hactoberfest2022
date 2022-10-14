package condition;
import java.util.*;

public class fibonacciseriesss {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n,i,last=1,current,secondlast=0;
		Scanner sc=new Scanner(System.in);
		System.out.println("enter the number of terms in fibonnacci series");
		n=sc.nextInt();
		for(i=0;i<n;i++) {
			if(i<2) {
				current=i;
			}
			else {
				current=last+secondlast;
				secondlast=last;
				last=current;
			}
			System.out.print(current+" ");
		}

	}

}
