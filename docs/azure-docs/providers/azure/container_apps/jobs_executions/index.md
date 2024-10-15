---
title: jobs_executions
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs_executions
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>jobs_executions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs_executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.jobs_executions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Job execution Id. |
| <CopyableCode code="name" /> | `string` | Job execution Name. |
| <CopyableCode code="properties" /> | `object` | Container Apps Job execution specific properties. |
| <CopyableCode code="type" /> | `string` | Job execution type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
id,
name,
properties,
type
FROM azure.container_apps.jobs_executions
WHERE jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```