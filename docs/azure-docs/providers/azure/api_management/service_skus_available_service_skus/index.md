---
title: service_skus_available_service_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - service_skus_available_service_skus
  - api_management
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
<tr><td><b>Name</b></td><td><code>service_skus_available_service_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.service_skus_available_service_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `capacity` | `object` | Describes scaling information of a SKU. |
| `resourceType` | `string` | The type of resource the SKU applies to. |
| `sku` | `object` | Describes an available API Management SKU. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` |
| `_list` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` |
