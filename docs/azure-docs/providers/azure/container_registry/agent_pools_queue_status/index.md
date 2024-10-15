---
title: agent_pools_queue_status
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools_queue_status
  - container_registry
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

Creates, updates, deletes, gets or lists a <code>agent_pools_queue_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent_pools_queue_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.agent_pools_queue_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="count" /> | `integer` | The number of pending runs in the queue |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="agentPoolName, registryName, resourceGroupName, subscriptionId" /> | Gets the count of queued runs for a given agent pool. |

## `SELECT` examples

Gets the count of queued runs for a given agent pool.


```sql
SELECT
count
FROM azure.container_registry.agent_pools_queue_status
WHERE agentPoolName = '{{ agentPoolName }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```