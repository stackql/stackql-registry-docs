---
title: dedicated_cloud_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_cloud_nodes
  - vmware_cloud_simple
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
<tr><td><b>Name</b></td><td><code>dedicated_cloud_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.vmware_cloud_simple.dedicated_cloud_nodes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/dedicatedCloudNodes/&#123;dedicatedCloudNodeName&#125; |
| `name` | `string` | &#123;dedicatedCloudNodeName&#125; |
| `properties` | `object` | Properties of dedicated cloud node |
| `sku` | `object` | The purchase SKU for CloudSimple paid resources |
| `tags` | `object` | Tags model |
| `type` | `string` | &#123;resourceProviderNamespace&#125;/&#123;resourceType&#125; |
| `location` | `string` | Azure region |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DedicatedCloudNodes_Get` | `SELECT` | `api-version, dedicatedCloudNodeName, resourceGroupName, subscriptionId` | Returns dedicated cloud node |
| `DedicatedCloudNodes_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Returns list of dedicate cloud nodes within resource group |
| `DedicatedCloudNodes_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | Returns list of dedicate cloud nodes within subscription |
| `DedicatedCloudNodes_CreateOrUpdate` | `INSERT` | `Referer, api-version, dedicatedCloudNodeName, resourceGroupName, subscriptionId, data__location` | Returns dedicated cloud node by its name |
| `DedicatedCloudNodes_Delete` | `DELETE` | `api-version, dedicatedCloudNodeName, resourceGroupName, subscriptionId` | Delete dedicated cloud node |
| `DedicatedCloudNodes_Update` | `EXEC` | `api-version, dedicatedCloudNodeName, resourceGroupName, subscriptionId` | Patches dedicated node properties |
