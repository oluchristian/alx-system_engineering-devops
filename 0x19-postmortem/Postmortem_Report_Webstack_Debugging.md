# Postmortem for Webstack Debugging
## An ALX Project

### Issue summary
From 6:45 AM to 8:43AM GMT, the production environment experienced a service outage during the routine deployment of a software update resulting in 1 hour and 5 minutes service downtime for the users. Investigation revealed that the outage was due to misconfiguration in the deployment script which led to incorrect server settings and incompatible dependencies.

### Timeline (all times GMT)
6:45 AM - Configuration push begin
6:50 AM - Outage begins
6:55 AM - Pagers alerted the developer on call
7:00 AM - Failed configuration change rollback
7:55 AM - Successful configuration change rollback
8:00 AM - Server restarts begins.
8:05 AM - 100% of traffic back online

### Root cause
The root cause was due to a misconfigured environment variable in the deployment script which caused the application to fail to sart properly.

### Resolution
The changes made on the misconfigured file which caused the error was rolled back and the file was reconfigured with the correct environment variable.

### Corrective and preventative measures:

#### Improvements/Fixes:
Tighten review processes for deployment scripts to catch misconfigurations before deployment.
Implement automated testing of deployment configurations to ensure compatibility and correctness.
Enhance monitoring to promptly detect similar misconfigurations in the future.
#### List of Tasks:
Implement strict code review policies for deployment scripts, including peer reviews and automated checks for environment variables.
Develop and implement automated tests for deployment configurations to verify compatibility and correctness before deployment.
Integrate more granular monitoring of application startup processes to quickly identify failures related to misconfigurations.
Conduct a thorough review of all environment variables used in deployment scripts and ensure they are properly documented and validated.

By implementing these measures, we aim to minimize the risk of similar incidents in the future and improve the resilience of our production environment.