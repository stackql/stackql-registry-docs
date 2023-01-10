---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - tagmanager
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.tagmanager.workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Workspace display name. @mutable tagmanager.accounts.containers.workspaces.create @mutable tagmanager.accounts.containers.workspaces.update |
| `description` | `string` | Workspace description. @mutable tagmanager.accounts.containers.workspaces.create @mutable tagmanager.accounts.containers.workspaces.update |
| `workspaceId` | `string` | The Workspace ID uniquely identifies the GTM Workspace. |
| `accountId` | `string` | GTM Account ID. |
| `containerId` | `string` | GTM Container ID. |
| `fingerprint` | `string` | The fingerprint of the GTM Workspace as computed at storage time. This value is recomputed whenever the workspace is modified. |
| `path` | `string` | GTM Workspace's API relative path. |
| `tagManagerUrl` | `string` | Auto generated link to the tag manager UI |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_containers_workspaces_get` | `SELECT` | `accountsId, containersId, workspacesId` | Gets a Workspace. |
| `accounts_containers_workspaces_list` | `SELECT` | `accountsId, containersId` | Lists all Workspaces that belong to a GTM Container. |
| `accounts_containers_workspaces_create` | `INSERT` | `accountsId, containersId` | Creates a Workspace. |
| `accounts_containers_workspaces_delete` | `DELETE` | `accountsId, containersId, workspacesId` | Deletes a Workspace. |
| `accounts_containers_workspaces_quick_preview` | `EXEC` | `accountsId, containersId, workspacesId` | Quick previews a workspace by creating a fake container version from all entities in the provided workspace. |
| `accounts_containers_workspaces_resolve_conflict` | `EXEC` | `accountsId, containersId, workspacesId` | Resolves a merge conflict for a workspace entity by updating it to the resolved entity passed in the request. |
| `accounts_containers_workspaces_sync` | `EXEC` | `accountsId, containersId, workspacesId` | Syncs a workspace to the latest container version by updating all unmodified workspace entities and displaying conflicts for modified entities. |
| `accounts_containers_workspaces_update` | `EXEC` | `accountsId, containersId, workspacesId` | Updates a Workspace. |
