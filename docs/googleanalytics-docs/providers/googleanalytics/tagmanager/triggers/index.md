---
title: triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - triggers
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
<tr><td><b>Name</b></td><td><code>triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.tagmanager.triggers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Trigger display name. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update |
| `eventName` | `object` | Represents a Google Tag Manager Parameter. |
| `customEventFilter` | `array` | Used in the case of custom event, which is fired iff all Conditions are true. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update |
| `visibilitySelector` | `object` | Represents a Google Tag Manager Parameter. |
| `tagManagerUrl` | `string` | Auto generated link to the tag manager UI |
| `waitForTagsTimeout` | `object` | Represents a Google Tag Manager Parameter. |
| `uniqueTriggerId` | `object` | Represents a Google Tag Manager Parameter. |
| `triggerId` | `string` | The Trigger ID uniquely identifies the GTM Trigger. |
| `visiblePercentageMax` | `object` | Represents a Google Tag Manager Parameter. |
| `visiblePercentageMin` | `object` | Represents a Google Tag Manager Parameter. |
| `workspaceId` | `string` | GTM Workspace ID. |
| `totalTimeMinMilliseconds` | `object` | Represents a Google Tag Manager Parameter. |
| `type` | `string` | Defines the data layer event that causes this trigger. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update |
| `selector` | `object` | Represents a Google Tag Manager Parameter. |
| `parentFolderId` | `string` | Parent folder id. |
| `notes` | `string` | User notes on how to apply this trigger in the container. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update |
| `continuousTimeMinMilliseconds` | `object` | Represents a Google Tag Manager Parameter. |
| `checkValidation` | `object` | Represents a Google Tag Manager Parameter. |
| `horizontalScrollPercentageList` | `object` | Represents a Google Tag Manager Parameter. |
| `containerId` | `string` | GTM Container ID. |
| `maxTimerLengthSeconds` | `object` | Represents a Google Tag Manager Parameter. |
| `waitForTags` | `object` | Represents a Google Tag Manager Parameter. |
| `autoEventFilter` | `array` | Used in the case of auto event tracking. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update |
| `verticalScrollPercentageList` | `object` | Represents a Google Tag Manager Parameter. |
| `fingerprint` | `string` | The fingerprint of the GTM Trigger as computed at storage time. This value is recomputed whenever the trigger is modified. |
| `parameter` | `array` | Additional parameters. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update |
| `accountId` | `string` | GTM Account ID. |
| `limit` | `object` | Represents a Google Tag Manager Parameter. |
| `interval` | `object` | Represents a Google Tag Manager Parameter. |
| `intervalSeconds` | `object` | Represents a Google Tag Manager Parameter. |
| `filter` | `array` | The trigger will only fire iff all Conditions are true. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update |
| `path` | `string` | GTM Trigger's API relative path. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_containers_workspaces_triggers_get` | `SELECT` | `accountsId, containersId, triggersId, workspacesId` | Gets a GTM Trigger. |
| `accounts_containers_workspaces_triggers_list` | `SELECT` | `accountsId, containersId, workspacesId` | Lists all GTM Triggers of a Container. |
| `accounts_containers_workspaces_triggers_create` | `INSERT` | `accountsId, containersId, workspacesId` | Creates a GTM Trigger. |
| `accounts_containers_workspaces_triggers_delete` | `DELETE` | `accountsId, containersId, triggersId, workspacesId` | Deletes a GTM Trigger. |
| `accounts_containers_workspaces_triggers_revert` | `EXEC` | `accountsId, containersId, triggersId, workspacesId` | Reverts changes to a GTM Trigger in a GTM Workspace. |
| `accounts_containers_workspaces_triggers_update` | `EXEC` | `accountsId, containersId, triggersId, workspacesId` | Updates a GTM Trigger. |
