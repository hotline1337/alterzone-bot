using System;
using System.IO;
using System.Net;
using System.Threading;

using Spectre.Console;

namespace alterzone_bot
{
    internal class Program
    {
        public static void Main()
        {
            AnsiConsole.MarkupLine("┌─── [mediumpurple4]ALTERZONE AIO[/] ─── Inicjalizacja...");
            ServicePointManager.Expect100Continue = true;
            ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
            var alterzone_link = "https://alterzone.pl/rejestracja";
            var limited_offer = false;

            new WebDriverManager.DriverManager(Path.GetTempPath()).SetUpDriver(new WebDriverManager.DriverConfigs.Impl.EdgeConfig());
            var user_input = AnsiConsole.Ask<string>("│    [mediumpurple4]ALTERZONE AIO[/] ─── Czy chcesz uzyc ref-linka do rejestracji? (tak/nie): ");
            switch (user_input.ToLower())
            {
                case "tak":
                {
                    user_input = AnsiConsole.Ask<string>("│    [mediumpurple4]ALTERZONE AIO[/] ─── Podaj link: ");
                    if (user_input.StartsWith("https://alterzone.pl/R/"))
                    {
                        alterzone_link = user_input;
                    }
                    else
                    {
                        AnsiConsole.MarkupLine("└─── [indianred]ALTERZONE AIO[/] ─── Niewlasciwy link");
                        Thread.Sleep(3000);
                        Environment.Exit(0);
                    }

                    break;
                }
                case "nie":
                    alterzone_link = "https://alterzone.pl/rejestracja";
                    break;
                default:
                    AnsiConsole.MarkupLine("└─── [indianred]ALTERZONE AIO[/] ─── Niewlasciwa opcja");
                    Thread.Sleep(3000);
                    Environment.Exit(0);
                    break;
            }

            user_input = AnsiConsole.Ask<string>("│    [mediumpurple4]ALTERZONE AIO[/] ─── Czy chcesz skorzystac z oferty limitowanej? (tak/nie): ");
            switch (user_input.ToLower())
            {
                case "tak":
                    limited_offer = true;
                    break;
                case "nie":
                    limited_offer = false;
                    break;
                default:
                    AnsiConsole.MarkupLine("└─── [indianred]ALTERZONE AIO[/] ─── Niewlasciwa opcja");
                    Thread.Sleep(3000);
                    Environment.Exit(0);
                    break;
            }

            var driver = new Driver.Driver(limited_offer);
            driver.Execute(alterzone_link).GetAwaiter().GetResult();
        }
    }
}
