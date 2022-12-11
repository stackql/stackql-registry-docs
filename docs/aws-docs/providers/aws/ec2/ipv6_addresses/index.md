---
title: ipv6_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - ipv6_addresses
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
<tr><td><b>Name</b></td><td><code>ipv6_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.ipv6_addresses</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ipv6_addresses_Assign` | `EXEC` | `NetworkInterfaceId` | &lt;p&gt;Assigns one or more IPv6 addresses to the specified network interface. You can specify one or more specific IPv6 addresses, or you can specify the number of IPv6 addresses to be automatically assigned from within the subnet's IPv6 CIDR block range. You can assign as many IPv6 addresses to a network interface as you can assign private IPv4 addresses, and the limit varies per instance type. For information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI"&gt;IP Addresses Per Network Interface Per Instance Type&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You must specify either the IPv6 addresses or the IPv6 address count in the request. &lt;/p&gt; &lt;p&gt;You can optionally use Prefix Delegation on the network interface. You must specify either the IPV6 Prefix Delegation prefixes, or the IPv6 Prefix Delegation count. For information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-prefix-eni.html"&gt; Assigning prefixes to Amazon EC2 network interfaces&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `ipv6_addresses_Unassign` | `EXEC` | `NetworkInterfaceId` | Unassigns one or more IPv6 addresses IPv4 Prefix Delegation prefixes from a network interface. |
