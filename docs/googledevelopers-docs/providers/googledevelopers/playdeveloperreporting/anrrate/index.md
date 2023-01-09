---
title: anrrate
hide_title: false
hide_table_of_contents: false
keywords:
  - anrrate
  - playdeveloperreporting
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anrrate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.playdeveloperreporting.anrrate</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name. Format: apps/&#123;app&#125;/anrRateMetricSet |
| `freshnessInfo` | `object` | Represents the latest available time that can be requested in a TimelineSpec. Different aggregation periods have different freshness. For example, `DAILY` aggregation may lag behind `HOURLY` in cases where such aggregation is computed only once at the end of the day. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `vitals_anrrate_get` | `SELECT` | `appsId` | Describes the properties of the metric set. |
| `vitals_anrrate_query` | `EXEC` | `appsId` | Queries the metrics in the metric set. |
