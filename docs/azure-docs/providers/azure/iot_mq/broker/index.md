---
title: broker
hide_title: false
hide_table_of_contents: false
keywords:
  - broker
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
<tr><td><b>Name</b></td><td><code>broker</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_mq.broker" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation properties |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Broker Resource properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="brokerName, mqName, resourceGroupName, subscriptionId" /> | Get a BrokerResource |
| <CopyableCode code="list_by_mq_resource" /> | `SELECT` | <CopyableCode code="mqName, resourceGroupName, subscriptionId" /> | List BrokerResource resources by MqResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="brokerName, mqName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a BrokerResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="brokerName, mqName, resourceGroupName, subscriptionId" /> | Delete a BrokerResource |
| <CopyableCode code="_list_by_mq_resource" /> | `EXEC` | <CopyableCode code="mqName, resourceGroupName, subscriptionId" /> | List BrokerResource resources by MqResource |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="brokerName, mqName, resourceGroupName, subscriptionId" /> | Update a BrokerResource |
