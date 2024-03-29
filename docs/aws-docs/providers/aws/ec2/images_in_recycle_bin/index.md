---
title: images_in_recycle_bin
hide_title: false
hide_table_of_contents: false
keywords:
  - images_in_recycle_bin
  - ec2
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
<tr><td><b>Name</b></td><td><code>images_in_recycle_bin</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.images_in_recycle_bin</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the AMI. |
| `description` | `string` | The description of the AMI. |
| `imageId` | `string` | The ID of the AMI. |
| `recycleBinEnterTime` | `string` | The date and time when the AMI entered the Recycle Bin. |
| `recycleBinExitTime` | `string` | The date and time when the AMI is to be permanently deleted from the Recycle Bin. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `images_in_recycle_bin_List` | `SELECT` | `region` |
