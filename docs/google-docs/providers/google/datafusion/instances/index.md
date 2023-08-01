---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - datafusion
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
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datafusion.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `instances` | `array` | Represents a list of Data Fusion instances. |
| `nextPageToken` | `string` | Token to retrieve the next page of results or empty if there are no more results in the list. |
| `unreachable` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `instancesId, locationsId, projectsId` | Gets details of a single Data Fusion instance. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Data Fusion instances in the specified project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Data Fusion instance in the specified project and location. |
| `delete` | `DELETE` | `instancesId, locationsId, projectsId` | Deletes a single Date Fusion instance. |
| `patch` | `EXEC` | `instancesId, locationsId, projectsId` | Updates a single Data Fusion instance. |
| `restart` | `EXEC` | `instancesId, locationsId, projectsId` | Restart a single Data Fusion instance. At the end of an operation instance is fully restarted. |
