---
title: workflow_triggers_callback_urls
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_triggers_callback_urls
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

Creates, updates, deletes, gets or lists a <code>workflow_triggers_callback_urls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_triggers_callback_urls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.workflow_triggers_callback_urls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="basePath" /> | `string` | Gets the workflow trigger callback URL base path. |
| <CopyableCode code="method" /> | `string` | Gets the workflow trigger callback URL HTTP method. |
| <CopyableCode code="queries" /> | `object` | Gets the workflow trigger callback URL query parameters. |
| <CopyableCode code="relativePath" /> | `string` | Gets the workflow trigger callback URL relative path. |
| <CopyableCode code="relativePathParameters" /> | `array` | Gets the workflow trigger callback URL relative path parameters. |
| <CopyableCode code="value" /> | `string` | Gets the workflow trigger callback URL. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId, triggerName, workflowName" /> | Get the callback URL for a workflow trigger. |

## `SELECT` examples

Get the callback URL for a workflow trigger.


```sql
SELECT
basePath,
method,
queries,
relativePath,
relativePathParameters,
value
FROM azure.app_service.workflow_triggers_callback_urls
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND triggerName = '{{ triggerName }}'
AND workflowName = '{{ workflowName }}';
```