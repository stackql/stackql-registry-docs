---
title: storage_tasks_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_tasks_reports
  - storageactions
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

Creates, updates, deletes, gets or lists a <code>storage_tasks_reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_tasks_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storageactions.storage_tasks_reports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Storage task execution report for a run instance. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageTaskName, subscriptionId" /> | Fetch the storage tasks run report summary for each assignment. |

## `SELECT` examples

Fetch the storage tasks run report summary for each assignment.


```sql
SELECT
properties
FROM azure.storageactions.storage_tasks_reports
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageTaskName = '{{ storageTaskName }}'
AND subscriptionId = '{{ subscriptionId }}';
```