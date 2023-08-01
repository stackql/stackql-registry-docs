---
title: assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - assignments
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
<tr><td><b>Name</b></td><td><code>assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.blueprint.assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Managed identity generic object. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Detailed properties for a blueprint assignment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Assignments_Get` | `SELECT` | `assignmentName, resourceScope` | Get a blueprint assignment. |
| `Assignments_List` | `SELECT` | `resourceScope` | List blueprint assignments within a subscription or a management group. |
| `Assignments_CreateOrUpdate` | `INSERT` | `assignmentName, resourceScope, data__identity, data__properties` | Create or update a blueprint assignment. |
| `Assignments_Delete` | `DELETE` | `assignmentName, resourceScope` | Delete a blueprint assignment. |
| `Assignments_WhoIsBlueprint` | `EXEC` | `assignmentName, resourceScope` | Get Blueprints service SPN objectId |
