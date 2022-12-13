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
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Status of attestation service. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AttestationProviders_Get` | `SELECT` | `providerName, resourceGroupName, subscriptionId` | Get the status of Attestation Provider. |
| `AttestationProviders_List` | `SELECT` | `subscriptionId` | Returns a list of attestation providers in a subscription. |
| `AttestationProviders_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Returns attestation providers list in a resource group. |
| `AttestationProviders_Create` | `INSERT` | `providerName, resourceGroupName, subscriptionId, data__location, data__properties` | Creates a new Attestation Provider. |
| `AttestationProviders_Delete` | `DELETE` | `providerName, resourceGroupName, subscriptionId` | Delete Attestation Service. |
| `AttestationProviders_GetDefaultByLocation` | `EXEC` | `location, subscriptionId` | Get the default provider by location. |
| `AttestationProviders_ListDefault` | `EXEC` | `subscriptionId` | Get the default provider |
| `AttestationProviders_Update` | `EXEC` | `providerName, resourceGroupName, subscriptionId` | Updates the Attestation Provider. |
