---
title: runbook_draft_contents
hide_title: false
hide_table_of_contents: false
keywords:
  - runbook_draft_contents
  - automation
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

Creates, updates, deletes, gets or lists a <code>runbook_draft_contents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>runbook_draft_contents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.runbook_draft_contents" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Retrieve the content of runbook draft identified by runbook name. |
| <CopyableCode code="replace" /> | `REPLACE` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Replaces the runbook draft content. |

## `SELECT` examples

Retrieve the content of runbook draft identified by runbook name.


```sql
SELECT

FROM azure.automation.runbook_draft_contents
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND runbookName = '{{ runbookName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `REPLACE` example

Replaces all fields in the specified <code>runbook_draft_contents</code> resource.

```sql
/*+ update */
REPLACE azure.automation.runbook_draft_contents
SET 

WHERE 
automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND runbookName = '{{ runbookName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
