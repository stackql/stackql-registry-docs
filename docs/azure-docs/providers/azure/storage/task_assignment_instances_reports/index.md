---
title: task_assignment_instances_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - task_assignment_instances_reports
  - storage
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

Creates, updates, deletes, gets or lists a <code>task_assignment_instances_reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_assignment_instances_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.task_assignment_instances_reports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Storage task execution report for a run instance. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, storageTaskAssignmentName, subscriptionId" /> | Fetch the report summary of a single storage task assignment's instances |

## `SELECT` examples

Fetch the report summary of a single storage task assignment's instances


```sql
SELECT
properties
FROM azure.storage.task_assignment_instances_reports
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageTaskAssignmentName = '{{ storageTaskAssignmentName }}'
AND subscriptionId = '{{ subscriptionId }}';
```