---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - desktop_virtualization
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
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.desktop_virtualization.workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.  |
| `identity` | `object` | Identity for the resource. |
| `kind` | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| `managedBy` | `string` | The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource. |
| `plan` | `object` | Plan for the resource. |
| `properties` | `object` | Schema for Workspace properties. |
| `sku` | `object` | The resource model definition representing SKU |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Get a workspace. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List workspaces. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List workspaces in subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, workspaceName` | Create or update a workspace. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, workspaceName` | Remove a workspace. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List workspaces. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List workspaces in subscription. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Update a workspace. |
