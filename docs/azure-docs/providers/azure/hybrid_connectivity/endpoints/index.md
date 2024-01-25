---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
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
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_connectivity.endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Endpoint details |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `endpointName, resourceUri` | Gets the endpoint to the resource. |
| `list` | `SELECT` | `resourceUri` | List of endpoints to the target resource. |
| `create_or_update` | `INSERT` | `endpointName, resourceUri` | Create or update the endpoint to the target resource. |
| `delete` | `DELETE` | `endpointName, resourceUri` | Deletes the endpoint access to the target resource. |
| `_list` | `EXEC` | `resourceUri` | List of endpoints to the target resource. |
| `update` | `EXEC` | `endpointName, resourceUri` | Update the endpoint to the target resource. |
