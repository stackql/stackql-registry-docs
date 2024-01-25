---
title: service_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - service_configurations
  - hybrid_connectivity
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
<tr><td><b>Name</b></td><td><code>service_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_connectivity.service_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Service configuration details |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `endpointName, resourceUri, serviceConfigurationName` | Gets the details about the service to the resource. |
| `list_by_endpoint_resource` | `SELECT` | `endpointName, resourceUri` | API to enumerate registered services in service configurations under a Endpoint Resource |
| `delete` | `DELETE` | `endpointName, resourceUri, serviceConfigurationName` | Deletes the service details to the target resource. |
| `_list_by_endpoint_resource` | `EXEC` | `endpointName, resourceUri` | API to enumerate registered services in service configurations under a Endpoint Resource |
| `update` | `EXEC` | `endpointName, resourceUri, serviceConfigurationName` | Update the service details in the service configurations of the target resource. |
