---
title: outbound_network_dependencies_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - outbound_network_dependencies_endpoints
  - api_management
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
<tr><td><b>Id</b></td><td><code>azure.api_management.outbound_network_dependencies_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `category` | `string` | The type of service accessed by the Api Management Service, e.g., Azure Storage, Azure SQL Database, and Azure Active Directory. |
| `endpoints` | `array` | The endpoints that the Api Management Service reaches the service at. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `OutboundNetworkDependenciesEndpoints_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` |
