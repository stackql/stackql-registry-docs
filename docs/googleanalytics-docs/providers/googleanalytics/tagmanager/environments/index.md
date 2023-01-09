---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
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
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.tagmanager.environments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The environment display name. Can be set or changed only on USER type environments. @mutable tagmanager.accounts.containers.environments.create @mutable tagmanager.accounts.containers.environments.update |
| `description` | `string` | The environment description. Can be set or changed only on USER type environments. @mutable tagmanager.accounts.containers.environments.create @mutable tagmanager.accounts.containers.environments.update |
| `type` | `string` | The type of this environment. |
| `path` | `string` | GTM Environment's API relative path. |
| `authorizationTimestamp` | `string` | The last update time-stamp for the authorization code. |
| `accountId` | `string` | GTM Account ID. |
| `enableDebug` | `boolean` | Whether or not to enable debug by default for the environment. @mutable tagmanager.accounts.containers.environments.create @mutable tagmanager.accounts.containers.environments.update |
| `fingerprint` | `string` | The fingerprint of the GTM environment as computed at storage time. This value is recomputed whenever the environment is modified. |
| `containerVersionId` | `string` | Represents a link to a container version. |
| `workspaceId` | `string` | Represents a link to a quick preview of a workspace. |
| `authorizationCode` | `string` | The environment authorization code. |
| `url` | `string` | Default preview page url for the environment. @mutable tagmanager.accounts.containers.environments.create @mutable tagmanager.accounts.containers.environments.update |
| `containerId` | `string` | GTM Container ID. |
| `environmentId` | `string` | GTM Environment ID uniquely identifies the GTM Environment. |
| `tagManagerUrl` | `string` | Auto generated link to the tag manager UI |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_containers_environments_get` | `SELECT` | `accountsId, containersId, environmentsId` | Gets a GTM Environment. |
| `accounts_containers_environments_list` | `SELECT` | `accountsId, containersId` | Lists all GTM Environments of a GTM Container. |
| `accounts_containers_environments_create` | `INSERT` | `accountsId, containersId` | Creates a GTM Environment. |
| `accounts_containers_environments_delete` | `DELETE` | `accountsId, containersId, environmentsId` | Deletes a GTM Environment. |
| `accounts_containers_environments_reauthorize` | `EXEC` | `accountsId, containersId, environmentsId` | Re-generates the authorization code for a GTM Environment. |
| `accounts_containers_environments_update` | `EXEC` | `accountsId, containersId, environmentsId` | Updates a GTM Environment. |
