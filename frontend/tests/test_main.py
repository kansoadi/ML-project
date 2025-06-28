from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_streamlit_frontend():
    # Set up the WebDriver (e.g., ChromeDriver)
    driver = webdriver.Chrome()

    try:
        # Open the Streamlit app
        driver.get("http://127.0.0.1:8501")  # Replace with your Streamlit app's URL

        # Wait for the app to load
        time.sleep(5)

        # Interact with sliders (adjust slider selectors based on Streamlit's HTML structure)
        sliders = driver.find_elements(By.CLASS_NAME, "stSlider")
        slider_values = [5, 6, 7, 4, 3, 8, 2, 6, 1]  # Example values for each slider

        for slider, value in zip(sliders, slider_values):
            # Click and drag the slider to the desired value
            ActionChains(driver).click_and_hold(slider).move_by_offset(value * 10, 0).release().perform()
            time.sleep(0.5)  # Small delay for the slider to update

        # Submit the form (Streamlit automatically triggers the API call)
        time.sleep(3)  # Wait for the API response

        # Verify the prediction outcome
        prediction_output = driver.find_element(By.XPATH, "//*[contains(text(), 'Predicition Outcome:')]").text
        assert "Predicition Outcome:" in prediction_output

    finally:
        # Close the browser
        driver.quit()

# Run the test
test_streamlit_frontend()