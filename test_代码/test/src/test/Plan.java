package test;


import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class Plan {
	// TODO Auto-generated method stub
//	WebDriver driver = new ChromeDriver();
	
	public void enterPlan(WebDriver driver) {
		
		WebElement advManage = driver.findElement(By.linkText("������"));
		advManage.click();
	}
	
	public void createPlan(WebDriver driver) {
		
		WebElement create = driver.findElement(By.linkText("�½����ƻ�"));
		create.click();
		
		WebElement planName = driver.findElement(By.name("name"));
		planName.sendKeys("test_1");			
		
		WebElement totalBudget = driver.findElement(By.name("budget"));
		totalBudget.sendKeys("100000");
		
//		String jsString = "document.getElementById('workTime').nextSibling.firstChild.nextSibling.removeAttribute('readonly')";
//        JavascriptExecutor js = (JavascriptExecutor) driver;
//        js.executeScript(jsString);
	
		JavascriptExecutor removeAttribute = (JavascriptExecutor)driver;  		
		removeAttribute.executeScript("var setDate=document.getElementById(\"start_date\");setDate.removeAttribute('readonly');");
		WebElement startTime = driver.findElement(By.name("start_date"));
		startTime.sendKeys("2018-01-30");
		
		WebElement save = driver.findElement(By.linkText("����"));
		save.click();
		
		
		
		
	}


}
