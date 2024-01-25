---
title: online_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - online_endpoints
  - ml_services
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
<tr><td><b>Name</b></td><td><code>online_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ml_services.online_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `kind` | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Online endpoint configuration |
| `sku` | `object` | The resource model definition representing SKU |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `endpointName, resourceGroupName, subscriptionId, workspaceName` |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
| `create_or_update` | `INSERT` | `endpointName, resourceGroupName, subscriptionId, workspaceName, data__location, data__properties` |
| `delete` | `DELETE` | `endpointName, resourceGroupName, subscriptionId, workspaceName` |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` |
| `regenerate_keys` | `EXEC` | `endpointName, resourceGroupName, subscriptionId, workspaceName, data__keyType` |
| `update` | `EXEC` | `endpointName, resourceGroupName, subscriptionId, workspaceName` |
