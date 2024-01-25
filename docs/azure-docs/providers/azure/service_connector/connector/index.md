---
title: connector
hide_title: false
hide_table_of_contents: false
keywords:
  - connector
  - service_connector
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
<tr><td><b>Name</b></td><td><code>connector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_connector.connector</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The properties of the Linker. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `connectorName, location, resourceGroupName, subscriptionId` | Returns Connector resource for a given name. |
| `list` | `SELECT` | `location, resourceGroupName, subscriptionId` | Returns list of connector which connects to the resource, which supports to config the target service during the resource provision. |
| `create_or_update` | `INSERT` | `connectorName, location, resourceGroupName, subscriptionId, data__properties` | Create or update Connector resource. |
| `delete` | `DELETE` | `connectorName, location, resourceGroupName, subscriptionId` | Delete a Connector. |
| `_list` | `EXEC` | `location, resourceGroupName, subscriptionId` | Returns list of connector which connects to the resource, which supports to config the target service during the resource provision. |
| `generate_configurations` | `EXEC` | `connectorName, location, resourceGroupName, subscriptionId` | Generate configurations for a Connector. |
| `update` | `EXEC` | `connectorName, location, resourceGroupName, subscriptionId` | Operation to update an existing Connector. |
| `validate` | `EXEC` | `connectorName, location, resourceGroupName, subscriptionId` | Validate a Connector. |
