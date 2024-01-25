---
title: data_lake_connector_topic_map
hide_title: false
hide_table_of_contents: false
keywords:
  - data_lake_connector_topic_map
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
<tr><td><b>Name</b></td><td><code>data_lake_connector_topic_map</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_mq.data_lake_connector_topic_map</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | ExtendedLocation properties |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | MQ DataLakeConnector TopicMap Resource properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dataLakeConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName` | Get a DataLakeTopicMapResource |
| `list_by_data_lake_connector_resource` | `SELECT` | `dataLakeConnectorName, mqName, resourceGroupName, subscriptionId` | List DataLakeTopicMapResource resources by DataLakeConnectorResource |
| `create_or_update` | `INSERT` | `dataLakeConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName, data__extendedLocation` | Create a DataLakeTopicMapResource |
| `delete` | `DELETE` | `dataLakeConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName` | Delete a DataLakeTopicMapResource |
| `_list_by_data_lake_connector_resource` | `EXEC` | `dataLakeConnectorName, mqName, resourceGroupName, subscriptionId` | List DataLakeTopicMapResource resources by DataLakeConnectorResource |
| `update` | `EXEC` | `dataLakeConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName` | Update a DataLakeTopicMapResource |
