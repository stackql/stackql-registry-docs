---
title: runbook_drafts
hide_title: false
hide_table_of_contents: false
keywords:
  - runbook_drafts
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

Creates, updates, deletes, gets or lists a <code>runbook_drafts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>runbook_drafts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.runbook_drafts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creationTime" /> | `string` | Gets or sets the creation time of the runbook draft. |
| <CopyableCode code="draftContentLink" /> | `object` | Definition of the content link. |
| <CopyableCode code="inEdit" /> | `boolean` | Gets or sets whether runbook is in edit mode. |
| <CopyableCode code="lastModifiedTime" /> | `string` | Gets or sets the last modified time of the runbook draft. |
| <CopyableCode code="outputTypes" /> | `array` | Gets or sets the runbook output types. |
| <CopyableCode code="parameters" /> | `object` | Gets or sets the runbook draft parameters. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Retrieve the runbook draft identified by runbook name. |
| <CopyableCode code="undo_edit" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Undo draft edit to last known published state identified by runbook name. |

## `SELECT` examples

Retrieve the runbook draft identified by runbook name.


```sql
SELECT
creationTime,
draftContentLink,
inEdit,
lastModifiedTime,
outputTypes,
parameters
FROM azure.automation.runbook_drafts
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND runbookName = '{{ runbookName }}'
AND subscriptionId = '{{ subscriptionId }}';
```