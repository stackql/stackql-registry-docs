---
title: resource_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_pools
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
<tr><td><b>Name</b></td><td><code>resource_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.vmware_cloud_simple.resource_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | resource pool id (privateCloudId:vsphereId) |
| `name` | `string` | &#123;ResourcePoolName&#125; |
| `properties` | `object` | Properties of resource pool |
| `type` | `string` | &#123;resourceProviderNamespace&#125;/&#123;resourceType&#125; |
| `location` | `string` | Azure region |
| `privateCloudId` | `string` | The Private Cloud Id |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ResourcePools_Get` | `SELECT` | `api-version, pcName, regionId, resourcePoolName, subscriptionId` | Returns resource pool templates by its name |
| `ResourcePools_List` | `SELECT` | `api-version, pcName, regionId, subscriptionId` | Returns list of resource pools in region for private cloud |
