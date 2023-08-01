---
title: php_workloads
hide_title: false
hide_table_of_contents: false
keywords:
  - php_workloads
  - workloads
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
<tr><td><b>Name</b></td><td><code>php_workloads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.workloads.php_workloads</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | PHP workload resource properties |
| `sku` | `object` | The resource model definition representing SKU |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Identity for the resource. Currently not supported |
| `kind` | `string` | Indicates which kind of php workload this resource represent e.g WordPress |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PhpWorkloads_Get` | `SELECT` | `phpWorkloadName, resourceGroupName, subscriptionId` | Gets the PHP workload resource. |
| `PhpWorkloads_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists PHP workload resources in a resource group. |
| `PhpWorkloads_ListBySubscription` | `SELECT` | `subscriptionId` | Lists PHP workload resources for a subscription. |
| `PhpWorkloads_CreateOrUpdate` | `INSERT` | `phpWorkloadName, resourceGroupName, subscriptionId, data__kind` | Create or updated PHP workload resource. |
| `PhpWorkloads_Delete` | `DELETE` | `phpWorkloadName, resourceGroupName, subscriptionId` | Delete PHP workload resource. |
| `PhpWorkloads_Update` | `EXEC` | `phpWorkloadName, resourceGroupName, subscriptionId` | Update PHP workload resource. |
