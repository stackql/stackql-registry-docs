---
title: afd_custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - afd_custom_domains
  - cdn
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
<tr><td><b>Name</b></td><td><code>afd_custom_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.afd_custom_domains</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AFDCustomDomains_Get` | `SELECT` | `customDomainName, profileName, resourceGroupName, subscriptionId` | Gets an existing AzureFrontDoor domain with the specified domain name under the specified subscription, resource group and profile. |
| `AFDCustomDomains_ListByProfile` | `SELECT` | `profileName, resourceGroupName, subscriptionId` | Lists existing AzureFrontDoor domains. |
| `AFDCustomDomains_Create` | `INSERT` | `customDomainName, profileName, resourceGroupName, subscriptionId` | Creates a new domain within the specified profile. |
| `AFDCustomDomains_Delete` | `DELETE` | `customDomainName, profileName, resourceGroupName, subscriptionId` | Deletes an existing AzureFrontDoor domain with the specified domain name under the specified subscription, resource group and profile. |
| `AFDCustomDomains_RefreshValidationToken` | `EXEC` | `customDomainName, profileName, resourceGroupName, subscriptionId` | Updates the domain validation token. |
| `AFDCustomDomains_Update` | `EXEC` | `customDomainName, profileName, resourceGroupName, subscriptionId` | Updates an existing domain within a profile. |
