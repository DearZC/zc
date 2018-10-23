package test;

import org.openqa.selenium.WebDriver;

public class Main {

	public static void main(String[] args) {

		DSP dsp;
		dsp = new DSP();
		WebDriver web = dsp.login();

//		Plan plan;
//		plan = new Plan();
//
//		plan.enterPlan(web);
//		plan.createPlan(web);

	}

}
