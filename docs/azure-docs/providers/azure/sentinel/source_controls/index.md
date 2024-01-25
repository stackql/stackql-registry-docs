---
title: source_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - source_controls
  - sentinel
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
<tr><td><b>Name</b></td><td><code>source_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sentinel.source_controls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `properties` | `object` | Describes source control properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, sourceControlId, subscriptionId, workspaceName` | Gets a source control byt its identifier. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all source controls, without source control items. |
| `create` | `INSERT` | `resourceGroupName, sourceControlId, subscriptionId, workspaceName, data__properties` | Creates a source control. |
| `delete` | `DELETE` | `resourceGroupName, sourceControlId, subscriptionId, workspaceName, data__properties` | Delete a source control. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Gets all source controls, without source control items. |
