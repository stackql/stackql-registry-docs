---
title: locations_operations_status
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_operations_status
  - subscriptions_admin
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

Creates, updates, deletes, gets or lists a <code>locations_operations_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locations_operations_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.subscriptions_admin.locations_operations_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `object` | The admin offer identifier for the location wide SubscriptionsAdminResourceTypes.OperationsStatus resource type. |
| <CopyableCode code="endTime" /> | `string` | The end time of the operation. |
| <CopyableCode code="error" /> | `object` | The extended error information. |
| <CopyableCode code="percentComplete" /> | `number` | The completion percentage of the operation. |
| <CopyableCode code="properties" /> | `object` | The internal operation properties. |
| <CopyableCode code="responseContent" /> | `object` | The content of the response. |
| <CopyableCode code="retryAfter" /> | `string` | The amount of time clients should wait.. |
| <CopyableCode code="startTime" /> | `string` | The start time of the operation. |
| <CopyableCode code="status" /> | `string` | The status of the operation. |
| <CopyableCode code="terminalHttpStatusCode" /> | `string` | The terminal http status code for the operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, operationsStatusName, subscriptionId" /> | Get the operation status. |

## `SELECT` examples

Get the operation status.


```sql
SELECT
id,
endTime,
error,
percentComplete,
properties,
responseContent,
retryAfter,
startTime,
status,
terminalHttpStatusCode
FROM azure_stack.subscriptions_admin.locations_operations_status
WHERE location = '{{ location }}'
AND operationsStatusName = '{{ operationsStatusName }}'
AND subscriptionId = '{{ subscriptionId }}';
```