using System;
using System.IO;
using System.Text.RegularExpressions;
using System.Threading;
using System.Threading.Tasks;

using OpenQA.Selenium;
using OpenQA.Selenium.Edge;
using OpenQA.Selenium.Support.UI;
using SeleniumExtras.WaitHelpers;

using TempMail;
using RandomDataGenerator.Randomizers;
using RandomDataGenerator.FieldOptions;
using System.Linq;
using Spectre.Console;

#pragma warning disable 1998

namespace Driver
{
    internal class Driver
    {
        private bool limited_offer = false;
        private int counter = 0;

        private readonly EdgeOptions options = new EdgeOptions();
        private readonly EdgeDriverService service = EdgeDriverService.CreateDefaultService();

        public Driver(bool limited_offer = false)
        {
            this.limited_offer = limited_offer;
            this.options.AddExcludedArgument("enable-logging");
            foreach (var argument in new[] { 
                "--headless", "--disable-extensions", "--disable-logging", "--log-level=3" 
            })
            {
                this.options.AddArgument(argument);
            }
            this.service.SuppressInitialDiagnosticInformation = true;
            this.service.EnableVerboseLogging = false;

            AnsiConsole.MarkupLine("│    [mediumpurple4]ALTERZONE AIO[/] ─── Usluga utworzona");
            AnsiConsole.MarkupLine("│    [mediumpurple4]ALTERZONE AIO[/] ─── Generowanie kodow, to moze chwile potrwac...");
        }

        private async Task<string> GenerateEmail()
        {
            using (var mail = new TemporaryMail())
            {
                return await mail.GenerateRandomMailbox();
            }
        }

        private async Task<string> GetEmailBody(string mailbox)
        {
            using (var mail = new TemporaryMail())
            {
                var email = await mail.WaitForEmail(mailbox,
                    x => x.subject.Contains("konto")
                );
                return email.body;
            }
        }

