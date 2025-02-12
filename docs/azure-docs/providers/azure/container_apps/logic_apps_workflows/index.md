---
title: logic_apps_workflows
hide_title: false
hide_table_of_contents: false
keywords:
  - logic_apps_workflows
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

Creates, updates, deletes, gets or lists a <code>logic_apps_workflows</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logic_apps_workflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.logic_apps_workflows" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="kind" /> | `string` | The resource kind. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | Additional workflow properties. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="containerAppName, logicAppName, resourceGroupName, subscriptionId, workflowName" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="containerAppName, logicAppName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
id,
name,
kind,
location,
properties,
type
FROM azure.container_apps.logic_apps_workflows
WHERE containerAppName = '{{ containerAppName }}'
AND logicAppName = '{{ logicAppName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```