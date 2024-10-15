---
title: resource_endpoint_health
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_endpoint_health
  - iot_hub
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>resource_endpoint_health</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_endpoint_health</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.resource_endpoint_health" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="endpointId" /> | `string` | Id of the endpoint |
| <CopyableCode code="healthStatus" /> | `string` | Health statuses have following meanings. The 'healthy' status shows that the endpoint is accepting messages as expected. The 'unhealthy' status shows that the endpoint is not accepting messages as expected and IoT Hub is retrying to send data to this endpoint. The status of an unhealthy endpoint will be updated to healthy when IoT Hub has established an eventually consistent state of health. The 'dead' status shows that the endpoint is not accepting messages, after IoT Hub retried sending messages for the retrial period. See IoT Hub metrics to identify errors and monitor issues with endpoints. The 'unknown' status shows that the IoT Hub has not established a connection with the endpoint. No messages have been delivered to or rejected from this endpoint |
| <CopyableCode code="lastKnownError" /> | `string` | Last error obtained when a message failed to be delivered to iot hub |
| <CopyableCode code="lastKnownErrorTime" /> | `string` | Time at which the last known error occurred |
| <CopyableCode code="lastSendAttemptTime" /> | `string` | Last time iot hub tried to send a message to the endpoint |
| <CopyableCode code="lastSuccessfulSendAttemptTime" /> | `string` | Last time iot hub successfully sent a message to the endpoint |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="iotHubName, resourceGroupName, subscriptionId" /> | Get the health for routing endpoints. |

## `SELECT` examples

Get the health for routing endpoints.


```sql
SELECT
endpointId,
healthStatus,
lastKnownError,
lastKnownErrorTime,
lastSendAttemptTime,
lastSuccessfulSendAttemptTime
FROM azure.iot_hub.resource_endpoint_health
WHERE iotHubName = '{{ iotHubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```