---
title: dedicated_cloud_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_cloud_nodes
  - vmware_cloud_simple
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
<tr><td><b>Name</b></td><td><code>dedicated_cloud_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.vmware_cloud_simple.dedicated_cloud_nodes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/dedicatedCloudNodes/&#123;dedicatedCloudNodeName&#125; |
| `name` | `string` | &#123;dedicatedCloudNodeName&#125; |
| `location` | `string` | Azure region |
| `properties` | `object` | Properties of dedicated cloud node |
| `sku` | `object` | The purchase SKU for CloudSimple paid resources |
| `tags` | `object` | Tags model |
| `type` | `string` | &#123;resourceProviderNamespace&#125;/&#123;resourceType&#125; |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, dedicatedCloudNodeName, resourceGroupName, subscriptionId` | Returns dedicated cloud node |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Returns list of dedicate cloud nodes within resource group |
| `list_by_subscription` | `SELECT` | `api-version, subscriptionId` | Returns list of dedicate cloud nodes within subscription |
| `create_or_update` | `INSERT` | `Referer, api-version, dedicatedCloudNodeName, resourceGroupName, subscriptionId, data__location` | Returns dedicated cloud node by its name |
| `delete` | `DELETE` | `api-version, dedicatedCloudNodeName, resourceGroupName, subscriptionId` | Delete dedicated cloud node |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | Returns list of dedicate cloud nodes within resource group |
| `_list_by_subscription` | `EXEC` | `api-version, subscriptionId` | Returns list of dedicate cloud nodes within subscription |
| `update` | `EXEC` | `api-version, dedicatedCloudNodeName, resourceGroupName, subscriptionId` | Patches dedicated node properties |
