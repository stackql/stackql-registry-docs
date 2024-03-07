---
title: ports_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - ports_connections
  - service_map
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
<tr><td><b>Name</b></td><td><code>ports_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_map.ports_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Additional resource type qualifier. |
| `properties` | `object` | Properties for a connection resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `machineName, portName, resourceGroupName, subscriptionId, workspaceName` |
| `_list` | `EXEC` | `machineName, portName, resourceGroupName, subscriptionId, workspaceName` |