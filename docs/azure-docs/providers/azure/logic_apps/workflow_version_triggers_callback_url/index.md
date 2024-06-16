---
title: workflow_version_triggers_callback_url
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_version_triggers_callback_url
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
<tr><td><b>Name</b></td><td><code>workflow_version_triggers_callback_url</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.workflow_version_triggers_callback_url" /></td></tr>
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
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, triggerName, versionId, workflowName" /> |
