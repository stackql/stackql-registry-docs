---
title: integration_account_assemblies
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_assemblies
  - logic_apps
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
<tr><td><b>Name</b></td><td><code>integration_account_assemblies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.integration_account_assemblies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the resource name. |
| `location` | `string` | The resource location. |
| `properties` | `object` | The assembly properties definition. |
| `tags` | `object` | The resource tags. |
| `type` | `string` | Gets the resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, assemblyArtifactName, integrationAccountName, resourceGroupName, subscriptionId` | Get an assembly for an integration account. |
| `list` | `SELECT` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | List the assemblies for an integration account. |
| `create_or_update` | `INSERT` | `api-version, assemblyArtifactName, integrationAccountName, resourceGroupName, subscriptionId, data__properties` | Create or update an assembly for an integration account. |
| `delete` | `DELETE` | `api-version, assemblyArtifactName, integrationAccountName, resourceGroupName, subscriptionId` | Delete an assembly for an integration account. |
| `_list` | `EXEC` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | List the assemblies for an integration account. |
