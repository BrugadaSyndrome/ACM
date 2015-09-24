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
        static private bool DEBUG = false;
        static private string acm_folder = Directory.GetCurrentDirectory();
        static private string answer_folder = "Answers";
        static private string problem_folder = "Problems";
        static private string solution_folder = "Solutions";
        static private string[] languages = new string[] { "Python", "C++" };

        /*
            /Answers
                /problem1
                    problem1-1.in
                    problem1-1.out
                    problem1-2.in
                    problem1-2.out
                /problem2
                    problem2-1.in
                    problem2-1.out
                    problem2-2.in
                    problem2-2.out
            /Solutions
                /Language1
                    problem1.???
                /Language2
                    problem2.???
            Grader.exe
            /Problems
                problem1.pdf
                problem2.pdf
        */

        static void Main(string[] args)
        {
            // Setup necessary folders
            Setup();
            
            // Grade problems
            System.IO.DirectoryInfo problems = new System.IO.DirectoryInfo(Path.Combine(acm_folder, problem_folder));
            foreach (DirectoryInfo prob in problems.EnumerateDirectories())
            {
                Console.WriteLine("Problem Directories: {0}", prob.Name);
            }

            /*
            System.IO.DirectoryInfo solutions = new System.IO.DirectoryInfo(python_solution_directory);
            foreach (FileInfo file in solutions.EnumerateFiles())
            {
                Console.WriteLine("Python File: {0}", file.Name);
            }
            */


        }

        private static bool CreateFolder(string folder)
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

        private static void Setup()
        {
            if (DEBUG)
                Console.WriteLine("Setup started.");

            int files_created = 0;

            // Create necessary folders
            if (CreateFolder(Path.Combine(acm_folder, answer_folder))) files_created++;
            if (CreateFolder(Path.Combine(acm_folder, problem_folder))) files_created++;
            if (CreateFolder(Path.Combine(acm_folder, solution_folder))) files_created++;

            // Create a sub-directory for each item in languages[]
            foreach (string folder in languages)
            {
                if (CreateFolder(Path.Combine(acm_folder, "Solutions", folder))) files_created++;
            }

            // Create a sub-directory in answers for each problem.pdf file in the Problems folder
            System.IO.DirectoryInfo problem_directory = new System.IO.DirectoryInfo(Path.Combine(acm_folder, "Problems"));
            foreach (FileInfo file in problem_directory.EnumerateFiles())
            {
                if (file.Extension == ".pdf")
                {
                    if (CreateFolder(Path.Combine(acm_folder, answer_folder, Path.GetFileNameWithoutExtension(file.Name)))) files_created++;
                }
                else if (DEBUG)
                    Console.WriteLine("File found in Problems Directory that is not a PDF: {0}", file.Name);
            }

            Console.WriteLine("Setup Done. Created {0} folders.", files_created);
        }

    }
}
