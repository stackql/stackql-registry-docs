---
title: providers
hide_title: false
hide_table_of_contents: false
keywords:
  - providers
  - attestation
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
<tr><td><b>Name</b></td><td><code>providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.attestation.providers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Status of attestation service. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `providerName, resourceGroupName, subscriptionId` | Get the status of Attestation Provider. |
| `list` | `SELECT` | `subscriptionId` | Returns a list of attestation providers in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Returns attestation providers list in a resource group. |
| `create` | `INSERT` | `providerName, resourceGroupName, subscriptionId, data__location, data__properties` | Creates or updates an Attestation Provider. |
| `delete` | `DELETE` | `providerName, resourceGroupName, subscriptionId` | Delete Attestation Service. |
| `_list` | `EXEC` | `subscriptionId` | Returns a list of attestation providers in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Returns attestation providers list in a resource group. |
| `update` | `EXEC` | `providerName, resourceGroupName, subscriptionId` | Updates the Attestation Provider. |
