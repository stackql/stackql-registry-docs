---
title: security_groups_to_client_vpn_target_network
hide_title: false
hide_table_of_contents: false
keywords:
  - security_groups_to_client_vpn_target_network
  - ec2_api
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_groups_to_client_vpn_target_network</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2_api.security_groups_to_client_vpn_target_network</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `security_groups_to_client_vpn_target_network_Apply` | `EXEC` | `ClientVpnEndpointId, SecurityGroupId, VpcId, region` |
