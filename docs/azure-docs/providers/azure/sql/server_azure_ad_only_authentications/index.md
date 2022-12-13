---
title: server_azure_ad_only_authentications
hide_title: false
hide_table_of_contents: false
keywords:
  - server_azure_ad_only_authentications
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
<tr><td><b>Name</b></td><td><code>server_azure_ad_only_authentications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.server_azure_ad_only_authentications</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerAzureADOnlyAuthentications_Get` | `SELECT` | `authenticationName, resourceGroupName, serverName, subscriptionId` | Gets a specific Azure Active Directory only authentication property. |
| `ServerAzureADOnlyAuthentications_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of server Azure Active Directory only authentications. |
| `ServerAzureADOnlyAuthentications_CreateOrUpdate` | `INSERT` | `authenticationName, resourceGroupName, serverName, subscriptionId` | Sets Server Active Directory only authentication property or updates an existing server Active Directory only authentication property. |
| `ServerAzureADOnlyAuthentications_Delete` | `DELETE` | `authenticationName, resourceGroupName, serverName, subscriptionId` | Deletes an existing server Active Directory only authentication property. |
