---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
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
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.tagmanager.versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Container version display name. @mutable tagmanager.accounts.containers.versions.update |
| `description` | `string` | Container version description. @mutable tagmanager.accounts.containers.versions.update |
| `trigger` | `array` | The triggers in the container that this version was taken from. |
| `variable` | `array` | The variables in the container that this version was taken from. |
| `deleted` | `boolean` | A value of true indicates this container version has been deleted. |
| `zone` | `array` | The zones in the container that this version was taken from. |
| `folder` | `array` | The folders in the container that this version was taken from. |
| `path` | `string` | GTM Container Version's API relative path. |
| `container` | `object` | Represents a Google Tag Manager Container, which specifies the platform tags will run on, manages workspaces, and retains container versions. |
| `customTemplate` | `array` | The custom templates in the container that this version was taken from. |
| `builtInVariable` | `array` | The built-in variables in the container that this version was taken from. |
| `fingerprint` | `string` | The fingerprint of the GTM Container Version as computed at storage time. This value is recomputed whenever the container version is modified. |
| `tag` | `array` | The tags in the container that this version was taken from. |
| `containerId` | `string` | GTM Container ID. |
| `accountId` | `string` | GTM Account ID. |
| `tagManagerUrl` | `string` | Auto generated link to the tag manager UI |
| `client` | `array` | The clients in the container that this version was taken from. |
| `gtagConfig` | `array` | The Google tag configs in the container that this version was taken from. |
| `containerVersionId` | `string` | The Container Version ID uniquely identifies the GTM Container Version. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_containers_versions_get` | `SELECT` | `accountsId, containersId, versionsId` | Gets a Container Version. |
| `accounts_containers_versions_delete` | `DELETE` | `accountsId, containersId, versionsId` | Deletes a Container Version. |
| `accounts_containers_versions_live` | `EXEC` | `accountsId, containersId` | Gets the live (i.e. published) container version |
| `accounts_containers_versions_publish` | `EXEC` | `accountsId, containersId, versionsId` | Publishes a Container Version. |
| `accounts_containers_versions_set_latest` | `EXEC` | `accountsId, containersId, versionsId` | Sets the latest version used for synchronization of workspaces when detecting conflicts and errors. |
| `accounts_containers_versions_undelete` | `EXEC` | `accountsId, containersId, versionsId` | Undeletes a Container Version. |
| `accounts_containers_versions_update` | `EXEC` | `accountsId, containersId, versionsId` | Updates a Container Version. |
