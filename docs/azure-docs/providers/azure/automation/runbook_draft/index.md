---
title: runbook_draft
hide_title: false
hide_table_of_contents: false
keywords:
  - runbook_draft
  - automation
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>runbook_draft</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.runbook_draft" /></td></tr>
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
| <CopyableCode code="replace_content" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Replaces the runbook draft content. |
| <CopyableCode code="undo_edit" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Undo draft edit to last known published state identified by runbook name. |
