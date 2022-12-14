---
title: server_azure_ad_administrators
hide_title: false
hide_table_of_contents: false
keywords:
  - server_azure_ad_administrators
  - sql
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
<tr><td><b>Name</b></td><td><code>server_azure_ad_administrators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.server_azure_ad_administrators</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerAzureADAdministrators_Get` | `SELECT` | `administratorName, resourceGroupName, serverName, subscriptionId` | Gets a Azure Active Directory administrator. |
| `ServerAzureADAdministrators_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of Azure Active Directory administrators in a server. |
| `ServerAzureADAdministrators_CreateOrUpdate` | `INSERT` | `administratorName, resourceGroupName, serverName, subscriptionId` | Creates or updates an existing Azure Active Directory administrator. |
| `ServerAzureADAdministrators_Delete` | `DELETE` | `administratorName, resourceGroupName, serverName, subscriptionId` | Deletes the Azure Active Directory administrator with the given name. |
