---
title: dhcp_options
hide_title: false
hide_table_of_contents: false
keywords:
  - dhcp_options
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dhcp_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.dhcp_options</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `dhcpConfigurationSet` | `array` | One or more DHCP options in the set. |
| `dhcpOptionsId` | `string` | The ID of the set of DHCP options. |
| `ownerId` | `string` | The ID of the Amazon Web Services account that owns the DHCP options set. |
| `tagSet` | `array` | Any tags assigned to the DHCP options set. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `dhcp_options_Describe` | `SELECT` |  | &lt;p&gt;Describes one or more of your DHCP options sets.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html"&gt;DHCP options sets&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `dhcp_options_Create` | `INSERT` | `DhcpConfiguration` | &lt;p&gt;Creates a set of DHCP options for your VPC. After creating the set, you must associate it with the VPC, causing all existing and new instances that you launch in the VPC to use this set of DHCP options. The following are the individual DHCP options you can specify. For more information about the options, see &lt;a href="http://www.ietf.org/rfc/rfc2132.txt"&gt;RFC 2132&lt;/a&gt;.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;domain-name-servers&lt;/code&gt; - The IP addresses of up to four domain name servers, or AmazonProvidedDNS. The default DHCP option set specifies AmazonProvidedDNS. If specifying more than one domain name server, specify the IP addresses in a single parameter, separated by commas. To have your instance receive a custom DNS hostname as specified in &lt;code&gt;domain-name&lt;/code&gt;, you must set &lt;code&gt;domain-name-servers&lt;/code&gt; to a custom DNS server.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;domain-name&lt;/code&gt; - If you're using AmazonProvidedDNS in &lt;code&gt;us-east-1&lt;/code&gt;, specify &lt;code&gt;ec2.internal&lt;/code&gt;. If you're using AmazonProvidedDNS in another Region, specify &lt;code&gt;region.compute.internal&lt;/code&gt; (for example, &lt;code&gt;ap-northeast-1.compute.internal&lt;/code&gt;). Otherwise, specify a domain name (for example, &lt;code&gt;ExampleCompany.com&lt;/code&gt;). This value is used to complete unqualified DNS hostnames. &lt;b&gt;Important&lt;/b&gt;: Some Linux operating systems accept multiple domain names separated by spaces. However, Windows and other Linux operating systems treat the value as a single domain, which results in unexpected behavior. If your DHCP options set is associated with a VPC that has instances with multiple operating systems, specify only one domain name.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ntp-servers&lt;/code&gt; - The IP addresses of up to four Network Time Protocol (NTP) servers.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;netbios-name-servers&lt;/code&gt; - The IP addresses of up to four NetBIOS name servers.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;netbios-node-type&lt;/code&gt; - The NetBIOS node type (1, 2, 4, or 8). We recommend that you specify 2 (broadcast and multicast are not currently supported). For more information about these node types, see &lt;a href="http://www.ietf.org/rfc/rfc2132.txt"&gt;RFC 2132&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Your VPC automatically starts out with a set of DHCP options that includes only a DNS server that we provide (AmazonProvidedDNS). If you create a set of options, and if your VPC has an internet gateway, make sure to set the &lt;code&gt;domain-name-servers&lt;/code&gt; option either to &lt;code&gt;AmazonProvidedDNS&lt;/code&gt; or to a domain name server of your choice. For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html"&gt;DHCP options sets&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `dhcp_options_Delete` | `DELETE` | `DhcpOptionsId` | Deletes the specified set of DHCP options. You must disassociate the set of DHCP options before you can delete it. You can disassociate the set of DHCP options by associating either a new set of options or the default set of options with the VPC. |
| `dhcp_options_Associate` | `EXEC` | `DhcpOptionsId, VpcId` | &lt;p&gt;Associates a set of DHCP options (that you've previously created) with the specified VPC, or associates no DHCP options with the VPC.&lt;/p&gt; &lt;p&gt;After you associate the options with the VPC, any existing instances and all new instances that you launch in that VPC use the options. You don't need to restart or relaunch the instances. They automatically pick up the changes within a few hours, depending on how frequently the instance renews its DHCP lease. You can explicitly renew the lease using the operating system on the instance.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html"&gt;DHCP options sets&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
