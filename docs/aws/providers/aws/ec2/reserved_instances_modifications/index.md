---
title: reserved_instances_modifications
hide_title: false
hide_table_of_contents: false
keywords:
  - reserved_instances_modifications
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
<tr><td><b>Name</b></td><td><code>reserved_instances_modifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.reserved_instances_modifications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `status` | `string` | The status of the Reserved Instances modification request. |
| `reservedInstancesSet` | `array` | The IDs of one or more Reserved Instances. |
| `effectiveDate` | `string` | The time for the modification to become effective. |
| `reservedInstancesModificationId` | `string` | A unique ID for the Reserved Instance modification. |
| `clientToken` | `string` | A unique, case-sensitive key supplied by the client to ensure that the request is idempotent. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html"&gt;Ensuring Idempotency&lt;/a&gt;. |
| `createDate` | `string` | The time when the modification request was created. |
| `modificationResultSet` | `array` | Contains target configurations along with their corresponding new Reserved Instance IDs. |
| `statusMessage` | `string` | The reason for the status. |
| `updateDate` | `string` | The time when the modification request was last updated. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `reserved_instances_modifications_Describe` | `SELECT` |  |
