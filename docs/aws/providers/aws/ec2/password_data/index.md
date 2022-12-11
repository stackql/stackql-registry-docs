---
title: password_data
hide_title: false
hide_table_of_contents: false
keywords:
  - password_data
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
<tr><td><b>Name</b></td><td><code>password_data</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.password_data</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `timestamp` | `string` | The time the data was last updated. |
| `instanceId` | `string` | The ID of the Windows instance. |
| `passwordData` | `string` | The password of the instance. Returns an empty string if the password is not available. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `password_data_Get` | `SELECT` | `InstanceId` |
