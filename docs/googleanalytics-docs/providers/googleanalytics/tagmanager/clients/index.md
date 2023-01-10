---
title: clients
hide_title: false
hide_table_of_contents: false
keywords:
  - clients
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
<tr><td><b>Name</b></td><td><code>clients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.tagmanager.clients</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Client display name. @mutable tagmanager.accounts.containers.workspaces.clients.create @mutable tagmanager.accounts.containers.workspaces.clients.update |
| `priority` | `integer` | Priority determines relative firing order. @mutable tagmanager.accounts.containers.workspaces.clients.create @mutable tagmanager.accounts.containers.workspaces.clients.update |
| `path` | `string` | GTM client's API relative path. |
| `workspaceId` | `string` | GTM Workspace ID. |
| `parameter` | `array` | The client's parameters. @mutable tagmanager.accounts.containers.workspaces.clients.create @mutable tagmanager.accounts.containers.workspaces.clients.update |
| `fingerprint` | `string` | The fingerprint of the GTM Client as computed at storage time. This value is recomputed whenever the client is modified. |
| `parentFolderId` | `string` | Parent folder id. |
| `notes` | `string` | User notes on how to apply this tag in the container. @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update |
| `accountId` | `string` | GTM Account ID. |
| `clientId` | `string` | The Client ID uniquely identifies the GTM client. |
| `tagManagerUrl` | `string` | Auto generated link to the tag manager UI |
| `containerId` | `string` | GTM Container ID. |
| `type` | `string` | Client type. @mutable tagmanager.accounts.containers.workspaces.clients.create @mutable tagmanager.accounts.containers.workspaces.clients.update |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_containers_workspaces_clients_get` | `SELECT` | `accountsId, clientsId, containersId, workspacesId` | Gets a GTM Client. |
| `accounts_containers_workspaces_clients_list` | `SELECT` | `accountsId, containersId, workspacesId` | Lists all GTM Clients of a GTM container workspace. |
| `accounts_containers_workspaces_clients_create` | `INSERT` | `accountsId, containersId, workspacesId` | Creates a GTM Client. |
| `accounts_containers_workspaces_clients_delete` | `DELETE` | `accountsId, clientsId, containersId, workspacesId` | Deletes a GTM Client. |
| `accounts_containers_workspaces_clients_revert` | `EXEC` | `accountsId, clientsId, containersId, workspacesId` | Reverts changes to a GTM Client in a GTM Workspace. |
| `accounts_containers_workspaces_clients_update` | `EXEC` | `accountsId, clientsId, containersId, workspacesId` | Updates a GTM Client. |
