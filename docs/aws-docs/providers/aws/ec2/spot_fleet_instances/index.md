---
title: spot_fleet_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - spot_fleet_instances
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
<tr><td><b>Name</b></td><td><code>spot_fleet_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.spot_fleet_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `instanceId` | `string` | The ID of the instance. |
| `instanceType` | `string` | The instance type. |
| `spotInstanceRequestId` | `string` | The ID of the Spot Instance request. |
| `instanceHealth` | `string` | The health status of the instance. If the status of either the instance status check or the system status check is &lt;code&gt;impaired&lt;/code&gt;, the health status of the instance is &lt;code&gt;unhealthy&lt;/code&gt;. Otherwise, the health status is &lt;code&gt;healthy&lt;/code&gt;. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `spot_fleet_instances_Describe` | `SELECT` | `SpotFleetRequestId` |
