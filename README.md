# Task 1 Software configuration
## Subtask 1 Why did I choose to participate in the challenge portfolio? 

I would like to learn automation QA instruments to *__have more flexibility__* in testing. I dreamed of it when I finished a manual testing course some time ago. 

*__My goal__* is to become a trainee and to work in QA. I expect this project to help me grow and gain new skills. 


Besides, I am happy to learn from professionals and to have ability to work as a team with other participants. 

May the force be with us,

Iryna 

# TASK 2: Selectors

## scouts_panel_title_xpath

//form/div/div[1]/h5

//*[text()="Scouts Panel"]

//child::h5

## login_field_xpath 

//*[@id='login']

//*[@name='login']

//input[contains(@name, 'log')]

## password_field_xpath

//*[@id='password']

//*[@name='password']

//*[@type='password']

## remind_password_hyperlink_xpath 

//form/div/div[1]/a

//a[.='Remind password']

//child::div/a

## language_menu_button_xpath

//div[contains(@class,'selectMenu')]

//*[@role='button']

//*[@aria-haspopup='listbox']

## language_menu_icon_xpath 

//*[@d = 'M7 10l5 5 5-5z']

//*[name()='svg']

//*[contains(@class, 'SvgIcon')]

## sign_in_button_xpath

//form/div/div[2]/button

//*[@type='submit']

//button 

## Validations:

## Please provide your username or your e-mail.

## username_e_mail_validation_span_xpath

 //*[text()='Please provide your username or your e-mail.']

//span[.='Please provide your username or your e-mail.']

//*[@ class='MuiCardContent-root']/child::div[3]/span

#### the latter XPath allows for different text in case of different interaction, able to locate the validation notification itself, but not its certain text after certain interaction (login+password or only login)._ 

## Please provide your password.

## password_validation_span_xpath

//*[text()='Please provide your password.']

//span[.='Please provide your password.']

//form//div[1]/div[3]/span 

#### the latter XPath allows for different text in case of different interaction, able to locate the validation notification itself, but not its certain text after certain interaction (login+password or only login)._ 


