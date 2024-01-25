---
title: registries
hide_title: false
hide_table_of_contents: false
keywords:
  - registries
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
<tr><td><b>Name</b></td><td><code>registries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ml_services.registries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `kind` | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Details of the Registry |
| `sku` | `object` | The resource model definition representing SKU |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `registryName, resourceGroupName, subscriptionId` |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` |
| `list_by_subscription` | `SELECT` | `subscriptionId` |
| `create_or_update` | `INSERT` | `registryName, resourceGroupName, subscriptionId, data__location, data__properties` |
| `delete` | `DELETE` | `registryName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` |
| `_list_by_subscription` | `EXEC` | `subscriptionId` |
| `remove_regions` | `EXEC` | `registryName, resourceGroupName, subscriptionId, data__location, data__properties` |
| `update` | `EXEC` | `registryName, resourceGroupName, subscriptionId` |
