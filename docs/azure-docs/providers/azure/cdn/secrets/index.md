---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
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
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.secrets</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Secrets_Get` | `SELECT` | `profileName, resourceGroupName, secretName, subscriptionId` | Gets an existing Secret within a profile. |
| `Secrets_ListByProfile` | `SELECT` | `profileName, resourceGroupName, subscriptionId` | Lists existing AzureFrontDoor secrets. |
| `Secrets_Create` | `INSERT` | `profileName, resourceGroupName, secretName, subscriptionId` | Creates a new Secret within the specified profile. |
| `Secrets_Delete` | `DELETE` | `profileName, resourceGroupName, secretName, subscriptionId` | Deletes an existing Secret within profile. |
