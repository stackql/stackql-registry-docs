---
title: principal_id_format
hide_title: false
hide_table_of_contents: false
keywords:
  - principal_id_format
  - ec2_api
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
<tr><td><b>Name</b></td><td><code>principal_id_format</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2_api.principal_id_format</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `arn` | `string` | PrincipalIdFormatARN description |
| `statusSet` | `array` | PrincipalIdFormatStatuses description |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `principal_id_format_Describe` | `SELECT` | `region` |
