---
title: private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resources
  - recovery_services
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
<tr><td><b>Name</b></td><td><code>private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services.private_link_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier of the resource. |
| `name` | `string` | Name of the resource. |
| `properties` | `object` | Properties of the private link resource. |
| `type` | `string` | e.g. Microsoft.RecoveryServices/vaults/privateLinkResources |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `privateLinkResourceName, resourceGroupName, subscriptionId, vaultName` |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, vaultName` |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, vaultName` |
