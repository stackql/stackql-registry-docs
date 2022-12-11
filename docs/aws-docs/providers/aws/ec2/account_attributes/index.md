---
title: account_attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - account_attributes
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
<tr><td><b>Name</b></td><td><code>account_attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.account_attributes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `attributeValueSet` | `array` | The values for the account attribute. |
| `attributeName` | `string` | The name of the account attribute. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `account_attributes_Describe` | `SELECT` |  |
