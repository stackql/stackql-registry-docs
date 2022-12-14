---
title: integration_runtime_status
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtime_status
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
<tr><td><b>Name</b></td><td><code>integration_runtime_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.integration_runtime_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The integration runtime name. |
| `properties` | `object` | Integration runtime status. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `IntegrationRuntimeStatus_Get` | `SELECT` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` |
