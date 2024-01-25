---
title: workspaces_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces_keys
  - ml_services
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
<tr><td><b>Name</b></td><td><code>workspaces_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ml_services.workspaces_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `appInsightsInstrumentationKey` | `string` | The access key of the workspace app insights |
| `containerRegistryCredentials` | `object` |  |
| `notebookAccessKeys` | `object` |  |
| `userStorageArmId` | `string` | The arm Id key of the workspace storage |
| `userStorageKey` | `string` | The access key of the workspace storage |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
