---
title: zones
hide_title: false
hide_table_of_contents: false
keywords:
  - zones
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
<tr><td><b>Name</b></td><td><code>zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.tagmanager.zones</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Zone display name. |
| `typeRestriction` | `object` | Represents a Zone's type restrictions. |
| `workspaceId` | `string` | GTM Workspace ID. |
| `notes` | `string` | User notes on how to apply this zone in the container. |
| `boundary` | `object` | Represents a Zone's boundaries. |
| `containerId` | `string` | GTM Container ID. |
| `zoneId` | `string` | The Zone ID uniquely identifies the GTM Zone. |
| `path` | `string` | GTM Zone's API relative path. |
| `tagManagerUrl` | `string` | Auto generated link to the tag manager UI |
| `accountId` | `string` | GTM Account ID. |
| `childContainer` | `array` | Containers that are children of this Zone. |
| `fingerprint` | `string` | The fingerprint of the GTM Zone as computed at storage time. This value is recomputed whenever the zone is modified. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_containers_workspaces_zones_get` | `SELECT` | `accountsId, containersId, workspacesId, zonesId` | Gets a GTM Zone. |
| `accounts_containers_workspaces_zones_list` | `SELECT` | `accountsId, containersId, workspacesId` | Lists all GTM Zones of a GTM container workspace. |
| `accounts_containers_workspaces_zones_create` | `INSERT` | `accountsId, containersId, workspacesId` | Creates a GTM Zone. |
| `accounts_containers_workspaces_zones_delete` | `DELETE` | `accountsId, containersId, workspacesId, zonesId` | Deletes a GTM Zone. |
| `accounts_containers_workspaces_zones_revert` | `EXEC` | `accountsId, containersId, workspacesId, zonesId` | Reverts changes to a GTM Zone in a GTM Workspace. |
| `accounts_containers_workspaces_zones_update` | `EXEC` | `accountsId, containersId, workspacesId, zonesId` | Updates a GTM Zone. |
