---
title: integration_runtime_start
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtime_start
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
<tr><td><b>Name</b></td><td><code>integration_runtime_start</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.integration_runtime_start</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The operation name. |
| `error` | `string` | The operation error message. |
| `properties` | `object` | The operation properties. |
| `status` | `string` | status of Start Integrationruntimes. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `integrationRuntimeName, integrationRuntimeOperationId, resourceGroupName, subscriptionId, workspaceName` |
