---
title: dedicated_cloud_services
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_cloud_services
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
<tr><td><b>Name</b></td><td><code>dedicated_cloud_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.vmware_cloud_simple.dedicated_cloud_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/dedicatedCloudServices/&#123;dedicatedCloudServiceName&#125; |
| `name` | `string` | &#123;dedicatedCloudServiceName&#125; |
| `tags` | `object` | Tags model |
| `type` | `string` | &#123;resourceProviderNamespace&#125;/&#123;resourceType&#125; |
| `location` | `string` | Azure region |
| `properties` | `object` | Properties of dedicated cloud service |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DedicatedCloudServices_Get` | `SELECT` | `api-version, dedicatedCloudServiceName, resourceGroupName, subscriptionId` | Returns Dedicate Cloud Service |
| `DedicatedCloudServices_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Returns list of dedicated cloud services within a resource group |
| `DedicatedCloudServices_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | Returns list of dedicated cloud services within a subscription |
| `DedicatedCloudServices_CreateOrUpdate` | `INSERT` | `api-version, dedicatedCloudServiceName, resourceGroupName, subscriptionId, data__location` | Create dedicate cloud service |
| `DedicatedCloudServices_Delete` | `DELETE` | `api-version, dedicatedCloudServiceName, resourceGroupName, subscriptionId` | Delete dedicate cloud service |
| `DedicatedCloudServices_Update` | `EXEC` | `api-version, dedicatedCloudServiceName, resourceGroupName, subscriptionId` | Patch dedicated cloud service's properties |
