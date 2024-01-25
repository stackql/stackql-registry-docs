---
title: blueprints
hide_title: false
hide_table_of_contents: false
keywords:
  - blueprints
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
<tr><td><b>Name</b></td><td><code>blueprints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.blueprints.blueprints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | String Id used to locate any resource on Azure. |
| `name` | `string` | Name of this resource. |
| `properties` | `object` | Schema for blueprint definition properties. |
| `type` | `string` | Type of this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `blueprintName, resourceScope` | Get a blueprint definition. |
| `list` | `SELECT` | `resourceScope` | List blueprint definitions. |
| `create_or_update` | `INSERT` | `blueprintName, resourceScope, data__properties` | Create or update a blueprint definition. |
| `delete` | `DELETE` | `blueprintName, resourceScope` | Delete a blueprint definition. |
| `_list` | `EXEC` | `resourceScope` | List blueprint definitions. |
