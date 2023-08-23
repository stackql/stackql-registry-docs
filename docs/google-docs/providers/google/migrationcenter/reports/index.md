---
title: reports
hide_title: false
hide_table_of_contents: false
keywords:
  - reports
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
<tr><td><b>Name</b></td><td><code>reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.migrationcenter.reports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of resource. |
| `description` | `string` | Free-text description. |
| `createTime` | `string` | Output only. Creation timestamp. |
| `displayName` | `string` | User-friendly display name. Maximum length is 63 characters. |
| `state` | `string` | Report creation state. |
| `summary` | `object` | Describes the Summary view of a Report, which contains aggregated values for all the groups and preference sets included in this Report. |
| `type` | `string` | Report type. |
| `updateTime` | `string` | Output only. Last update timestamp. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, reportConfigsId, reportsId` | Gets details of a single Report. |
| `list` | `SELECT` | `locationsId, projectsId, reportConfigsId` | Lists Reports in a given ReportConfig. |
| `create` | `INSERT` | `locationsId, projectsId, reportConfigsId` | Creates a report. |
| `delete` | `DELETE` | `locationsId, projectsId, reportConfigsId, reportsId` | Deletes a Report. |
| `_list` | `EXEC` | `locationsId, projectsId, reportConfigsId` | Lists Reports in a given ReportConfig. |
