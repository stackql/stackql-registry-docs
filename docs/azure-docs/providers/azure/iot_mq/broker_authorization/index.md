---
title: broker_authorization
hide_title: false
hide_table_of_contents: false
keywords:
  - broker_authorization
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
<tr><td><b>Name</b></td><td><code>broker_authorization</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_mq.broker_authorization" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authorizationName, brokerName, mqName, resourceGroupName, subscriptionId" /> | Get a BrokerAuthorizationResource |
| <CopyableCode code="list_by_broker_resource" /> | `SELECT` | <CopyableCode code="brokerName, mqName, resourceGroupName, subscriptionId" /> | List BrokerAuthorizationResource resources by BrokerResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authorizationName, brokerName, mqName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a BrokerAuthorizationResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authorizationName, brokerName, mqName, resourceGroupName, subscriptionId" /> | Delete a BrokerAuthorizationResource |
| <CopyableCode code="_list_by_broker_resource" /> | `EXEC` | <CopyableCode code="brokerName, mqName, resourceGroupName, subscriptionId" /> | List BrokerAuthorizationResource resources by BrokerResource |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="authorizationName, brokerName, mqName, resourceGroupName, subscriptionId" /> | Update a BrokerAuthorizationResource |
