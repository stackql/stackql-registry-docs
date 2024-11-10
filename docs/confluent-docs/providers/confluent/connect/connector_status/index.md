---
title: connector_status
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_status
  - connect
  - confluent
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage confluent resources using SQL
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>connector_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.connect.connector_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the connector. |
| <CopyableCode code="connector" /> | `object` | The map containing connector status. |
| <CopyableCode code="tasks" /> | `array` | The map containing the task status. |
| <CopyableCode code="type" /> | `string` | Type of connector, sink or source. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="read_connectv1connector_status" /> | `SELECT` | <CopyableCode code="connector_name, environment_id, kafka_cluster_id" /> | Get current status of the connector. This includes whether it is running, failed, or paused. Also includes which worker it is assigned to, error information if it has failed, and the state of all its tasks. |

## `SELECT` examples

Get current status of the connector. This includes whether it is running, failed, or paused. Also includes which worker it is assigned to, error information if it has failed, and the state of all its tasks.


```sql
SELECT
name,
connector,
tasks,
type
FROM confluent.connect.connector_status
WHERE connector_name = '{{ connector_name }}'
AND environment_id = '{{ environment_id }}'
AND kafka_cluster_id = '{{ kafka_cluster_id }}';
```