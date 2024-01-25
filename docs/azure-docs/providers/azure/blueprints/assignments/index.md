---
title: assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - assignments
  - blueprints
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
<tr><td><b>Id</b></td><td><code>azure.blueprints.assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed identity generic object. |
| `location` | `string` | The location of this blueprint assignment. |
| `properties` | `object` | Detailed properties for a blueprint assignment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `assignmentName, resourceScope` | Get a blueprint assignment. |
| `list` | `SELECT` | `resourceScope` | List blueprint assignments within a subscription or a management group. |
| `create_or_update` | `INSERT` | `assignmentName, resourceScope, data__identity, data__properties` | Create or update a blueprint assignment. |
| `delete` | `DELETE` | `assignmentName, resourceScope` | Delete a blueprint assignment. |
| `_list` | `EXEC` | `resourceScope` | List blueprint assignments within a subscription or a management group. |
| `who_is_blueprint` | `EXEC` | `assignmentName, resourceScope` | Get Blueprints service SPN objectId |
