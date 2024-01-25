---
title: environments_worker_pool_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_worker_pool_skus
  - app_service
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
<tr><td><b>Name</b></td><td><code>environments_worker_pool_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.environments_worker_pool_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `capacity` | `object` | Description of the App Service plan scale options. |
| `resourceType` | `string` | Resource type that this SKU applies to. |
| `sku` | `object` | Description of a SKU for a scalable resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `name, resourceGroupName, subscriptionId, workerPoolName` |
| `_list` | `EXEC` | `name, resourceGroupName, subscriptionId, workerPoolName` |
