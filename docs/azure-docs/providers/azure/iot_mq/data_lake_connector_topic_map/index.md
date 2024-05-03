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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_lake_connector_topic_map</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_mq.data_lake_connector_topic_map" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation properties |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | MQ DataLakeConnector TopicMap Resource properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataLakeConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName" /> | Get a DataLakeTopicMapResource |
| <CopyableCode code="list_by_data_lake_connector_resource" /> | `SELECT` | <CopyableCode code="dataLakeConnectorName, mqName, resourceGroupName, subscriptionId" /> | List DataLakeTopicMapResource resources by DataLakeConnectorResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataLakeConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName, data__extendedLocation" /> | Create a DataLakeTopicMapResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataLakeConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName" /> | Delete a DataLakeTopicMapResource |
| <CopyableCode code="_list_by_data_lake_connector_resource" /> | `EXEC` | <CopyableCode code="dataLakeConnectorName, mqName, resourceGroupName, subscriptionId" /> | List DataLakeTopicMapResource resources by DataLakeConnectorResource |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="dataLakeConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName" /> | Update a DataLakeTopicMapResource |
