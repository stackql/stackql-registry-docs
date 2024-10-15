---
title: jobs_job_histories
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs_job_histories
  - scheduler
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

Creates, updates, deletes, gets or lists a <code>jobs_job_histories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs_job_histories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.scheduler.jobs_job_histories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets the job history identifier. |
| <CopyableCode code="name" /> | `string` | Gets the job history name. |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | Gets the job history resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="jobCollectionName, jobName, resourceGroupName, subscriptionId" /> | Lists job history. |

## `SELECT` examples

Lists job history.


```sql
SELECT
id,
name,
properties,
type
FROM azure.scheduler.jobs_job_histories
WHERE jobCollectionName = '{{ jobCollectionName }}'
AND jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```