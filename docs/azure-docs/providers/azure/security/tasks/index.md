---
title: tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks
  - security
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

Creates, updates, deletes, gets or lists a <code>tasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.tasks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Describes properties of a task. |
| <CopyableCode code="type" /> | `string` | Resource type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Recommended tasks that will help improve the security of the subscription proactively |
| <CopyableCode code="list_by_home_region" /> | `SELECT` | <CopyableCode code="ascLocation, subscriptionId" /> | Recommended tasks that will help improve the security of the subscription proactively |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="ascLocation, resourceGroupName, subscriptionId" /> | Recommended tasks that will help improve the security of the subscription proactively |

## `SELECT` examples

Recommended tasks that will help improve the security of the subscription proactively


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.tasks
WHERE subscriptionId = '{{ subscriptionId }}';
```