---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
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
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.tagmanager.tags</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Tag display name. @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update |
| `fingerprint` | `string` | The fingerprint of the GTM Tag as computed at storage time. This value is recomputed whenever the tag is modified. |
| `monitoringMetadataTagNameKey` | `string` | If non-empty, then the tag display name will be included in the monitoring metadata map using the key specified. @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update |
| `blockingRuleId` | `array` | Blocking rule IDs. If any of the listed rules evaluate to true, the tag will not fire. @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update |
| `scheduleStartMs` | `string` | The start timestamp in milliseconds to schedule a tag. @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update |
| `parameter` | `array` | The tag's parameters. @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update |
| `scheduleEndMs` | `string` | The end timestamp in milliseconds to schedule a tag. @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update |
| `setupTag` | `array` | The list of setup tags. Currently we only allow one. |
| `parentFolderId` | `string` | Parent folder id. |
| `accountId` | `string` | GTM Account ID. |
| `firingTriggerId` | `array` | Firing trigger IDs. A tag will fire when any of the listed triggers are true and all of its blockingTriggerIds (if any specified) are false. @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update |
| `paused` | `boolean` | Indicates whether the tag is paused, which prevents the tag from firing. @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update |
| `notes` | `string` | User notes on how to apply this tag in the container. @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update |
| `workspaceId` | `string` | GTM Workspace ID. |
| `tagFiringOption` | `string` | Option to fire this tag. |
| `tagId` | `string` | The Tag ID uniquely identifies the GTM Tag. |
| `tagManagerUrl` | `string` | Auto generated link to the tag manager UI |
| `blockingTriggerId` | `array` | Blocking trigger IDs. If any of the listed triggers evaluate to true, the tag will not fire. @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update |
| `firingRuleId` | `array` | Firing rule IDs. A tag will fire when any of the listed rules are true and all of its blockingRuleIds (if any specified) are false. @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update |
| `type` | `string` | GTM Tag Type. @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update |
| `teardownTag` | `array` | The list of teardown tags. Currently we only allow one. |
| `priority` | `object` | Represents a Google Tag Manager Parameter. |
| `monitoringMetadata` | `object` | Represents a Google Tag Manager Parameter. |
| `consentSettings` | `object` |  |
| `path` | `string` | GTM Tag's API relative path. |
| `containerId` | `string` | GTM Container ID. |
| `liveOnly` | `boolean` | If set to true, this tag will only fire in the live environment (e.g. not in preview or debug mode). @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_containers_workspaces_tags_get` | `SELECT` | `accountsId, containersId, tagsId, workspacesId` | Gets a GTM Tag. |
| `accounts_containers_workspaces_tags_list` | `SELECT` | `accountsId, containersId, workspacesId` | Lists all GTM Tags of a Container. |
| `accounts_containers_workspaces_tags_create` | `INSERT` | `accountsId, containersId, workspacesId` | Creates a GTM Tag. |
| `accounts_containers_workspaces_tags_delete` | `DELETE` | `accountsId, containersId, tagsId, workspacesId` | Deletes a GTM Tag. |
| `accounts_containers_workspaces_tags_revert` | `EXEC` | `accountsId, containersId, tagsId, workspacesId` | Reverts changes to a GTM Tag in a GTM Workspace. |
| `accounts_containers_workspaces_tags_update` | `EXEC` | `accountsId, containersId, tagsId, workspacesId` | Updates a GTM Tag. |
