from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
     [
        r"what is your name ?",
        ["My name is Chatty and I'm a chatbot ?",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    
     [
        r"(.*) clearpass (.*)extented(.*) IT (.*)",
        ["REST based API",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*)authentication|authorization sources|source (.*)clearpass(.*)",
        ["AD, LDAP, and SQL dB.",]
        
    ],
    [
        r"(.*) authentication protocols|protocol (.*) employee access(.*)",
        ["PEAP, EAP-FAST, EAP-TLS, EAP-TTLS, and EAP-PEAP-Public",]
        
    ],
    [
        r"(.*) created ?",
        ["HP created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Bangalore, Karnataka',]
    ],
    [
        r"(.*) virtualization platforms|platform (.*)clearpass(.*)",
        ["VMware vSphere Hypervisor (ESXi), Microsoft Hyper V, and Amazon AWS (EC2)",]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it.",]
    ],
[
        r"(.*) browsers|browser (.*)clearPass(.*)",
        ["Mozilla Firefox,Google Chrome,Apple safari,Microsoft Internet Explorer ",]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"(.*)virtual appliances|appliance (.*)platforms|platform(.*)",
        ["VMware ESX ,ESXi and Microsoft Hyper-V"]
    ],
    [
        r"(.*)active profiling methods|method (.*)",
        ["Nmap, WMI, SSH, SNMP"]
     ],
    [
        r"(.*) passive profiling methods|method (.*)",
        ["MAC OUI, DHCP, TCP, Netflow v5/v10, IPFIX, sFLOW, ‘SPAN’ Port, HTTP User-Agent, IF-MAP",]
    ],
    [
        r"(.*)integrated (.*) third-party profiling methods(.*)",
        ["Onboard, OnGuard, ArubaOS, EMM/MDM, Rapid7, Cisco device sensor",]
    ],
    [
        r"(.*)clearpass hardware appliance ports|port (.*)",
        ["Data port,iLO port,Management port,Serial port,USB ports"]
    ],
    [
        r"(.*)versions|version(.*) VMware vSphere Hypervisor(.*)",
        ["5.5,6.0,6.5 U1"]
     ],
    [
        r"(.*)multiple device registration portals|portal(.*)",
        ["Guest, Aruba AirGroup, BYOD (bring your own device)"]
    ],
    [
        r"(.*)Admin|Operator (.*) security(.*)",
        ["via CAC (Common Access Card) and TLS (Transport Layer Security) certificates",]
    ],
    [
        r"(.*)identity stores|store (.*)Clearpass(.*)",
        ["Built-in SQL store,Built-in SQL store, static hosts list"]
    ],
    [
        r"(.*)expansion|expand (.*)OCSP(.*)",
        ["Online Certificate Status Protocol",]
   ],
   [
        r"(.*)addressing(.*) clearpass(.*)",
        ["Ipv6"]
    ],
    
    [
        r"(.*)Clearpass use|uses ipv6 or ipv4 addressing(.*)",
        ["Ipv6"]
    ],
    [
        r"(.*)clearpass (.*)addressing(.*)",
        ["It uses Ipv6."]
    ],
    [
        r"(.*)ClearPass C1000 Hardware Appliance|appliances(.*)",
        ["It is a RADIUS/ TACACS+ server that provides advanced policy control for up to 500 simultaneous sessions."]
    ],
    [
        r"(.*)pro5000 simultaneous sessions|session (.*) ClearPass C2000 Hardware Appliance|appliances(.*)",
        ["5000 simultaneous sessions"]
    ],
    [
        r"(.*)color indicates|indicate (.*)Risk Score Colors|color(.*)",
        ["Blue-Very Low Risk,brown - Low Risk,yellow-Medium Risk,Red-High Risk"]
   ],
    [
        r"(.*)standard (.*)clearpass Guest(.*)",
        ["It is built on AAA framework which is based on authentication,authorization, and accounting components."]
   ],
    [
        r"(.*)protocol (.*)NAS (.*)authenticate(.*) user(.*)",
        ["RADIUS protocol"]
    ],
    [
        r"(.*)network connectivity (.*)clearpass Guest(.*)",
        ["VLAN selection, IP address, and hostname"]
    ],
    [
        r"(.*)uses|use (.*)airgroup(.*)",
        ["AirGroup allows users to register their personal mobile devices on the local network and define a group of friends or associates who are allowed to share them."]
    ],
    [
        r"(.*)cookies|cookie used(.*)",
        ["Cookies are used  to make Web sites work, or work more efficiently, as well as to provide information to the owners"]
    ],
    [
        r"What (.*)cookies|cookie",
        ["Cookies are small text files that are placed on a user’s computer by Web sites the user visits."]
    ],
    [
        r"(.*) NAS",
        ["Network Access Server used to authenticate and  provide access to the network"]
    ],
    
     [
        r"(.*)possible states|state(.*) session|sessions(.*)",
        ["Active,stale,closed"]
    ],
     [
        r"what (.*)dynamic authorisation(.*)",
        ["Dynamic Authorization describes the ability to make changes to a guest account’s session while it is in progress."]
    ],
     [
        r"(.*)built-in AAA services|service (.*)aruba(.*)",
        ["RADIUS, TACACS+, and Kerberos"]
    ],
     [
        r"(.*)mobile device posture checks(.*) aruba",
        ["They are: Network Access Control (NAC), Network Access Protection (NAP) posture and health checks, and Mobile Device Management(MDM)"]
    ],
     [
        r"(.*)Device and User certificate enrollment(.*) aruba(.*)",
        ["Simple Certificate Enrollment Protocol (SCEP), Enrollment over Secure Transport (EST) and REST API-based workflows"]
    ],
     [
        r"(.*)APIs (.*)aruba(.*)",
        ["HTTP/RESTful APIs"]
   ],
     [
        r"(.*)Framework|frameworks and Protocolprotocols (.*)aruba(.*)",
        ["EAP-FAST,PEAP,EAP-TTLS,EAP-TLS"]
    ],
     [
        r"(.*)Identity Stores|store (.*)aruba(.*)",
        ["Microsoft Active Directory,Kerberos,Microsoft SQL, PostgreSQL, MariaDB, and Oracle 11g ODBC-compliant SQL server"]
    ],
     [
        r"(.*)browser|browsers (.*)aruba(.*)",
        ["Apple Safari 9.x,Mobile Safari 5.x,Microsoft Edge"]
    ],
    [
        r"(.*)special character|characters (.*)password|passwords (.*)aruba(.*)",
        ["Plus sign,Comma,Hyphen,Period,Semicolon,Equal sign,Question mark,Underscore"]
    ], 
    [
        r"(.*)Initial Login|Activation (.*)ClearPass Platform License (.*)aruba(.*)",
        ["Specifying the ClearPass Platform License Key Upon Initial Login,Logging in to the ClearPass Server,Customizing the Landing Page Layout,"]
    ], 
    [
        r"(.*)default password(.*)",
        ["eTIPS123"]
     ], 
    [
        r"(.*)graph|graphs (.*)displays|display|displayed (.*)requests|request(.*)",
        [" RADIUS,TACACS+, and WebAuth requests"]
     ],
     [
        r"(.*)services|service (.*)aruba(.*)",
        ["Services Flow and Creation Methods ,Modifying and Managing Services,Using Templates to Create ClearPass Services,Configuring Other Policy Manager Services"]
     ],
     [
        r"(.*)options|option (.*) Posture(.*)",
        ["Posture Architecture and Flow,Creating a New Posture Policy,Configuring Audit Servers"]
     ],
     [
        r"(.*)elements|element (.*)modified(.*) Profile and Network Scan page|pages(.*)",
        ["Subnet scans,Network scans,SNMP Configuration,SSH Configuration,WMI Configuration"]
     ],
    [
        r"(.*)list (.*)provided services|service template|templates(.*)",
        ["802.1X Wired, 802.1X Wireless, and Aruba 802.1X Wireless Service Template,"]
     ],
    [
        r"(.*)aruba 802.1X|802.1 Wired service template|templates(.*)",
        ["The Aruba 802.1X Wireless template is designed for wireless end-hosts connecting through an Aruba 802.11 wireless access device or controller using IEEE 802.1X authentication"]
     ],
    [
        r"(.*)parameters|parameter (.*)Authentication Source(.*)",
        ["Server,Port,Identity,Password,NetBIOS,Base DN"]
     ],
    [
        r"(.*)attribute|attributes (.*)Authentication Source(.*)",
        ["Account Expires,Department,Email,Name,Phone, UserDN,Company,member of"]
     ],
    [
        r"(.*)Wired Network Settings(.*) aruba",
        ["Select Switch,Device Name,IP Address,Vendor Name,RADIUS Shared Secret"]
     ],
    [
        r"(.*)Pagination(.*)",
        [" pagination controls to navigate through pages of your results. The count of results displayed and total shows below the page links"]
     ],
    [
        r"(.*) types|type (.*) filters(.*)",
        ["user,host,IP"]
     ],[
        r"(.*)Column|columns (.*)database(.*)",
        ["Entity,Department,Risk Score,Change"]
     ],[
        r"(.*)action|actions (.*)Entity360(.*)",
        ["Time Range Picker,Search Bar,Filter Options"]
     ],
    [
        r"(.*)column|columns(.*) Alerts(.*)",
        ["Type,Contribution,Date,Severity,Confidence,Stage"]
     ],
    [
        r"(.*)buttons (.*)Entity360(.*)",
        ["The buttons are: actions,summary,NAC Timeline,activity,group by,devices,apps & ports,auth. history,conv. graph,web history,comments"]
     ],
    [
        r"(.*)Login Details(.*)",
        ["The login details are: Time,Domain,Host Name,IP Address,MAC Address,Logon Type,Status"]
     ],
    [
        r"(.*) attribute|attributes (.*) Profile Overviews|overview(.*)",
        ["The attributes are: top internal server,bottom internal server,top internal apps,top internet sites,top internal hosts"]
     ],
    [
        r"(.*)Windows Server 2008 Core(.*)SQL Server(.*)",
        ["The Windows Server 2008 Core edition can:Run the file server role.Run the Hyper-V virtualization server role.Run the Directory Services role.Run the DHCP server role."]
     ],
    [
        r"(.*) network devices(.*) clearpass(.*) 802.1x|802.1 auth(.*)",
        [" Clearpass is vendor Neutral, any network device that has 802.1x feature, it should work with clearpass"]
     ],
    [
        r"(.*) Block (.*) users|user from installing new virtual machines|machine(.*)",
        ["This depending upon the user level access that you create on the ESX (Assuming you are using VM Ware virutal machines).  you could assign the roles, access for the VM users on the ESX itself and you can authenticate and return the respective roles from Clearpass"]
     ],
    [
        r"(.*)branching and merging tutorials|tutorial (.*) TortoiseSVN(.*)",
        ["A very good resource for source control in general. Not really TortoiseSVN specific, though"]
     ],
    [
        r"(.*)medical devices|device (.*) clearpass(.*)",
        ["if the device supports authentication, it would work with clearpass."]
     ],
    [
        r"(.*)scripting(.*) .NET applications|application(.*)",
        ["You could use any of the DLR languages, which provide a way to really easily host your own scripting platform. However, you don't have to use a scripting language for this. You could use C# and compile it with the C# code provider. As long as you load it in its own AppDomain, you can load and unload it to your heart's content."]
     ],
    [
        r"(.*)Continuous integration (.*)SVN(.*)",
        ["CC is quite good in that you can have one CC server monitor another CC server so you could set up stuff like - when a build completes on your build server, your test server would wake up, boot up a virtual machine and deploy your application"]
     ],
    [
        r"(.*)CruiseControl.NET run|runs (.*) IIS 7.0(.*)",
        ["just use the http://confluence.public.thoughtworks.org/display/CCNET/Welcome+to+CruiseControl.NET rel=nofollow title=Human Interface Guidelines>CruiseControl.NET wiki"]
     ],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)hardware appliance|appliances platform|platforms (.*)aruba(.*)",
        ["ClearPass Policy Manager, C1000 ClearPass Policy Manager C2000, ClearPass Policy Manager C3000"]
    ],
    [
        r"(.*)Powering|power Off (.*)ClearPass Hardware(.*)",
        ["Connect to the CLI from the serial console using the serial port.And then Enter the following commands: login: poweroff, password: poweroff"]
    ],
    [
        r"(.*)Hypervisors(.*)clearpass",
        ["VMware vSphere Hypervisor (ESXi),Microsoft Hyper-V"]
    ],
    [
        r"(.*)Login Details(.*)",
        ["Login details are: Time,Domain,Host Name,IP Address,MAC Address,Logon Type,Status"]
    ],
    [
        r"(.*) Viewing Conversations Graph(.*)",
        ["The graph shows only the 1000 most recent conversations, which covers only a small amount of time. For best performance, use search criteria to refine the results. You may also want to keep the date range set to past hour or today, unless you use extensive search criteria."]
    ],
    [
        r"(.*) option|options (.*)Conversations Graph(.*)",
        ["General Settings,Nodes Tab,Links Tab,Timebar Tab, Properties Tab"]
    ],
    [
        r"(.*)classification|classifications|type|types (.*)Alert(.*)",
        ["Attack Stage,Alert Category,Alert Type,Alert Name"]
    ],
    [
        r"(.*) alert360",
        ["Use Alert360 to view, investigate, and take action on an alert.The panels on this page are explained in this section.Different panels appear for discrete versus GUEBA alerts and different alert conditions."]
    ],
    
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    
    
]
def chatty(userText):
    chat = Chat(pairs, reflections)
    userText=userText.lower()
    return chat.respond(userText)

