---
title: instance_uefi_data
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_uefi_data
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
<tr><td><b>Name</b></td><td><code>instance_uefi_data</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.instance_uefi_data</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `instanceId` | `string` | The ID of the instance from which to retrieve the UEFI data. |
| `uefiData` | `string` | Base64 representation of the non-volatile UEFI variable store. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `instance_uefi_data_Get` | `SELECT` | `InstanceId` |
