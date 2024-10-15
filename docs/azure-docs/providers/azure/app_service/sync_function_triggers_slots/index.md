---
title: sync_function_triggers_slots
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_function_triggers_slots
  - app_service
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

Creates, updates, deletes, gets or lists a <code>sync_function_triggers_slots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sync_function_triggers_slots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.sync_function_triggers_slots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="key" /> | `string` | Secret key. |
| <CopyableCode code="trigger_url" /> | `string` | Trigger URL. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for This is to allow calling via powershell and ARM template. |

## `SELECT` examples

Description for This is to allow calling via powershell and ARM template.


```sql
SELECT
key,
trigger_url
FROM azure.app_service.sync_function_triggers_slots
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```