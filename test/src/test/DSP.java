package test;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class DSP {

	public WebDriver login() {
		// TODO Auto-generated method stub

		System.setProperty("webdriver.chrome.driver",
				"C:\\Users\\zc\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe");
		WebDriver driver = new ChromeDriver();
		driver.get("http://dspdev.ssptest.gionee.com/list/cpt");
		

		WebElement username = driver.findElement(By.name("username"));
		username.sendKeys("gionee_zc03");

		WebElement password = driver.findElement(By.name("password"));
		password.sendKeys("123456");

		WebElement picture = driver.findElement(By.className("code"));
		picture.sendKeys("2017");

		WebElement login = driver.findElement(By.xpath("//div[@class='form-cont']/input[@type='submit']"));
		login.click();

		// 最大化窗口
		driver.manage().window().maximize();
		
		return  driver;
	}
}