---
title: content_template
hide_title: false
hide_table_of_contents: false
keywords:
  - content_template
  - sentinel
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
<tr><td><b>Name</b></td><td><code>content_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sentinel.content_template</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `properties` | `object` | Template property bag. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, templateId, workspaceName` | Gets a template byt its identifier.<br />Expandable properties:<br />- properties/mainTemplate<br />- properties/dependantTemplates |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, templateId, workspaceName` | Delete an installed template. |
| `install` | `EXEC` | `resourceGroupName, subscriptionId, templateId, workspaceName` | Install a template. |
