using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Practical_1b_Currency.ServiceReference_Currency;

namespace Practical_1b_Currency
{
    internal class Program
    {
        static void Main(string[] args)
        {
            CurrencyConverterClient client = new CurrencyConverterClient(); ;
            Console.WriteLine("Enter the currency in Indian Rupees: ");
            double result = double.Parse(Console.ReadLine());
            Console.WriteLine(client.InrtoDollar(result));
            Console.ReadLine();
        }
    }
}
