---
title: services_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - services_skus
  - data_migration
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
<tr><td><b>Name</b></td><td><code>services_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_migration.services_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `capacity` | `object` | A description of the scaling capacities of the SKU |
| `resourceType` | `string` | The resource type, including the provider namespace |
| `sku` | `object` | SKU name, tier, etc. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `api-version, groupName, serviceName, subscriptionId` |
| `_list` | `EXEC` | `api-version, groupName, serviceName, subscriptionId` |
