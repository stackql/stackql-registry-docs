---
title: workspace_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_private_link_resources
  - healthcare_apis
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>workspace_private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.healthcare_apis.workspace_private_link_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of a private link resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkspacePrivateLinkResources_Get` | `SELECT` | `api-version, groupName, resourceGroupName, subscriptionId, workspaceName` | Gets a private link resource that need to be created for a workspace. |
| `WorkspacePrivateLinkResources_ListByWorkspace` | `SELECT` | `api-version, resourceGroupName, subscriptionId, workspaceName` | Gets the private link resources that need to be created for a workspace. |
