---
title: triggers_event_subscription_status
hide_title: false
hide_table_of_contents: false
keywords:
  - triggers_event_subscription_status
  - data_factory
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

Creates, updates, deletes, gets or lists a <code>triggers_event_subscription_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>triggers_event_subscription_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.triggers_event_subscription_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="status" /> | `string` | Event Subscription Status. |
| <CopyableCode code="triggerName" /> | `string` | Trigger name. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId, triggerName" /> | Get a trigger's event subscription status. |

## `SELECT` examples

Get a trigger's event subscription status.


```sql
SELECT
status,
triggerName
FROM azure.data_factory.triggers_event_subscription_status
WHERE factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND triggerName = '{{ triggerName }}';
```