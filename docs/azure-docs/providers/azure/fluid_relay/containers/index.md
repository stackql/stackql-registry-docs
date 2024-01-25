---
title: containers
hide_title: false
hide_table_of_contents: false
keywords:
  - containers
  - fluid_relay
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
<tr><td><b>Name</b></td><td><code>containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.fluid_relay.containers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The properties of a Fluid Relay Container resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `fluidRelayContainerName, fluidRelayServerName, resourceGroup, subscriptionId` |
| `list_by_fluid_relay_servers` | `SELECT` | `fluidRelayServerName, resourceGroup, subscriptionId` |
| `delete` | `DELETE` | `fluidRelayContainerName, fluidRelayServerName, resourceGroup, subscriptionId` |
| `_list_by_fluid_relay_servers` | `EXEC` | `fluidRelayServerName, resourceGroup, subscriptionId` |
