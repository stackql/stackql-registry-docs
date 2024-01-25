---
title: data_lake_connector
hide_title: false
hide_table_of_contents: false
keywords:
  - data_lake_connector
  - iot_mq
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
<tr><td><b>Name</b></td><td><code>data_lake_connector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_mq.data_lake_connector</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | ExtendedLocation properties |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | MQ DataLakeConnector  Resource properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dataLakeConnectorName, mqName, resourceGroupName, subscriptionId` | Get a DataLakeConnectorResource |
| `list_by_mq_resource` | `SELECT` | `mqName, resourceGroupName, subscriptionId` | List DataLakeConnectorResource resources by MqResource |
| `create_or_update` | `INSERT` | `dataLakeConnectorName, mqName, resourceGroupName, subscriptionId, data__extendedLocation` | Create a DataLakeConnectorResource |
| `delete` | `DELETE` | `dataLakeConnectorName, mqName, resourceGroupName, subscriptionId` | Delete a DataLakeConnectorResource |
| `_list_by_mq_resource` | `EXEC` | `mqName, resourceGroupName, subscriptionId` | List DataLakeConnectorResource resources by MqResource |
| `update` | `EXEC` | `dataLakeConnectorName, mqName, resourceGroupName, subscriptionId` | Update a DataLakeConnectorResource |