        private async Task GetPoints(EdgeDriver driver, WebDriverWait wait)
        {
            try
            {
                /* Nowy Rok z Alter Zone */
                driver.Url = "https://alterzone.pl/aktywnosci/styczen1_2023/gra";
                wait.Until(ExpectedConditions.ElementExists(By.XPath("//*[@id=\"root\"]/div/div[2]/div/div/section/div[2]/div/div/div[4]")));
                var prawda = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[2]/div/div/section/div[2]/div/div/div[4]/button[1]"));
                var falsz = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[2]/div/div/section/div[2]/div/div/div[4]/button[2]"));
                var dalej = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[2]/div/div/section/div[2]/div/div/button"));
                /* Pytanie 1 */
                driver.ExecuteScript("arguments[0].click();", prawda);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 2 */
                driver.ExecuteScript("arguments[0].click();", falsz);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 3 */
                driver.ExecuteScript("arguments[0].click();", prawda);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 4 */
                driver.ExecuteScript("arguments[0].click();", prawda);
                driver.ExecuteScript("arguments[0].click();", dalej);

                /* 7 błędów głównych */
                driver.Url = "https://alterzone.pl/aktywnosci/styczen4_2023/gra";
                prawda = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[2]/div/div/section/div[2]/div/div/div[4]/button[1]"));
                falsz = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[2]/div/div/section/div[2]/div/div/div[4]/button[2]"));
                dalej = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[2]/div/div/section/div[2]/div/div/button"));
                /* Pytanie 1 */
                driver.ExecuteScript("arguments[0].click();", falsz);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 2 */
                driver.ExecuteScript("arguments[0].click();", prawda);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 3 */
                driver.ExecuteScript("arguments[0].click();", falsz);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 4 */
                driver.ExecuteScript("arguments[0].click();", prawda);
                driver.ExecuteScript("arguments[0].click();", dalej);

                /* Subskrypcja neo™ */
                driver.Url = "https://alterzone.pl/aktywnosci/luty1_2023/gra";
                prawda = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[2]/div/div/section/div[2]/div/div/div[4]/button[1]"));
                falsz = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[2]/div/div/section/div[2]/div/div/div[4]/button[2]"));
                dalej = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[2]/div/div/section/div[2]/div/div/button"));
                /* Pytanie 1 */
                driver.ExecuteScript("arguments[0].click();", falsz);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 2 */
                driver.ExecuteScript("arguments[0].click();", falsz);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 3 */
                driver.ExecuteScript("arguments[0].click();", falsz);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 4 */
                driver.ExecuteScript("arguments[0].click();", prawda);
                driver.ExecuteScript("arguments[0].click();", dalej);

                /* Poznaj warianty smakowe neo™ */
                driver.Url = "https://alterzone.pl/aktywnosci/luty2_2023/gra";
                prawda = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[2]/div/div/section/div[2]/div/div/div[2]/div[2]/button[1]"));
                falsz = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[2]/div/div/section/div[2]/div/div/div[2]/div[2]/button[2]"));
                dalej = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[2]/div/div/section/div[2]/div/div/button"));
                /* Pytanie 1 */
                driver.ExecuteScript("arguments[0].click();", prawda);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 2 */
                driver.ExecuteScript("arguments[0].click();", falsz);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 3 */
                driver.ExecuteScript("arguments[0].click();", falsz);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 4 */
                driver.ExecuteScript("arguments[0].click();", prawda);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 5 */
                driver.ExecuteScript("arguments[0].click();", prawda);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 6 */
                driver.ExecuteScript("arguments[0].click();", prawda);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 7 */
                driver.ExecuteScript("arguments[0].click();", prawda);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 8 */
                driver.ExecuteScript("arguments[0].click();", prawda);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 9 */
                driver.ExecuteScript("arguments[0].click();", prawda);
                driver.ExecuteScript("arguments[0].click();", dalej);

                /* Opowiedz nam o sobie */
                driver.Url = "https://alterzone.pl/aktywnosci/ankieta1_2023_luty/gra";
                var ankieta_button = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[2]/div/div/section/div[2]/div/div/div[3]/button[1]"));
                dalej = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[2]/div/div/section/div[2]/div/div/button"));
                /* Pytanie 1 */
                driver.ExecuteScript("arguments[0].click();", prawda);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 2 */
                driver.ExecuteScript("arguments[0].click();", falsz);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 3 */
                driver.ExecuteScript("arguments[0].click();", falsz);
                driver.ExecuteScript("arguments[0].click();", dalej);
                /* Pytanie 4 */
                driver.ExecuteScript("arguments[0].click();", prawda);
                driver.ExecuteScript("arguments[0].click();", dalej);
            }
            catch (Exception ex)
            {
                AnsiConsole.MarkupLine($"│    [indianred]ALTERZONE AIO[/] ─── {ex.Message}");
            }
        }

        private async Task Redeem(WebDriver driver, WebDriverWait wait, string site, string suffix)
        {
            try
            {
                driver.Url = site;
                string odbierz_xpath = "", kod_xpath = "";

                if (site.Contains("zone_awards_3wcenie1"))
                {
                    odbierz_xpath = "//*[@id=\"root\"]/div/div[2]/div/div/section/div[2]/div[6]/button";
                    kod_xpath = "//*[@id=\"root\"]/div/div[2]/div/div/section/div[2]/button";
                }
                else if (site.Contains("neo_1+1_nastart"))
                {
                    odbierz_xpath = "//*[@id=\"root\"]/div/div[2]/div/div/section/div[2]/div[7]/button";
                    kod_xpath = "//*[@id=\"root\"]/div/div[2]/div/div/section/div[2]/div[4]/button";
                }

                wait.Until(ExpectedConditions.ElementExists(By.XPath(odbierz_xpath)));
                var odbierz_nagrode = driver.FindElement(By.XPath(odbierz_xpath));
                driver.ExecuteScript("arguments[0].click();", odbierz_nagrode);
                wait.Until(ExpectedConditions.ElementExists(By.XPath("//*[@id=\"root\"]/div/div[2]/div/div/section/div/div[3]/button")));
                var potwierdz = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[2]/div/div/section/div/div[3]/button"));
                driver.ExecuteScript("arguments[0].click();", potwierdz);

                /* kopiuj kod */
                wait.Until(ExpectedConditions.ElementExists(By.XPath(kod_xpath)));
                var kod = driver.FindElement(By.XPath(kod_xpath));
                File.AppendAllText("kody.txt", kod.Text.Replace("KOD: ", "") + $" ({suffix})\n");
                AnsiConsole.MarkupLine($"│    [mediumpurple4]ALTERZONE AIO[/] ─── Dodano kod [mediumpurple4]{kod.Text.Replace("KOD: ", "")} [/]([mediumpurple4]{suffix}[/]) ([mediumpurple4]{this.counter}[/])");
            }
            catch (Exception ex)
            {
                AnsiConsole.MarkupLine($"│    [indianred]ALTERZONE AIO[/] ─── {ex.Message}");
            }
        }

