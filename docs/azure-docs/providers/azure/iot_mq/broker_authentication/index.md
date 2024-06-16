---
title: broker_authentication
hide_title: false
hide_table_of_contents: false
keywords:
  - broker_authentication
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
<tr><td><b>Name</b></td><td><code>broker_authentication</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_mq.broker_authentication" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authenticationName, brokerName, mqName, resourceGroupName, subscriptionId" /> | Get a BrokerAuthenticationResource |
| <CopyableCode code="list_by_broker_resource" /> | `SELECT` | <CopyableCode code="brokerName, mqName, resourceGroupName, subscriptionId" /> | List BrokerAuthenticationResource resources by BrokerResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authenticationName, brokerName, mqName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a BrokerAuthenticationResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authenticationName, brokerName, mqName, resourceGroupName, subscriptionId" /> | Delete a BrokerAuthenticationResource |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="authenticationName, brokerName, mqName, resourceGroupName, subscriptionId" /> | Update a BrokerAuthenticationResource |
