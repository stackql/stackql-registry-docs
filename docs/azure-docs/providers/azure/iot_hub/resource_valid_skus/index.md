---
title: resource_valid_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_valid_skus
  - iot_hub
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
<tr><td><b>Name</b></td><td><code>resource_valid_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_hub.resource_valid_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `capacity` | `object` | IoT Hub capacity information. |
| `resourceType` | `string` | The type of the resource. |
| `sku` | `object` | Information about the SKU of the IoT hub. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` |
| `_get` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` |
