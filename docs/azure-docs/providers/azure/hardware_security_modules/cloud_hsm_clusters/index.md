---
title: cloud_hsm_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_hsm_clusters
  - hardware_security_modules
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
<tr><td><b>Name</b></td><td><code>cloud_hsm_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hardware_security_modules.cloud_hsm_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `properties` | `object` | Properties of a Cloud HSM Cluster. |
| `sku` | `object` | Cloud Hsm Cluster SKU information |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `cloudHsmClusterName, resourceGroupName, subscriptionId` | Gets the specified Cloud HSM Cluster |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | The List operation gets information about the Cloud HSM Clusters associated with the subscription and within the specified resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | The List operation gets information about the Cloud HSM Clusters associated with the subscription. |
| `create_or_update` | `INSERT` | `cloudHsmClusterName, resourceGroupName, subscriptionId` | Create or Update a Cloud HSM Cluster in the specified subscription. |
| `delete` | `DELETE` | `cloudHsmClusterName, resourceGroupName, subscriptionId` | Deletes the specified Cloud HSM Cluster |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | The List operation gets information about the Cloud HSM Clusters associated with the subscription and within the specified resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | The List operation gets information about the Cloud HSM Clusters associated with the subscription. |
| `update` | `EXEC` | `cloudHsmClusterName, resourceGroupName, subscriptionId` | Update a Cloud HSM Cluster in the specified subscription. |
