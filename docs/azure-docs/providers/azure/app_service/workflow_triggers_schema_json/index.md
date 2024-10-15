---
title: workflow_triggers_schema_json
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_triggers_schema_json
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

Creates, updates, deletes, gets or lists a <code>workflow_triggers_schema_json</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_triggers_schema_json</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.workflow_triggers_schema_json" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="content" /> | `string` | The JSON content. |
| <CopyableCode code="title" /> | `string` | The JSON title. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId, triggerName, workflowName" /> | Get the trigger schema as JSON. |

## `SELECT` examples

Get the trigger schema as JSON.


```sql
SELECT
content,
title
FROM azure.app_service.workflow_triggers_schema_json
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND triggerName = '{{ triggerName }}'
AND workflowName = '{{ workflowName }}';
```