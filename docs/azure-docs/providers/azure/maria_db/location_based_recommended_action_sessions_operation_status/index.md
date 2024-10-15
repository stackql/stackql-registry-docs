---
title: location_based_recommended_action_sessions_operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - location_based_recommended_action_sessions_operation_status
  - maria_db
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

Creates, updates, deletes, gets or lists a <code>location_based_recommended_action_sessions_operation_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_based_recommended_action_sessions_operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maria_db.location_based_recommended_action_sessions_operation_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Operation identifier. |
| <CopyableCode code="startTime" /> | `string` | Operation start time. |
| <CopyableCode code="status" /> | `string` | Operation status. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationName, operationId, subscriptionId" /> | Recommendation action session operation status. |

## `SELECT` examples

Recommendation action session operation status.


```sql
SELECT
name,
startTime,
status
FROM azure.maria_db.location_based_recommended_action_sessions_operation_status
WHERE locationName = '{{ locationName }}'
AND operationId = '{{ operationId }}'
AND subscriptionId = '{{ subscriptionId }}';
```