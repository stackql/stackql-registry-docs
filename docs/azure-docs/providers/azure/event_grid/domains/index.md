---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - event_grid
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
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of the Event Grid Domain Resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Tags of the resource. |
| `identity` | `object` | The identity information for the resource. |
| `location` | `string` | Location of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Domains_Get` | `SELECT` | `domainName, resourceGroupName, subscriptionId` | Get properties of a domain. |
| `Domains_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all the domains under a resource group. |
| `Domains_ListBySubscription` | `SELECT` | `subscriptionId` | List all the domains under an Azure subscription. |
| `Domains_CreateOrUpdate` | `INSERT` | `domainName, resourceGroupName, subscriptionId` | Asynchronously creates or updates a new domain with the specified parameters. |
| `Domains_Delete` | `DELETE` | `domainName, resourceGroupName, subscriptionId` | Delete existing domain. |
| `Domains_ListSharedAccessKeys` | `EXEC` | `domainName, resourceGroupName, subscriptionId` | List the two keys used to publish to a domain. |
| `Domains_RegenerateKey` | `EXEC` | `domainName, resourceGroupName, subscriptionId, data__keyName` | Regenerate a shared access key for a domain. |
| `Domains_Update` | `EXEC` | `domainName, resourceGroupName, subscriptionId` | Asynchronously updates a domain with the specified parameters. |
