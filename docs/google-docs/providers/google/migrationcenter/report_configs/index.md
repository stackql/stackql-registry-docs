---
title: report_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - report_configs
  - migrationcenter
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
<tr><td><b>Name</b></td><td><code>report_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.migrationcenter.report_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | A token identifying a page of results the server should return. |
| `reportConfigs` | `array` | A list of report configs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, reportConfigsId` | Gets details of a single ReportConfig. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists ReportConfigs in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a report configuration. |
| `delete` | `DELETE` | `locationsId, projectsId, reportConfigsId` | Deletes a ReportConfig. |
