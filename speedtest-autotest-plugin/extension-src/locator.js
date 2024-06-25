locators = {
  homeLink: cy.get('ul.navbar-nav li.nav-item').eq(0).find('a.nav-link'),
  signInLink: cy.get('ul.navbar-nav li.nav-item').eq(1).find('a.nav-link'),
  usernameInput: cy.get('div.auth-page div.container div.row div.col-md-6 form fieldset input[formcontrolname="username"]'),
  emailInput: cy.get('div.auth-page div.container div.row div.col-md-6 form fieldset input[formcontrolname="email"]'),
  passwordInput: cy.get('div.auth-page div.container div.row div.col-md-6 form fieldset input[formcontrolname="password"]'),
  signUpButton: cy.get('div.auth-page div.container div.row div.col-md-6 form fieldset button.btn.btn-lg.btn-primary'),
}

const testcase = 'click signLink,input username, email,password';
