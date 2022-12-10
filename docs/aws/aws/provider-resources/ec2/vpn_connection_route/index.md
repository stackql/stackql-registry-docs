---
title: vpn_connection_route
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_connection_route
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
<tr><td><b>Name</b></td><td><code>vpn_connection_route</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.vpn_connection_route</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `vpn_connection_route_Create` | `INSERT` | `DestinationCidrBlock, VpnConnectionId` | &lt;p&gt;Creates a static route associated with a VPN connection between an existing virtual private gateway and a VPN customer gateway. The static route allows traffic to be routed from the virtual private gateway to the VPN customer gateway.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html"&gt;Amazon Web Services Site-to-Site VPN&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Site-to-Site VPN User Guide&lt;/i&gt;.&lt;/p&gt; |
| `vpn_connection_route_Delete` | `DELETE` | `DestinationCidrBlock, VpnConnectionId` | Deletes the specified static route associated with a VPN connection between an existing virtual private gateway and a VPN customer gateway. The static route allows traffic to be routed from the virtual private gateway to the VPN customer gateway. |
