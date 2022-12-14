---
title: assignment_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - assignment_operations
  - blueprint
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assignment_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.blueprint.assignment_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | String Id used to locate any resource on Azure. |
| `name` | `string` | Name of this resource. |
| `properties` | `object` | Properties of AssignmentOperation. |
| `type` | `string` | Type of this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AssignmentOperations_Get` | `SELECT` | `assignmentName, assignmentOperationName, resourceScope` | Get a blueprint assignment operation. |
| `AssignmentOperations_List` | `SELECT` | `assignmentName, resourceScope` | List operations for given blueprint assignment within a subscription or a management group. |
