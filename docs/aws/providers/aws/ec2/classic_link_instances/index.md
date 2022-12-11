---
title: classic_link_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - classic_link_instances
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
<tr><td><b>Name</b></td><td><code>classic_link_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.classic_link_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `groupSet` | `array` | A list of security groups. |
| `instanceId` | `string` | The ID of the instance. |
| `tagSet` | `array` | Any tags assigned to the instance. |
| `vpcId` | `string` | The ID of the VPC. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `classic_link_instances_Describe` | `SELECT` |  |
