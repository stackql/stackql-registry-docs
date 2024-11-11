---
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
  - fine_tuning
  - openai
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage openai resources using SQL
custom_edit_url: null
image: /img/providers/openai/stackql-openai-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.fine_tuning.events" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="created_at" /> | `integer` |  |
| <CopyableCode code="level" /> | `string` |  |
| <CopyableCode code="message" /> | `string` |  |
| <CopyableCode code="object" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_fine_tuning_events" /> | `SELECT` | <CopyableCode code="fine_tuning_job_id" /> |  |

## `SELECT` examples




```sql
SELECT
id,
created_at,
level,
message,
object
FROM openai.fine_tuning.events
WHERE fine_tuning_job_id = '{{ fine_tuning_job_id }}';
```