---
title: integration_runtime_object_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtime_object_metadata
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
<tr><td><b>Name</b></td><td><code>integration_runtime_object_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.integration_runtime_object_metadata</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | The link to the next page of results, if any remaining results exist. |
| `value` | `array` | List of SSIS object metadata. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Get object metadata from an integration runtime |
| `refresh` | `EXEC` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Refresh the object metadata in an integration runtime |
