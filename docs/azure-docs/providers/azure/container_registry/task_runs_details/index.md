---
title: task_runs_details
hide_title: false
hide_table_of_contents: false
keywords:
  - task_runs_details
  - container_registry
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

Creates, updates, deletes, gets or lists a <code>task_runs_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_runs_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.task_runs_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed identity for the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource |
| <CopyableCode code="properties" /> | `object` | The properties of task run. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, taskRunName" /> | Gets the detailed information for a given task run that includes all secrets. |

## `SELECT` examples

Gets the detailed information for a given task run that includes all secrets.


```sql
SELECT
identity,
location,
properties
FROM azure.container_registry.task_runs_details
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND taskRunName = '{{ taskRunName }}';
```