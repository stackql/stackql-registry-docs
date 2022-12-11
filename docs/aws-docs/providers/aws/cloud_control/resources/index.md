---
title: resources
hide_title: false
hide_table_of_contents: false
keywords:
  - resources
  - cloud_control
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
<tr><td><b>Name</b></td><td><code>resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloud_control.resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `Properties` | `string` |
| `Identifier` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_resource` | `SELECT` | `data__Identifier, data__TypeName` |
| `list_resources` | `SELECT` | `data__TypeName` |
| `create_resource` | `INSERT` | `data__DesiredState, data__TypeName` |
| `delete_resource` | `DELETE` | `data__Identifier, data__TypeName` |
| `update_resource` | `UPDATE` | `data__Identifier, data__PatchDocument, data__TypeName` |
