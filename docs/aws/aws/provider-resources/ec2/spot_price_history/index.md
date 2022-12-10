---
title: spot_price_history
hide_title: false
hide_table_of_contents: false
keywords:
  - spot_price_history
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
<tr><td><b>Name</b></td><td><code>spot_price_history</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.spot_price_history</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `instanceType` | `string` | The instance type. |
| `productDescription` | `string` | A general description of the AMI. |
| `spotPrice` | `string` | The maximum price per hour that you are willing to pay for a Spot Instance. |
| `timestamp` | `string` | The date and time the request was created, in UTC format (for example, &lt;i&gt;YYYY&lt;/i&gt;-&lt;i&gt;MM&lt;/i&gt;-&lt;i&gt;DD&lt;/i&gt;T&lt;i&gt;HH&lt;/i&gt;:&lt;i&gt;MM&lt;/i&gt;:&lt;i&gt;SS&lt;/i&gt;Z). |
| `availabilityZone` | `string` | The Availability Zone. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `spot_price_history_Describe` | `SELECT` |  |
