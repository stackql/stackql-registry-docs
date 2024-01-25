---
title: associations
hide_title: false
hide_table_of_contents: false
keywords:
  - associations
  - custom_providers
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
<tr><td><b>Name</b></td><td><code>associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.custom_providers.associations</code></td></tr>
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
| `get` | `SELECT` | `associationName, scope` | Get an association. |
| `create_or_update` | `INSERT` | `associationName, scope` | Create or update an association. |
| `delete` | `DELETE` | `associationName, scope` | Delete an association. |
