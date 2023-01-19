---
title: gtag_config
hide_title: false
hide_table_of_contents: false
keywords:
  - gtag_config
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
<tr><td><b>Name</b></td><td><code>gtag_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.tagmanager.gtag_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `accountId` | `string` | Google tag account ID. |
| `workspaceId` | `string` | Google tag workspace ID. Only used by GTM containers. Set to 0 otherwise. |
| `path` | `string` | Google tag config's API relative path. |
| `tagManagerUrl` | `string` | Auto generated link to the tag manager UI |
| `fingerprint` | `string` | The fingerprint of the Google tag config as computed at storage time. This value is recomputed whenever the config is modified. |
| `gtagConfigId` | `string` | The ID uniquely identifies the Google tag config. |
| `parameter` | `array` | The Google tag config's parameters. @mutable tagmanager.accounts.containers.workspaces.gtag_config.create @mutable tagmanager.accounts.containers.workspaces.gtag_config.update |
| `containerId` | `string` | Google tag container ID. |
| `type` | `string` | Google tag config type. @required tagmanager.accounts.containers.workspaces.gtag_config.create @required tagmanager.accounts.containers.workspaces.gtag_config.update @mutable tagmanager.accounts.containers.workspaces.gtag_config.create @mutable tagmanager.accounts.containers.workspaces.gtag_config.update |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_containers_workspaces_gtag_config_get` | `SELECT` | `accountsId, containersId, gtag_configId, workspacesId` | Gets a Google tag config. |
| `accounts_containers_workspaces_gtag_config_list` | `SELECT` | `accountsId, containersId, workspacesId` | Lists all Google tag configs in a Container. |
| `accounts_containers_workspaces_gtag_config_create` | `INSERT` | `accountsId, containersId, workspacesId` | Creates a Google tag config. |
| `accounts_containers_workspaces_gtag_config_delete` | `DELETE` | `accountsId, containersId, gtag_configId, workspacesId` | Deletes a Google tag config. |
| `accounts_containers_workspaces_gtag_config_update` | `EXEC` | `accountsId, containersId, gtag_configId, workspacesId` | Updates a Google tag config. |
