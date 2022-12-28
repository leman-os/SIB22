import nmap3

scan = nmap3.Nmap()
version_result = scan.nmap_version_detection("192.168.56.101")
for i in version_result["192.168.56.101"]["ports"]:
    print("PortID: "+i["portid"], "| Service Name: "+i["service"]["name"], "| Service Version:"+i["service"].get('version', 'none'))