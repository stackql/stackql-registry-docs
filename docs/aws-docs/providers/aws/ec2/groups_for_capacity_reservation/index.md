---
title: groups_for_capacity_reservation
hide_title: false
hide_table_of_contents: false
keywords:
  - groups_for_capacity_reservation
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
<tr><td><b>Name</b></td><td><code>groups_for_capacity_reservation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.groups_for_capacity_reservation</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `groupArn` | `string` | The ARN of the resource group. |
| `ownerId` | `string` | The ID of the Amazon Web Services account that owns the resource group. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `groups_for_capacity_reservation_Get` | `SELECT` | `CapacityReservationId` |
