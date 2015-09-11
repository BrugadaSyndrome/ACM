using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Grader
{
    class Program
    {
        static bool DEBUG = true;

        static void Main(string[] args)
        {
            // Create problem folder if it does not exist
            string acm_directory = Directory.GetCurrentDirectory();
            string problem_directory = Path.Combine(acm_directory, "..\\..\\..\\Problems");
            CreateFolder(problem_directory);

            // Grade problems
            System.IO.DirectoryInfo problems = new System.IO.DirectoryInfo(problem_directory);
            foreach (DirectoryInfo prob in problems.EnumerateDirectories())
            {
                Console.WriteLine("Problem: {0}", prob.Name);
            }

            Console.WriteLine("Done grading problems.");
        }

        public static bool CreateFolder(string folder)
        {
            if (!Directory.Exists(folder))
            {
                Directory.CreateDirectory(folder);
                if (DEBUG)
                    Console.WriteLine("Folder \"{0}\" created.", folder);
                return true;
            }
            else
            {
                if (DEBUG)
                    Console.WriteLine("Folder \"{0}\" already exists.", folder);
                return false;
            }
        }

    }
}
