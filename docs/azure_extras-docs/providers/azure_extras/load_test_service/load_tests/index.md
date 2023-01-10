---
title: load_tests
hide_title: false
hide_table_of_contents: false
keywords:
  - load_tests
  - load_test_service
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
<tr><td><b>Name</b></td><td><code>load_tests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.load_test_service.load_tests</code></td></tr>
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
| `LoadTests_Get` | `SELECT` | `loadTestName, resourceGroupName, subscriptionId` | Get a LoadTest resource. |
| `LoadTests_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists loadtest resources in a resource group. |
| `LoadTests_ListBySubscription` | `SELECT` | `subscriptionId` | Lists loadtests resources in a subscription. |
| `LoadTests_CreateOrUpdate` | `INSERT` | `loadTestName, resourceGroupName, subscriptionId` | Create or update LoadTest resource. |
| `LoadTests_Delete` | `DELETE` | `loadTestName, resourceGroupName, subscriptionId` | Delete a LoadTest resource. |
| `LoadTests_Update` | `EXEC` | `loadTestName, resourceGroupName, subscriptionId` | Update a loadtest resource. |
