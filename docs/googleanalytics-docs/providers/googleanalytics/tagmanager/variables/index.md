---
title: variables
hide_title: false
hide_table_of_contents: false
keywords:
  - variables
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
<tr><td><b>Name</b></td><td><code>variables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.tagmanager.variables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Variable display name. @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update |
| `variableId` | `string` | The Variable ID uniquely identifies the GTM Variable. |
| `fingerprint` | `string` | The fingerprint of the GTM Variable as computed at storage time. This value is recomputed whenever the variable is modified. |
| `parameter` | `array` | The variable's parameters. @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update |
| `path` | `string` | GTM Variable's API relative path. |
| `enablingTriggerId` | `array` | For mobile containers only: A list of trigger IDs for enabling conditional variables; the variable is enabled if one of the enabling triggers is true while all the disabling triggers are false. Treated as an unordered set. @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update |
| `scheduleEndMs` | `string` | The end timestamp in milliseconds to schedule a variable. @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update |
| `formatValue` | `object` |  |
| `type` | `string` | GTM Variable Type. @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update |
| `workspaceId` | `string` | GTM Workspace ID. |
| `scheduleStartMs` | `string` | The start timestamp in milliseconds to schedule a variable. @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update |
| `parentFolderId` | `string` | Parent folder id. |
| `accountId` | `string` | GTM Account ID. |
| `disablingTriggerId` | `array` | For mobile containers only: A list of trigger IDs for disabling conditional variables; the variable is enabled if one of the enabling trigger is true while all the disabling trigger are false. Treated as an unordered set. @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update |
| `containerId` | `string` | GTM Container ID. |
| `notes` | `string` | User notes on how to apply this variable in the container. @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update |
| `tagManagerUrl` | `string` | Auto generated link to the tag manager UI |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_containers_workspaces_variables_get` | `SELECT` | `accountsId, containersId, variablesId, workspacesId` | Gets a GTM Variable. |
| `accounts_containers_workspaces_variables_list` | `SELECT` | `accountsId, containersId, workspacesId` | Lists all GTM Variables of a Container. |
| `accounts_containers_workspaces_variables_create` | `INSERT` | `accountsId, containersId, workspacesId` | Creates a GTM Variable. |
| `accounts_containers_workspaces_variables_delete` | `DELETE` | `accountsId, containersId, variablesId, workspacesId` | Deletes a GTM Variable. |
| `accounts_containers_workspaces_variables_revert` | `EXEC` | `accountsId, containersId, variablesId, workspacesId` | Reverts changes to a GTM Variable in a GTM Workspace. |
| `accounts_containers_workspaces_variables_update` | `EXEC` | `accountsId, containersId, variablesId, workspacesId` | Updates a GTM Variable. |
