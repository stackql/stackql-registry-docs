---
title: data_types
hide_title: false
hide_table_of_contents: false
keywords:
  - data_types
  - network_analytics
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
<tr><td><b>Name</b></td><td><code>data_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network_analytics.data_types</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dataProductName, dataTypeName, resourceGroupName, subscriptionId` | Retrieve data type resource. |
| `list_by_data_product` | `SELECT` | `dataProductName, resourceGroupName, subscriptionId` | List data type by parent resource. |
| `create` | `INSERT` | `dataProductName, dataTypeName, resourceGroupName, subscriptionId` | Create data type resource. |
| `delete` | `DELETE` | `dataProductName, dataTypeName, resourceGroupName, subscriptionId` | Delete data type resource. |
| `_list_by_data_product` | `EXEC` | `dataProductName, resourceGroupName, subscriptionId` | List data type by parent resource. |
| `generate_storage_container_sas_token` | `EXEC` | `dataProductName, dataTypeName, resourceGroupName, subscriptionId, data__expiryTimeStamp, data__ipAddress, data__startTimeStamp` | Generate sas token for storage container. |
| `update` | `EXEC` | `dataProductName, dataTypeName, resourceGroupName, subscriptionId` | Update data type resource. |
