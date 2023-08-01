---
title: network_status
hide_title: false
hide_table_of_contents: false
keywords:
  - network_status
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
<tr><td><b>Name</b></td><td><code>network_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.network_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `connectivityStatus` | `array` | Gets the list of Connectivity Status to the Resources on which the service depends upon. |
| `dnsServers` | `array` | Gets the list of DNS servers IPV4 addresses. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `NetworkStatus_ListByLocation` | `SELECT` | `locationName, resourceGroupName, serviceName, subscriptionId` |
| `NetworkStatus_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` |
