---
title: upgrade_notifications
hide_title: false
hide_table_of_contents: false
keywords:
  - upgrade_notifications
  - redis
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

Creates, updates, deletes, gets or lists a <code>upgrade_notifications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>upgrade_notifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redis.upgrade_notifications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of upgrade notification. |
| <CopyableCode code="timestamp" /> | `string` | Timestamp when upgrade notification occurred. |
| <CopyableCode code="upsellNotification" /> | `object` | Details about this upgrade notification |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="history, name, resourceGroupName, subscriptionId" /> | Gets any upgrade notifications for a Redis cache. |

## `SELECT` examples

Gets any upgrade notifications for a Redis cache.


```sql
SELECT
name,
timestamp,
upsellNotification
FROM azure_isv.redis.upgrade_notifications
WHERE history = '{{ history }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```