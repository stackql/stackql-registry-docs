
---
title: executions_execution_history
hide_title: false
hide_table_of_contents: false
keywords:
  - executions_execution_history
  - workflowexecutions
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

Creates, updates, deletes or gets an <code>executions_execution_history</code> resource or lists <code>executions_execution_history</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>executions_execution_history</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.workflowexecutions.executions_execution_history" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete_execution_history" /> | `DELETE` | <CopyableCode code="executionsId, locationsId, projectsId, workflowsId" /> | Deletes all step entries for an execution. |

## `DELETE` example

Deletes the specified executions_execution_history resource.

```sql
DELETE FROM google.workflowexecutions.executions_execution_history
WHERE executionsId = '{{ executionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND workflowsId = '{{ workflowsId }}';
```
