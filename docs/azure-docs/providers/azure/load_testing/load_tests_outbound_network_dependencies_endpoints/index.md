---
title: load_tests_outbound_network_dependencies_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - load_tests_outbound_network_dependencies_endpoints
  - load_testing
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
<tr><td><b>Name</b></td><td><code>load_tests_outbound_network_dependencies_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.load_testing.load_tests_outbound_network_dependencies_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `category` | `string` | The type of service that Azure Load Testing connects to. |
| `endpoints` | `array` | The endpoints for this service to which the Batch service makes outbound calls. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `loadTestName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `loadTestName, resourceGroupName, subscriptionId` |
