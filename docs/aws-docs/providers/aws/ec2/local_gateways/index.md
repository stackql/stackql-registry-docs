---
title: local_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateways
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
<tr><td><b>Name</b></td><td><code>local_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.local_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `localGatewayId` | `string` | The ID of the local gateway. |
| `outpostArn` | `string` | The Amazon Resource Name (ARN) of the Outpost. |
| `ownerId` | `string` | The ID of the Amazon Web Services account that owns the local gateway. |
| `state` | `string` | The state of the local gateway. |
| `tagSet` | `array` | The tags assigned to the local gateway. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `local_gateways_Describe` | `SELECT` |  |
