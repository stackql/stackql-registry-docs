---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - managedidentities
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.managedidentities.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The unique name of the Backup in the form of `projects/{project_id}/locations/global/domains/{domain_name}/backups/{name}` |
| `statusMessage` | `string` | Output only. Additional information about the current status of this backup, if available. |
| `type` | `string` | Output only. Indicates whether it’s an on-demand backup or scheduled. |
| `updateTime` | `string` | Output only. Last update time. |
| `createTime` | `string` | Output only. The time the backups was created. |
| `labels` | `object` | Optional. Resource labels to represent user provided metadata. |
| `state` | `string` | Output only. The current state of the backup. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_global_domains_backups_get` | `SELECT` | `backupsId, domainsId, projectsId` | Gets details of a single Backup. |
| `projects_locations_global_domains_backups_list` | `SELECT` | `domainsId, projectsId` | Lists Backup in a given project. |
| `projects_locations_global_domains_backups_create` | `INSERT` | `domainsId, projectsId` | Creates a Backup for a domain. |
| `projects_locations_global_domains_backups_delete` | `DELETE` | `backupsId, domainsId, projectsId` | Deletes identified Backup. |
| `projects_locations_global_domains_backups_patch` | `EXEC` | `backupsId, domainsId, projectsId` | Updates the labels for specified Backup. |
