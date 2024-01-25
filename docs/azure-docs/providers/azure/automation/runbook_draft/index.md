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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>runbook_draft</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.runbook_draft</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `creationTime` | `string` | Gets or sets the creation time of the runbook draft. |
| `draftContentLink` | `object` | Definition of the content link. |
| `inEdit` | `boolean` | Gets or sets whether runbook is in edit mode. |
| `lastModifiedTime` | `string` | Gets or sets the last modified time of the runbook draft. |
| `outputTypes` | `array` | Gets or sets the runbook output types. |
| `parameters` | `object` | Gets or sets the runbook draft parameters. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `automationAccountName, resourceGroupName, runbookName, subscriptionId` | Retrieve the runbook draft identified by runbook name. |
| `replace_content` | `EXEC` | `automationAccountName, resourceGroupName, runbookName, subscriptionId` | Replaces the runbook draft content. |
| `undo_edit` | `EXEC` | `automationAccountName, resourceGroupName, runbookName, subscriptionId` | Undo draft edit to last known published state identified by runbook name. |
