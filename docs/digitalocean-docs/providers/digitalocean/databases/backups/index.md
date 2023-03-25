---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - databases
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.databases.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `created_at` | `string` | A time value given in ISO8601 combined date and time format at which the backup was created. |
| `size_gigabytes` | `number` | The size of the database backup in GBs. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_backups` | `SELECT` | `database_cluster_uuid` |
| `_list_backups` | `EXEC` | `database_cluster_uuid` |
