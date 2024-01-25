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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `profileName, resourceGroupName, secretName, subscriptionId` | Gets an existing Secret within a profile. |
| `list_by_profile` | `SELECT` | `profileName, resourceGroupName, subscriptionId` | Lists existing AzureFrontDoor secrets. |
| `create` | `INSERT` | `profileName, resourceGroupName, secretName, subscriptionId` | Creates a new Secret within the specified profile. |
| `delete` | `DELETE` | `profileName, resourceGroupName, secretName, subscriptionId` | Deletes an existing Secret within profile. |
| `_list_by_profile` | `EXEC` | `profileName, resourceGroupName, subscriptionId` | Lists existing AzureFrontDoor secrets. |
