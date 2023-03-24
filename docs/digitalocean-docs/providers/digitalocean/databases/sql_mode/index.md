---
title: sql_mode
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_mode
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
<tr><td><b>Name</b></td><td><code>sql_mode</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.databases.sql_mode</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_sql_mode` | `SELECT` | `database_cluster_uuid` | To retrieve the configured SQL modes for an existing MySQL cluster, send a GET request to `/v2/databases/$DATABASE_ID/sql_mode`.<br />The response will be a JSON object with a `sql_mode` key. This will be set to a string representing the configured SQL modes. |
| `update_sql_mode` | `EXEC` | `database_cluster_uuid, data__sql_mode` | To configure the SQL modes for an existing MySQL cluster, send a PUT request to `/v2/databases/$DATABASE_ID/sql_mode` specifying the desired modes. See the official MySQL 8 documentation for a [full list of supported SQL modes](https://dev.mysql.com/doc/refman/8.0/en/sql-mode.html#sql-mode-full).<br />A successful request will receive a 204 No Content status code with no body in response. |
