---
title: replication_cycles
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_cycles
  - vmmigration
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
<tr><td><b>Name</b></td><td><code>replication_cycles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vmmigration.replication_cycles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Output only. A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `replicationCycles` | `array` | Output only. The list of replication cycles response. |
| `unreachable` | `array` | Output only. Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, migratingVmsId, projectsId, replicationCyclesId, sourcesId` | Gets details of a single ReplicationCycle. |
| `list` | `SELECT` | `locationsId, migratingVmsId, projectsId, sourcesId` | Lists ReplicationCycles in a given MigratingVM. |
