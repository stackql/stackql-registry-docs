---
title: azure_ad_only_authentications
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_ad_only_authentications
  - synapse
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
<tr><td><b>Name</b></td><td><code>azure_ad_only_authentications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.azure_ad_only_authentications</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AzureADOnlyAuthentications_Get` | `SELECT` | `azureADOnlyAuthenticationName, resourceGroupName, subscriptionId, workspaceName` | Gets a Azure Active Directory only authentication property |
| `AzureADOnlyAuthentications_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets a list of Azure Active Directory only authentication property for a workspace |
| `AzureADOnlyAuthentications_Create` | `INSERT` | `azureADOnlyAuthenticationName, resourceGroupName, subscriptionId, workspaceName` | Create or Update a Azure Active Directory only authentication property for the workspaces |
