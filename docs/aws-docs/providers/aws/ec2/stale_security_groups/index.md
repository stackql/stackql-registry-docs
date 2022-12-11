---
title: stale_security_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - stale_security_groups
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
<tr><td><b>Name</b></td><td><code>stale_security_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.stale_security_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The description of the security group. |
| `groupId` | `string` | The ID of the security group. |
| `groupName` | `string` | The name of the security group. |
| `staleIpPermissions` | `array` | Information about the stale inbound rules in the security group. |
| `staleIpPermissionsEgress` | `array` | Information about the stale outbound rules in the security group. |
| `vpcId` | `string` | The ID of the VPC for the security group. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `stale_security_groups_Describe` | `SELECT` | `VpcId` |
