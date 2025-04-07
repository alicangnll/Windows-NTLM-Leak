# NTLM Hash Leak via .theme File

# About Vulnerability
- Author: Ali Can Gönüllü, Cyber Security Specialist
- Discovery Date: 19.03.2025
- Vulnerability CVE Number: -
- CVSS v3.1 Score: 6.8 – 7.0 (Medium)</li>
</ul>

# CVSS v3.1 Scoring Table
CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:N/A:N

# Vulnerability Testing / Recreation Phase 

Recommended to test on Kali Linux 
- 	Install the required package with <b>pip install websocket-client</b> command
- 	Then send the file to the target computer and let the target click on the file.


# Finding Vulnerability 

Exposure of sensitive information to an unauthorized actor in Windows Theme allows an unauthorized attacker to perform spoofing over a network.
In the related vulnerability, the SMB path written in the Windows Theme file tries to establish a connection with the SMB server determined as soon as the file with the “.theme” extension is clicked. In this case, NTLM codes are exposed and spoofing is performed.

https://github.com/user-attachments/assets/8d4ca4f9-658b-4484-a7a3-528e1dc51f65

# Eliminating Vulnerability 

-	Need to update your Windows Server version
