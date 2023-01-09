---
title: queries
hide_title: false
hide_table_of_contents: false
keywords:
  - queries
  - doubleclickbidmanager
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.doubleclickbidmanager.queries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `queryId` | `string` | Output only. Query ID. |
| `schedule` | `object` | Information on when and how frequently to run a query. |
| `metadata` | `object` | Query metadata. |
| `params` | `object` | Parameters of a query or report. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `queryId` | Retrieves a query. |
| `list` | `SELECT` |  | Lists queries created by the current user. |
| `create` | `INSERT` |  | Creates a query. |
| `delete` | `DELETE` | `queryId` | Deletes a query as well as the associated reports. |
| `run` | `EXEC` | `queryId` | Runs a stored query to generate a report. |
