---
title: kafka_connector
hide_title: false
hide_table_of_contents: false
keywords:
  - kafka_connector
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
<tr><td><b>Name</b></td><td><code>kafka_connector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_mq.kafka_connector" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation properties |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | KafkaConnector Properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="kafkaConnectorName, mqName, resourceGroupName, subscriptionId" /> | Get a KafkaConnectorResource |
| <CopyableCode code="list_by_mq_resource" /> | `SELECT` | <CopyableCode code="mqName, resourceGroupName, subscriptionId" /> | List KafkaConnectorResource resources by MqResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="kafkaConnectorName, mqName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a KafkaConnectorResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="kafkaConnectorName, mqName, resourceGroupName, subscriptionId" /> | Delete a KafkaConnectorResource |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="kafkaConnectorName, mqName, resourceGroupName, subscriptionId" /> | Update a KafkaConnectorResource |
