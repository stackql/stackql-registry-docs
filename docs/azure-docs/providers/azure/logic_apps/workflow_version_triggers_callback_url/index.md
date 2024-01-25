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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_version_triggers_callback_url</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.workflow_version_triggers_callback_url</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `basePath` | `string` | Gets the workflow trigger callback URL base path. |
| `method` | `string` | Gets the workflow trigger callback URL HTTP method. |
| `queries` | `object` | Gets the workflow trigger callback URL query parameters. |
| `relativePath` | `string` | Gets the workflow trigger callback URL relative path. |
| `relativePathParameters` | `array` | Gets the workflow trigger callback URL relative path parameters. |
| `value` | `string` | Gets the workflow trigger callback URL. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `api-version, resourceGroupName, subscriptionId, triggerName, versionId, workflowName` |
