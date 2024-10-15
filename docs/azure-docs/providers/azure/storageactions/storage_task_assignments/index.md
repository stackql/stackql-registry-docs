---
title: storage_task_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_task_assignments
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

Creates, updates, deletes, gets or lists a <code>storage_task_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_task_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storageactions.storage_task_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID of the Storage Task Assignment. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageTaskName, subscriptionId" /> | Lists Resource IDs of the Storage Task Assignments associated with this Storage Task. |

## `SELECT` examples

Lists Resource IDs of the Storage Task Assignments associated with this Storage Task.


```sql
SELECT
id
FROM azure.storageactions.storage_task_assignments
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageTaskName = '{{ storageTaskName }}'
AND subscriptionId = '{{ subscriptionId }}';
```