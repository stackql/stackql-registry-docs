---
title: private_clouds
hide_title: false
hide_table_of_contents: false
keywords:
  - private_clouds
  - vmware
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.vmware.private_clouds</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Identity for the virtual machine. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of a private cloud resource |
| `sku` | `object` | The resource model definition representing SKU |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `PrivateClouds_Get` | `SELECT` | `privateCloudName, resourceGroupName, subscriptionId` |
| `PrivateClouds_List` | `SELECT` | `resourceGroupName, subscriptionId` |
| `PrivateClouds_CreateOrUpdate` | `INSERT` | `privateCloudName, resourceGroupName, subscriptionId, data__location, data__sku` |
| `PrivateClouds_Delete` | `DELETE` | `privateCloudName, resourceGroupName, subscriptionId` |
| `PrivateClouds_ListAdminCredentials` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId` |
| `PrivateClouds_ListInSubscription` | `EXEC` | `subscriptionId` |
| `PrivateClouds_RotateNsxtPassword` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId` |
| `PrivateClouds_RotateVcenterPassword` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId` |
| `PrivateClouds_Update` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId` |
