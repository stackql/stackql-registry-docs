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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `backups` | `array` | A list of Cloud AD backups in the domain. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `unreachable` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupsId, domainsId, projectsId` | Gets details of a single Backup. |
| `list` | `SELECT` | `domainsId, projectsId` | Lists Backup in a given project. |
| `create` | `INSERT` | `domainsId, projectsId` | Creates a Backup for a domain. |
| `delete` | `DELETE` | `backupsId, domainsId, projectsId` | Deletes identified Backup. |
| `patch` | `EXEC` | `backupsId, domainsId, projectsId` | Updates the labels for specified Backup. |
