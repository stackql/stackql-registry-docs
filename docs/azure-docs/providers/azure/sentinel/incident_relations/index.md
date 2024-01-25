---
title: incident_relations
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_relations
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
<tr><td><b>Name</b></td><td><code>incident_relations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sentinel.incident_relations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `properties` | `object` | Relation property bag. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `incidentId, relationName, resourceGroupName, subscriptionId, workspaceName` | Gets a relation for a given incident. |
| `list` | `SELECT` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Gets all relations for a given incident. |
| `create_or_update` | `INSERT` | `incidentId, relationName, resourceGroupName, subscriptionId, workspaceName` | Creates or updates a relation for a given incident. |
| `delete` | `DELETE` | `incidentId, relationName, resourceGroupName, subscriptionId, workspaceName` | Deletes a relation for a given incident. |
| `_list` | `EXEC` | `incidentId, resourceGroupName, subscriptionId, workspaceName` | Gets all relations for a given incident. |
