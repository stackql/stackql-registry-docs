---
title: service_replica
hide_title: false
hide_table_of_contents: false
keywords:
  - service_replica
  - service_fabric_mesh
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
<tr><td><b>Name</b></td><td><code>service_replica</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_mesh.service_replica</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `osType` | `string` | The operation system required by the code in service. |
| `replicaName` | `string` | Name of the replica. |
| `codePackages` | `array` | Describes the set of code packages that forms the service. A code package describes the container and the properties for running it. All the code packages are started together on the same host and share the same context (network, process etc.). |
| `diagnostics` | `object` | Reference to sinks in DiagnosticsDescription. |
| `networkRefs` | `array` | The names of the private networks that this service needs to be part of. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServiceReplica_Get` | `SELECT` | `api-version, applicationResourceName, replicaName, resourceGroupName, serviceResourceName, subscriptionId` | Gets the information about the service replica with the given name. The information include the description and other properties of the service replica. |
| `ServiceReplica_List` | `SELECT` | `api-version, applicationResourceName, resourceGroupName, serviceResourceName, subscriptionId` | Gets the information about all replicas of a given service of an application. The information includes the runtime properties of the replica instance. |
