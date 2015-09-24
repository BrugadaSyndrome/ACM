//#define DEBUG

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
        //static bool DEBUG = true;

        static String[] Program_Folders = new String[] { "Problems" };
        static String[] Languages = new String[] { "Python" };

        static void Main(string[] args)
        {
            

            // Create necessary folders
            string acm_directory = Directory.GetCurrentDirectory();

            /*
            string problem_directory = Path.Combine(acm_directory, "..\\..\\..\\..\\Problems");
            CreateFolder(problem_directory);
            string python_solution_directory = Path.Combine(acm_directory, "..\\..\\..\\..\\Python_Solutions");
            CreateFolder(python_solution_directory);
            */

            // Grade problems
            /*
            System.IO.DirectoryInfo problems = new System.IO.DirectoryInfo(problem_directory);
            foreach (DirectoryInfo prob in problems.EnumerateDirectories())
            {
                Console.WriteLine("Problem Directories: {0}", prob.Name);
            }
            */

            /*
            System.IO.DirectoryInfo solutions = new System.IO.DirectoryInfo(python_solution_directory);
            foreach (FileInfo file in solutions.EnumerateFiles())
            {
                Console.WriteLine("Python File: {0}", file.Name);
            }
            */

            Console.WriteLine("Done grading problems.");
        }

        public static bool CreateFolder(string folder)
        {
            if (!Directory.Exists(folder))
            {
                Directory.CreateDirectory(folder);
                #if (DEBUG)
                    Console.WriteLine("Folder \"{0}\" created.", folder);
                #endif
                return true;
            }
            else
            {
                #if (DEBUG)
                    Console.WriteLine("Folder \"{0}\" already exists.", folder);
                #endif
                return false;
            }
        }

    }
}
