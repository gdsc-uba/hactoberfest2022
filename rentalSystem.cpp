# include <iostream>
# include <conio.h>
# include <string>

using namespace std;

int main()
{
	int kamar,harga,lama,bayar;
	string nkamar;
	
	cout<<"RENTAL SYSTEM INFORMATION"<<endl;
	cout<<endl;
	cout<<"No  Type_of_room  Price " <<endl;
	cout<<"1.   Family      Rp: 500.000 "<<endl;
	cout<<"2.   Dulux       Rp: 1.000.000 "<<endl;
	cout<<"3.   Rose        Rp: 1.500.000 "<<endl;
	cout<<"**************"<<endl;
	cout<<endl;
	
	cout<<"Choose Room Type :";
	cin>>kamar;
	if(kamar==1)
	{
		harga = 500000;
		nkamar= "Family";
	}
    else if (kamar==2)
    {
    	harga = 1000000;
    	nkamar= "Dulux";
	}
	else if (kamar==3)
	{
		harga = 1500000;
		nkamar= "Rose";
	}
	
	cout<< " The room you choose is " << kamar << " at a price of Rp = "<< harga <<"/day"<<endl;
	cout<< "How long do you want to rent the room : ";
	cin>>lama;
	bayar = lama*harga;
	
	cout<<endl;
	cout<< " Your preferred type of room : "<< nkamar <<endl;
	cout<< " Your rental period "<< lama <<"hari"<<endl;
	cout<< " The total rental price you have to pay is Rp :"<< bayar <<endl;
    getch();
}

