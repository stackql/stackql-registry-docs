---
title: workflow_triggers_schema_json
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_triggers_schema_json
  - logic_apps
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
<tr><td><b>Name</b></td><td><code>workflow_triggers_schema_json</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.workflow_triggers_schema_json" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="content" /> | `string` | The JSON content. |
| <CopyableCode code="title" /> | `string` | The JSON title. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, triggerName, workflowName" /> |
