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
                /problem1
                    problem1.py
                    problem1.etc
                /problem2
                    problem2.py
                    problem2.etc
            Grader.exe
            /Problems
                problem1.pdf
                problem2.pdf
        */

        static void Main(string[] args) {
            // Setup necessary folders
            Setup();
            
            // Grade problems
            System.IO.DirectoryInfo answers = new System.IO.DirectoryInfo(Path.Combine(acm_folder, answer_folder));
            foreach (DirectoryInfo ans in answers.EnumerateDirectories()) {
                Console.WriteLine("Problem: {0}", ans.Name);

                System.IO.DirectoryInfo solutions = new System.IO.DirectoryInfo(Path.Combine(acm_folder, solution_folder, ans.Name));
                foreach (FileInfo file in solutions.EnumerateFiles()) {
                    Console.WriteLine("       + {0}", file.Name);
                }
            }
        }

        private static bool CreateFolder(string folder) {
            if (!Directory.Exists(folder)) {
                Directory.CreateDirectory(folder);
                if (DEBUG)
                    Console.WriteLine("Folder \"{0}\" created.", folder);
                return true;
            }
            else {
                if (DEBUG)
                    Console.WriteLine("Folder \"{0}\" already exists.", folder);
                return false;
            }
        }

        private static void Setup() {
            if (DEBUG)
                Console.WriteLine("Setup started.");

            int folders_created = 0;

            // Create necessary folders
            if (CreateFolder(Path.Combine(acm_folder, answer_folder)))
                folders_created++;
            if (CreateFolder(Path.Combine(acm_folder, problem_folder)))
                folders_created++;
            if (CreateFolder(Path.Combine(acm_folder, solution_folder)))
                folders_created++;

            // Create subdirectories in the Answers and Solutions folders for each pdf file in the Problems folder
            System.IO.DirectoryInfo problem_directory = new System.IO.DirectoryInfo(Path.Combine(acm_folder, problem_folder));
            foreach (FileInfo file in problem_directory.EnumerateFiles()) {
                if (file.Extension == ".pdf") {
                    if (CreateFolder(Path.Combine(acm_folder, answer_folder, Path.GetFileNameWithoutExtension(file.Name))))
                        folders_created++;
                    if (CreateFolder(Path.Combine(acm_folder, solution_folder, Path.GetFileNameWithoutExtension(file.Name))))
                        folders_created++;
                }
                else if (DEBUG)
                    Console.WriteLine("File found in Problems Directory that is not a PDF: {0}", file.Name);
            }

            if (DEBUG)
                Console.WriteLine("Created {0} folders. \nSetup Done", folders_created);
        }

    }
}