        public async Task Execute(string alterzone_link) 
        {
            while (true)
            {
                EdgeDriver driver = null;
                WebDriverWait wait = null;
                using (new OutputSink.OutputSink())
                {
                    driver = new EdgeDriver(this.service, this.options);
                    wait = new WebDriverWait(driver, TimeSpan.FromSeconds(30));
                }
                
                driver.Url = alterzone_link;
                try
                {
                    /* potwierdzenie wieku */
                    wait.Until(ExpectedConditions.ElementExists(By.XPath("/html/body/div[5]/div/div/div[2]/div/div[3]/button[1]")));
                    var potwierdzam_wiek = driver.FindElement(By.XPath("/html/body/div[5]/div/div/div[2]/div/div[3]/button[1]"));
                    driver.ExecuteScript("arguments[0].click();", potwierdzam_wiek);

                    /* cookies */
                    wait.Until(ExpectedConditions.ElementExists(By.XPath("//*[@id=\"accept_cookies\"]")));
                    var cookies = driver.FindElement(By.XPath("//*[@id=\"accept_cookies\"]"));
                    driver.ExecuteScript("arguments[0].click();", cookies);

                    /* rejestracja */
                    wait.Until(ExpectedConditions.ElementExists(By.XPath("//*[@id=\"root\"]/div/div[1]/div/div/div/div/div/div[2]/div/div[2]/button")));
                    var wchodze_w_to = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[1]/div/div/div/div/div/div[2]/div/div[2]/button"));
                    driver.ExecuteScript("arguments[0].click();", wchodze_w_to);

                    /* imie */
                    wait.Until(ExpectedConditions.ElementExists(By.XPath("//*[@id=\"root\"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[3]/div[1]/input")));
                    var imie = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[3]/div[1]/input"));
                    imie.SendKeys(RandomizerFactory.GetRandomizer(new FieldOptionsFirstName()).Generate());

                    /* nazwisko */
                    var nazwisko = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[3]/div[2]/input"));
                    nazwisko.SendKeys(RandomizerFactory.GetRandomizer(new FieldOptionsLastName()).Generate());

                    /* email */
                    var email = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[3]/div[3]/input"));
                    var mailbox = await GenerateEmail();
                    email.SendKeys(mailbox);

                    /* data urodzenia */
                    var dzien = new SelectElement(driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[3]/div[4]/div/select[1]")));
                    var miesiac = new SelectElement(driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[3]/div[4]/div/select[2]")));
                    var rok = new SelectElement(driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[3]/div[4]/div/select[3]")));
                    dzien.SelectByValue(new Random().Next(1, 28).ToString());
                    miesiac.SelectByValue(new Random().Next(1, 11).ToString());
                    rok.SelectByValue(new Random().Next(1988, 2004).ToString());

                    /* kod pocztowy */
                    var kod_pocztowy = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[3]/div[5]/input"));
                    kod_pocztowy.SendKeys($"{new Random().Next(10, 99)}-{new Random().Next(100, 999)}");

                    /* zgody */
                    var consent_agreement = driver.FindElement(By.XPath("//*[@id=\"consentAgreement\"]"));
                    var age_verified = driver.FindElement(By.XPath("//*[@id=\"ageVerified\"]"));
                    var conset_data = driver.FindElement(By.XPath("//*[@id=\"consentData\"]"));
                    driver.ExecuteScript("arguments[0].click();", consent_agreement);
                    driver.ExecuteScript("arguments[0].click();", age_verified);
                    driver.ExecuteScript("arguments[0].click();", conset_data);

                    /* dalej */
                    var dalej = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[4]/button"));
                    driver.ExecuteScript("arguments[0].click();", dalej);

                    /* zarejestruj sie */
                    wait.Until(ExpectedConditions.ElementExists(By.XPath("//*[@id=\"root\"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[4]/button")));
                    dalej = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[4]/button"));
                    driver.ExecuteScript("arguments[0].click();", dalej);

                    /* aktywacja mail */
                    var email_activation_link = "";
                    var text = await GetEmailBody(mailbox);
                    var text_array = text.Split('\n').Where(line => line.Contains("aHR0cHM6Ly9hbHRlcnpvbmUucGwvaGFzbG8vdXN0YXc")).ToArray();
                    var match = Regex.Match(text_array[0], "(http):\\/\\/([\\w_-]+(?:(?:\\.[\\w_-]+)+))([\\w.,@?^=%&:\\/~+#-]*[\\w@?^=%&\\/~+#-])");
                    if (match.Success)
                    {
                        email_activation_link = match.Value;
                    }

                    /* ustawianie hasla */
                    driver.Url = email_activation_link;
                    wait.Until(ExpectedConditions.ElementExists(By.XPath("//*[@id=\"passwd\"]")));
                    var haslo = driver.FindElement(By.XPath("//*[@id=\"passwd\"]"));
                    var powtorz_haslo = driver.FindElement(By.XPath("//*[@id=\"repeatPasswd\"]"));
                    haslo.SendKeys("Unknown1234!@");
                    powtorz_haslo.SendKeys("Unknown1234!@");

                    /* ustaw haslo */
                    wait.Until(ExpectedConditions.ElementExists(By.XPath("//*[@id=\"root\"]/div/div[1]/div/div/div/div/div/form/div[3]/button")));
                    var ustaw_haslo = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[1]/div/div/div/div/div/form/div[3]/button"));
                    driver.ExecuteScript("arguments[0].click();", ustaw_haslo);

                    /* konto aktywne */
                    wait.Until(ExpectedConditions.ElementExists(By.XPath("/html/body/div[5]/div/div/div[2]/div")));
                    var zaloguj_sie = driver.FindElement(By.XPath("/html/body/div[5]/div/div/div[2]/div/button"));
                    driver.ExecuteScript("arguments[0].click();", zaloguj_sie);

                    /* logowanie */
                    wait.Until(ExpectedConditions.ElementExists(By.XPath("//*[@id=\"root\"]/div/div[1]/div/div/div/div/div/form/div[3]/div[1]/input")));
                    email = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[1]/div/div/div/div/div/form/div[3]/div[1]/input"));
                    haslo = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[1]/div/div/div/div/div/form/div[3]/div[2]/input"));
                    zaloguj_sie = driver.FindElement(By.XPath("//*[@id=\"root\"]/div/div[1]/div/div/div/div/div/form/div[5]/button"));
                    email.SendKeys(mailbox);
                    haslo.SendKeys("Unknown1234!@");
                    driver.ExecuteScript("arguments[0].click();", zaloguj_sie);

                    /* glowna strona */
                    wait.Until(ExpectedConditions.ElementExists(By.XPath("/html/body/div[9]/div/div/div[2]/div/div[3]/button[1]")));
                    var odrzuc = driver.FindElement(By.XPath("/html/body/div[9]/div/div/div[2]/div/div[3]/button[1]"));
                    driver.ExecuteScript("arguments[0].click();", odrzuc);

                    /* odbierz nagrody */
                    await this.Redeem(driver, wait, "https://alterzone.pl/nagrody/odbior/neo_1+1_nastart", "2 w cenie 1");
                    if (this.limited_offer)
                    {
                        await this.GetPoints(driver, wait);
                        await this.Redeem(driver, wait, "https://alterzone.pl/nagrody/odbior/drop/zone_awards_3wcenie1", "3 w cenie 1");
                    }
                    this.counter++;
                }
                catch (Exception ex)
                {
                    AnsiConsole.MarkupLine($"│    [indianred]ALTERZONE AIO[/] ─── {ex.Message}");
                }
                finally
                {
                    driver.Close();
                    driver.Quit();
                }
            }
        }
    }
}
