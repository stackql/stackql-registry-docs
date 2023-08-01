---
title: source_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - source_controls
  - security_insights
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
<tr><td><b>Name</b></td><td><code>source_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.source_controls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Describes source control properties |
| `etag` | `string` | Etag of the azure resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SourceControls_Get` | `SELECT` | `resourceGroupName, sourceControlId, subscriptionId, workspaceName` | Gets a source control byt its identifier. |
| `SourceControls_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all source controls, without source control items. |
| `SourceControls_Create` | `INSERT` | `resourceGroupName, sourceControlId, subscriptionId, workspaceName` | Creates a source control. |
| `SourceControls_Delete` | `DELETE` | `resourceGroupName, sourceControlId, subscriptionId, workspaceName` | Delete a source control. |
