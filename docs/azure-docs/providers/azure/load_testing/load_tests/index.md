---
title: load_tests
hide_title: false
hide_table_of_contents: false
keywords:
  - load_tests
  - load_testing
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
<tr><td><b>Name</b></td><td><code>load_tests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.load_testing.load_tests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | LoadTest resource properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `loadTestName, resourceGroupName, subscriptionId` | Get a LoadTest resource. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists loadtest resources in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists loadtests resources in a subscription. |
| `create_or_update` | `INSERT` | `loadTestName, resourceGroupName, subscriptionId` | Create or update LoadTest resource. |
| `delete` | `DELETE` | `loadTestName, resourceGroupName, subscriptionId` | Delete a LoadTest resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists loadtest resources in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists loadtests resources in a subscription. |
| `update` | `EXEC` | `loadTestName, resourceGroupName, subscriptionId` | Update a loadtest resource. |
