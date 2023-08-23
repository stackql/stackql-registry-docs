---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - firestore
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
<tr><td><b>Id</b></td><td><code>google.firestore.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `backups` | `array` | List of all backups for the project. Ordered by `location ASC, create_time DESC, name ASC`. |
| `unreachable` | `array` | List of locations that existing backups were not able to be fetched from. Instead of failing the entire requests when a single location is unreachable, this response returns a partial result set and list of locations unable to be reached here. The request can be retried against a single location to get a concrete error. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupsId, locationsId, projectsId` | Gets information about a backup. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all the backups. |
| `delete` | `DELETE` | `backupsId, locationsId, projectsId` | Deletes a backup. |
