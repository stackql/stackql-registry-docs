---
title: host_reservation_offerings
hide_title: false
hide_table_of_contents: false
keywords:
  - host_reservation_offerings
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
<tr><td><b>Name</b></td><td><code>host_reservation_offerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.host_reservation_offerings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `currencyCode` | `string` | The currency of the offering. |
| `duration` | `integer` | The duration of the offering (in seconds). |
| `hourlyPrice` | `string` | The hourly price of the offering. |
| `instanceFamily` | `string` | The instance family of the offering. |
| `offeringId` | `string` | The ID of the offering. |
| `paymentOption` | `string` | The available payment option. |
| `upfrontPrice` | `string` | The upfront price of the offering. Does not apply to No Upfront offerings. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `host_reservation_offerings_Describe` | `SELECT` |  |
