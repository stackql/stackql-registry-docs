---
title: workflows
hide_title: false
hide_table_of_contents: false
keywords:
  - workflows
  - storage_sync
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
<tr><td><b>Name</b></td><td><code>workflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_sync.workflows</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, storageSyncServiceName, subscriptionId, workflowId` | Get Workflows resource |
| `list_by_storage_sync_service` | `SELECT` | `resourceGroupName, storageSyncServiceName, subscriptionId` | Get a Workflow List |
| `_list_by_storage_sync_service` | `EXEC` | `resourceGroupName, storageSyncServiceName, subscriptionId` | Get a Workflow List |
| `abort` | `EXEC` | `resourceGroupName, storageSyncServiceName, subscriptionId, workflowId` | Abort the given workflow. |
