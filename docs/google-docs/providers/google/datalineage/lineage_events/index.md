---
title: lineage_events
hide_title: false
hide_table_of_contents: false
keywords:
  - lineage_events
  - datalineage
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
<tr><td><b>Name</b></td><td><code>lineage_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datalineage.lineage_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name of the lineage event. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/processes/&#123;process&#125;/runs/&#123;run&#125;/lineageEvents/&#123;lineage_event&#125;`. Can be specified or auto-assigned. &#123;lineage_event&#125; must be not longer than 200 characters and only contain characters in a set: `a-zA-Z0-9_-:.` |
| `startTime` | `string` | Required. The beginning of the transformation which resulted in this lineage event. For streaming scenarios, it should be the beginning of the period from which the lineage is being reported. |
| `endTime` | `string` | Optional. The end of the transformation which resulted in this lineage event. For streaming scenarios, it should be the end of the period from which the lineage is being reported. |
| `links` | `array` | Optional. List of source-target pairs. Can't contain more than 100 tuples. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `lineageEventsId, locationsId, processesId, projectsId, runsId` | Gets details of a specified lineage event. |
| `list` | `SELECT` | `locationsId, processesId, projectsId, runsId` | Lists lineage events in the given project and location. The list order is not defined. |
| `create` | `INSERT` | `locationsId, processesId, projectsId, runsId` | Creates a new lineage event. |
| `delete` | `DELETE` | `lineageEventsId, locationsId, processesId, projectsId, runsId` | Deletes the lineage event with the specified name. |
