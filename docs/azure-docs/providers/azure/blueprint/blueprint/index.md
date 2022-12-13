---
title: blueprint
hide_title: false
hide_table_of_contents: false
keywords:
  - blueprint
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
<tr><td><b>Name</b></td><td><code>blueprint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.blueprint.blueprint</code></td></tr>
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
| `Blueprints_Get` | `SELECT` | `blueprintName, resourceScope` | Get a blueprint definition. |
| `Blueprints_List` | `SELECT` | `resourceScope` | List blueprint definitions. |
| `Blueprints_CreateOrUpdate` | `INSERT` | `blueprintName, resourceScope, data__properties` | Create or update a blueprint definition. |
| `Blueprints_Delete` | `DELETE` | `blueprintName, resourceScope` | Delete a blueprint definition. |
