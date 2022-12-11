---
title: private_ip_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - private_ip_addresses
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
<tr><td><b>Name</b></td><td><code>private_ip_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.private_ip_addresses</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `private_ip_addresses_Assign` | `EXEC` | `NetworkInterfaceId` | &lt;p&gt;Assigns one or more secondary private IP addresses to the specified network interface.&lt;/p&gt; &lt;p&gt;You can specify one or more specific secondary IP addresses, or you can specify the number of secondary IP addresses to be automatically assigned within the subnet's CIDR block range. The number of secondary IP addresses that you can assign to an instance varies by instance type. For information about instance types, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html"&gt;Instance Types&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;. For more information about Elastic IP addresses, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html"&gt;Elastic IP Addresses&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;When you move a secondary private IP address to another network interface, any Elastic IP address that is associated with the IP address is also moved.&lt;/p&gt; &lt;p&gt;Remapping an IP address is an asynchronous operation. When you move an IP address from one network interface to another, check &lt;code&gt;network/interfaces/macs/mac/local-ipv4s&lt;/code&gt; in the instance metadata to confirm that the remapping is complete.&lt;/p&gt; &lt;p&gt;You must specify either the IP addresses or the IP address count in the request.&lt;/p&gt; &lt;p&gt;You can optionally use Prefix Delegation on the network interface. You must specify either the IPv4 Prefix Delegation prefixes, or the IPv4 Prefix Delegation count. For information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-prefix-eni.html"&gt; Assigning prefixes to Amazon EC2 network interfaces&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `private_ip_addresses_Unassign` | `EXEC` | `NetworkInterfaceId` | Unassigns one or more secondary private IP addresses, or IPv4 Prefix Delegation prefixes from a network interface. |
