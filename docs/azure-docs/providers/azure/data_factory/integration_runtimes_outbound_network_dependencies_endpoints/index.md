---
title: integration_runtimes_outbound_network_dependencies_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtimes_outbound_network_dependencies_endpoints
  - data_factory
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
<tr><td><b>Name</b></td><td><code>integration_runtimes_outbound_network_dependencies_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.integration_runtimes_outbound_network_dependencies_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `category` | `string` | The category of outbound network dependency. |
| `endpoints` | `array` | The endpoints for outbound network dependency. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` |
