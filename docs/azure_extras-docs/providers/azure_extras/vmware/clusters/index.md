---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.vmware.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | The properties of a cluster |
| `sku` | `object` | The resource model definition representing SKU |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Clusters_Get` | `SELECT` | `clusterName, privateCloudName, resourceGroupName, subscriptionId` |
| `Clusters_List` | `SELECT` | `privateCloudName, resourceGroupName, subscriptionId` |
| `Clusters_CreateOrUpdate` | `INSERT` | `clusterName, privateCloudName, resourceGroupName, subscriptionId, data__sku` |
| `Clusters_Delete` | `DELETE` | `clusterName, privateCloudName, resourceGroupName, subscriptionId` |
| `Clusters_Update` | `EXEC` | `clusterName, privateCloudName, resourceGroupName, subscriptionId` |
