---
title: elastic_gpus
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_gpus
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
<tr><td><b>Name</b></td><td><code>elastic_gpus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.elastic_gpus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `instanceId` | `string` | The ID of the instance to which the Elastic Graphics accelerator is attached. |
| `tagSet` | `array` | The tags assigned to the Elastic Graphics accelerator. |
| `availabilityZone` | `string` | The Availability Zone in the which the Elastic Graphics accelerator resides. |
| `elasticGpuHealth` | `object` | Describes the status of an Elastic Graphics accelerator. |
| `elasticGpuId` | `string` | The ID of the Elastic Graphics accelerator. |
| `elasticGpuState` | `string` | The state of the Elastic Graphics accelerator. |
| `elasticGpuType` | `string` | The type of Elastic Graphics accelerator. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `elastic_gpus_Describe` | `SELECT` |  |
