---
title: client_vpn_authorization_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - client_vpn_authorization_rules
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
<tr><td><b>Name</b></td><td><code>client_vpn_authorization_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.client_vpn_authorization_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | A brief description of the authorization rule. |
| `status` | `object` | Describes the state of an authorization rule. |
| `accessAll` | `boolean` | Indicates whether the authorization rule grants access to all clients. |
| `clientVpnEndpointId` | `string` | The ID of the Client VPN endpoint with which the authorization rule is associated. |
| `destinationCidr` | `string` | The IPv4 address range, in CIDR notation, of the network to which the authorization rule applies. |
| `groupId` | `string` | The ID of the Active Directory group to which the authorization rule grants access. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `client_vpn_authorization_rules_Describe` | `SELECT` | `ClientVpnEndpointId` |
