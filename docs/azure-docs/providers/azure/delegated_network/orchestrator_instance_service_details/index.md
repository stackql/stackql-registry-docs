---
title: orchestrator_instance_service_details
hide_title: false
hide_table_of_contents: false
keywords:
  - orchestrator_instance_service_details
  - delegated_network
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
<tr><td><b>Name</b></td><td><code>orchestrator_instance_service_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.delegated_network.orchestrator_instance_service_details</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | An identifier that represents the resource. |
| `name` | `string` | The name of the resource. |
| `identity` | `object` |  |
| `kind` | `string` | The kind of workbook. Choices are user and shared. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties of orchestrator |
| `tags` | `object` | The resource tags. |
| `type` | `string` | The type of resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` |
