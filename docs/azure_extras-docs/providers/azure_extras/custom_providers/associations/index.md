---
title: associations
hide_title: false
hide_table_of_contents: false
keywords:
  - associations
  - custom_providers
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.custom_providers.associations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The association id. |
| `name` | `string` | The association name. |
| `properties` | `object` | The properties of the association. |
| `type` | `string` | The association type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Associations_Get` | `SELECT` | `associationName, scope` | Get an association. |
| `Associations_ListAll` | `SELECT` | `scope` | Gets all association for the given scope. |
| `Associations_CreateOrUpdate` | `INSERT` | `associationName, scope` | Create or update an association. |
| `Associations_Delete` | `DELETE` | `associationName, scope` | Delete an association. |
