---
title: snoozes
hide_title: false
hide_table_of_contents: false
keywords:
  - snoozes
  - monitoring
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
<tr><td><b>Name</b></td><td><code>snoozes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.monitoring.snoozes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Page token for repeated calls to ListSnoozes, to fetch additional pages of results. If this is empty or missing, there are no more pages. |
| `snoozes` | `array` | Snoozes matching this list call. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_snoozes_get` | `SELECT` | `projectsId, snoozesId` | Retrieves a Snooze by name. |
| `projects_snoozes_list` | `SELECT` | `projectsId` | Lists the Snoozes associated with a project. Can optionally pass in filter, which specifies predicates to match Snoozes. |
| `projects_snoozes_create` | `INSERT` | `projectsId` | Creates a Snooze that will prevent alerts, which match the provided criteria, from being opened. The Snooze applies for a specific time interval. |
| `projects_snoozes_patch` | `EXEC` | `projectsId, snoozesId` | Updates a Snooze, identified by its name, with the parameters in the given Snooze object. |
