---
title: webhooks_events
hide_title: false
hide_table_of_contents: false
keywords:
  - webhooks_events
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

Creates, updates, deletes, gets or lists a <code>webhooks_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webhooks_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.webhooks_events" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The event ID. |
| <CopyableCode code="eventRequestMessage" /> | `object` | The event request message sent to the service URI. |
| <CopyableCode code="eventResponseMessage" /> | `object` | The event response message received from the service URI. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, webhookName" /> | Lists recent events for the specified webhook. |

## `SELECT` examples

Lists recent events for the specified webhook.


```sql
SELECT
id,
eventRequestMessage,
eventResponseMessage
FROM azure.container_registry.webhooks_events
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND webhookName = '{{ webhookName }}';
```