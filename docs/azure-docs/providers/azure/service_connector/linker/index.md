---
title: linker
hide_title: false
hide_table_of_contents: false
keywords:
  - linker
  - service_connector
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
<tr><td><b>Name</b></td><td><code>linker</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_connector.linker</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The properties of the Linker. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `linkerName, resourceUri` | Returns Linker resource for a given name. |
| `list` | `SELECT` | `resourceUri` | Returns list of Linkers which connects to the resource. which supports to config both application and target service during the resource provision. |
| `create_or_update` | `INSERT` | `linkerName, resourceUri, data__properties` | Create or update Linker resource. |
| `delete` | `DELETE` | `linkerName, resourceUri` | Delete a Linker. |
| `_list` | `EXEC` | `resourceUri` | Returns list of Linkers which connects to the resource. which supports to config both application and target service during the resource provision. |
| `update` | `EXEC` | `linkerName, resourceUri` | Operation to update an existing Linker. |
| `validate` | `EXEC` | `linkerName, resourceUri` | Validate a Linker. |
