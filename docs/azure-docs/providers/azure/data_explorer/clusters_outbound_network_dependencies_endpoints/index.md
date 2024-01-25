---
title: clusters_outbound_network_dependencies_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_outbound_network_dependencies_endpoints
  - data_explorer
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
<tr><td><b>Name</b></td><td><code>clusters_outbound_network_dependencies_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_explorer.clusters_outbound_network_dependencies_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Endpoints accessed for a common purpose that the Kusto Service Environment requires outbound network access to. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` |
