---
title: private_clouds
hide_title: false
hide_table_of_contents: false
keywords:
  - private_clouds
  - vmware
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>private_clouds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.vmware.private_clouds</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for the virtual machine. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of a private cloud resource |
| `sku` | `object` | The resource model definition representing SKU |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `privateCloudName, resourceGroupName, subscriptionId` |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` |
| `create_or_update` | `INSERT` | `privateCloudName, resourceGroupName, subscriptionId, data__location, data__sku` |
| `delete` | `DELETE` | `privateCloudName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` |
| `_list_in_subscription` | `EXEC` | `subscriptionId` |
| `list_in_subscription` | `EXEC` | `subscriptionId` |
| `rotate_nsxt_password` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId` |
| `rotate_vcenter_password` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId` |
| `update` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId` |
