---
title: integration_runtime_auth_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtime_auth_keys
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
<tr><td><b>Name</b></td><td><code>integration_runtime_auth_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.integration_runtime_auth_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `authKey1` | `string` | The primary integration runtime authentication key. |
| `authKey2` | `string` | The secondary integration runtime authentication key. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IntegrationRuntimeAuthKeys_List` | `SELECT` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | List authentication keys in an integration runtime |
| `IntegrationRuntimeAuthKeys_Regenerate` | `EXEC` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Regenerate the authentication key for an integration runtime |
