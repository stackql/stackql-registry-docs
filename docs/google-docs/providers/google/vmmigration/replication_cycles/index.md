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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `startTime` | `string` | The time the replication cycle has started. |
| `progressPercent` | `integer` | The current progress in percentage of this cycle. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_sources_migratingVms_replicationCycles_get` | `SELECT` | `locationsId, migratingVmsId, projectsId, replicationCyclesId, sourcesId` | Gets details of a single ReplicationCycle. |
| `projects_locations_sources_migratingVms_replicationCycles_list` | `SELECT` | `locationsId, migratingVmsId, projectsId, sourcesId` | Lists ReplicationCycles in a given MigratingVM. |
