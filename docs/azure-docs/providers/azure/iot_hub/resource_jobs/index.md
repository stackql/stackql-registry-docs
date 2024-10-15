---
title: resource_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_jobs
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

Creates, updates, deletes, gets or lists a <code>resource_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.resource_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="endTimeUtc" /> | `string` | The time the job stopped processing. |
| <CopyableCode code="failureReason" /> | `string` | If status == failed, this string containing the reason for the failure. |
| <CopyableCode code="jobId" /> | `string` | The job identifier. |
| <CopyableCode code="parentJobId" /> | `string` | The job identifier of the parent job, if any. |
| <CopyableCode code="startTimeUtc" /> | `string` | The start time of the job. |
| <CopyableCode code="status" /> | `string` | The status of the job. |
| <CopyableCode code="statusMessage" /> | `string` | The status message for the job. |
| <CopyableCode code="type" /> | `string` | The type of the job. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobId, resourceGroupName, resourceName, subscriptionId" /> | Get the details of a job from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Get a list of all the jobs in an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry. |

## `SELECT` examples

Get a list of all the jobs in an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry.


```sql
SELECT
endTimeUtc,
failureReason,
jobId,
parentJobId,
startTimeUtc,
status,
statusMessage,
type
FROM azure.iot_hub.resource_jobs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```