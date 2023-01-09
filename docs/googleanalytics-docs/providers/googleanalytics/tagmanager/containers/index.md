---
title: containers
hide_title: false
hide_table_of_contents: false
keywords:
  - containers
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
<tr><td><b>Name</b></td><td><code>containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.tagmanager.containers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Container display name. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update |
| `fingerprint` | `string` | The fingerprint of the GTM Container as computed at storage time. This value is recomputed whenever the account is modified. |
| `taggingServerUrls` | `array` | List of server-side container URLs for the Container. If multiple URLs are provided, all URL paths must match. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update |
| `containerId` | `string` | The Container ID uniquely identifies the GTM Container. |
| `features` | `object` |  |
| `domainName` | `array` | List of domain names associated with the Container. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update |
| `usageContext` | `array` | List of Usage Contexts for the Container. Valid values include: web, android, or ios. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update |
| `accountId` | `string` | GTM Account ID. |
| `publicId` | `string` | Container Public ID. |
| `tagManagerUrl` | `string` | Auto generated link to the tag manager UI |
| `path` | `string` | GTM Container's API relative path. |
| `tagIds` | `array` | All Tag IDs that refer to this Container. |
| `notes` | `string` | Container Notes. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_containers_get` | `SELECT` | `accountsId, containersId` | Gets a Container. |
| `accounts_containers_list` | `SELECT` | `accountsId` | Lists all Containers that belongs to a GTM Account. |
| `accounts_containers_create` | `INSERT` | `accountsId` | Creates a Container. |
| `accounts_containers_delete` | `DELETE` | `accountsId, containersId` | Deletes a Container. |
| `accounts_containers_combine` | `EXEC` | `accountsId, containersId` | Combines Containers. |
| `accounts_containers_lookup` | `EXEC` |  | Looks up a Container by destination ID. |
| `accounts_containers_move_tag_id` | `EXEC` | `accountsId, containersId` | Move Tag ID out of a Container. |
| `accounts_containers_snippet` | `EXEC` | `accountsId, containersId` | Gets the tagging snippet for a Container. |
| `accounts_containers_update` | `EXEC` | `accountsId, containersId` | Updates a Container. |
