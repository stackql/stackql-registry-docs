---
title: continuous_web_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - continuous_web_jobs
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

Creates, updates, deletes, gets or lists a <code>continuous_web_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>continuous_web_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.continuous_web_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | ContinuousWebJob resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId, webJobName" /> | Description for Gets a continuous web job by its ID for an app, or a deployment slot. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for List continuous web jobs for an app, or a deployment slot. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId, webJobName" /> | Description for Delete a continuous web job by its ID for an app, or a deployment slot. |

## `SELECT` examples

Description for List continuous web jobs for an app, or a deployment slot.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.continuous_web_jobs
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `DELETE` example

Deletes the specified <code>continuous_web_jobs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.continuous_web_jobs
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND webJobName = '{{ webJobName }}';
```
