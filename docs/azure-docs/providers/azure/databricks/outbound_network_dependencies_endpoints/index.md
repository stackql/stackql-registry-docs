---
title: outbound_network_dependencies_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - outbound_network_dependencies_endpoints
  - databricks
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
<tr><td><b>Name</b></td><td><code>outbound_network_dependencies_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.databricks.outbound_network_dependencies_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `endpoints` | `array` | The endpoints that Workspace connect to |
| `category` | `string` | The category of endpoints accessed by the Workspace, e.g. azure-storage, azure-mysql, etc. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `OutboundNetworkDependenciesEndpoints_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
