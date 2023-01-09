---
title: folders
hide_title: false
hide_table_of_contents: false
keywords:
  - folders
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
<tr><td><b>Name</b></td><td><code>folders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.tagmanager.folders</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Folder display name. @mutable tagmanager.accounts.containers.workspaces.folders.create @mutable tagmanager.accounts.containers.workspaces.folders.update |
| `path` | `string` | GTM Folder's API relative path. |
| `tagManagerUrl` | `string` | Auto generated link to the tag manager UI |
| `containerId` | `string` | GTM Container ID. |
| `fingerprint` | `string` | The fingerprint of the GTM Folder as computed at storage time. This value is recomputed whenever the folder is modified. |
| `workspaceId` | `string` | GTM Workspace ID. |
| `accountId` | `string` | GTM Account ID. |
| `folderId` | `string` | The Folder ID uniquely identifies the GTM Folder. |
| `notes` | `string` | User notes on how to apply this folder in the container. @mutable tagmanager.accounts.containers.workspaces.folders.create @mutable tagmanager.accounts.containers.workspaces.folders.update |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_containers_workspaces_folders_get` | `SELECT` | `accountsId, containersId, foldersId, workspacesId` | Gets a GTM Folder. |
| `accounts_containers_workspaces_folders_list` | `SELECT` | `accountsId, containersId, workspacesId` | Lists all GTM Folders of a Container. |
| `accounts_containers_workspaces_folders_create` | `INSERT` | `accountsId, containersId, workspacesId` | Creates a GTM Folder. |
| `accounts_containers_workspaces_folders_delete` | `DELETE` | `accountsId, containersId, foldersId, workspacesId` | Deletes a GTM Folder. |
| `accounts_containers_workspaces_folders_entities` | `EXEC` | `accountsId, containersId, foldersId, workspacesId` | List all entities in a GTM Folder. |
| `accounts_containers_workspaces_folders_move_entities_to_folder` | `EXEC` | `accountsId, containersId, foldersId, workspacesId` | Moves entities to a GTM Folder. |
| `accounts_containers_workspaces_folders_revert` | `EXEC` | `accountsId, containersId, foldersId, workspacesId` | Reverts changes to a GTM Folder in a GTM Workspace. |
| `accounts_containers_workspaces_folders_update` | `EXEC` | `accountsId, containersId, foldersId, workspacesId` | Updates a GTM Folder. |
