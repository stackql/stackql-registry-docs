---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
  - securitycenter
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.assets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `asset` | `object` | Security Command Center representation of a Google Cloud resource. The Asset is a Security Command Center resource that captures information about a single Google Cloud resource. All modifications to an Asset are only within the context of Security Command Center and don't affect the referenced Google Cloud resource. |
| `stateChange` | `string` | State change of the asset between the points in time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_assets_list` | `SELECT` | `foldersId` | Lists an organization's assets. |
| `organizations_assets_list` | `SELECT` | `organizationsId` | Lists an organization's assets. |
| `projects_assets_list` | `SELECT` | `projectsId` | Lists an organization's assets. |
| `_folders_assets_list` | `EXEC` | `foldersId` | Lists an organization's assets. |
| `_organizations_assets_list` | `EXEC` | `organizationsId` | Lists an organization's assets. |
| `_projects_assets_list` | `EXEC` | `projectsId` | Lists an organization's assets. |
| `folders_assets_group` | `EXEC` | `foldersId` | Filters an organization's assets and groups them by their specified properties. |
| `organizations_assets_group` | `EXEC` | `organizationsId` | Filters an organization's assets and groups them by their specified properties. |
| `organizations_assets_run_discovery` | `EXEC` | `organizationsId` | Runs asset discovery. The discovery is tracked with a long-running operation. This API can only be called with limited frequency for an organization. If it is called too frequently the caller will receive a TOO_MANY_REQUESTS error. |
| `projects_assets_group` | `EXEC` | `projectsId` | Filters an organization's assets and groups them by their specified properties. |
