<!DOCTYPE html>
<html>
    <head>
            <style>
                body {
                    background:rgb(250, 165, 8);
                    color: blueviolet;
                }
            </style>
         </head>
         <body>
            <h1>GoalSmith</h1>
         </body>
</html>

<style>
    .dropbtn {
      background-color: #e5ff00;
      color: rgb(76, 0, 255);
      padding: 16px;
      font-size: 16px;
      border: none;
    }
    
    .dropdown {
      position: relative;
      display: inline-block;
    }
    
    .dropdown-content {
      display: none;
      position: absolute;
      background-color: #eeff02;
      min-width: 160px;
      box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
      z-index: 1;
    }
    
    .dropdown-content a {
      color: rgb(26, 1, 252);
      padding: 12px 16px;
      text-decoration: none;
      display: block;
    }
    
    .dropdown-content a:hover {background-color: rgb(176, 252, 109);}
    
    .dropdown:hover .dropdown-content {display: block;}
    
    .dropdown:hover .dropbtn {background-color: #78fe71;}
    </style>
    </head>
    <body>
    
    <div class="dropdown">
      <button class="dropbtn">Getting Started</button>
      <div class="dropdown-content">
        <a href="Sign In Sign Up.html">Sign In/Sign Up</a>
        <a href="Continue as guest user.html">Continue as guest user</a>
        <a href="Short time goal.html">Short time goal</a>
      </div>
    </div>
