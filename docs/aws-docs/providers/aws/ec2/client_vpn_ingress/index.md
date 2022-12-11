---
title: client_vpn_ingress
hide_title: false
hide_table_of_contents: false
keywords:
  - client_vpn_ingress
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
<tr><td><b>Name</b></td><td><code>client_vpn_ingress</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.client_vpn_ingress</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `client_vpn_ingress_Authorize` | `EXEC` | `ClientVpnEndpointId, TargetNetworkCidr` | Adds an ingress authorization rule to a Client VPN endpoint. Ingress authorization rules act as firewall rules that grant access to networks. You must configure ingress authorization rules to enable clients to access resources in Amazon Web Services or on-premises networks. |
| `client_vpn_ingress_Revoke` | `EXEC` | `ClientVpnEndpointId, TargetNetworkCidr` | Removes an ingress authorization rule from a Client VPN endpoint.  |
