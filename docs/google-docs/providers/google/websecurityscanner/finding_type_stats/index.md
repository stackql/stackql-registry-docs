---
title: finding_type_stats
hide_title: false
hide_table_of_contents: false
keywords:
  - finding_type_stats
  - websecurityscanner
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
<tr><td><b>Name</b></td><td><code>finding_type_stats</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.websecurityscanner.finding_type_stats</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `findingType` | `string` | Output only. The finding type associated with the stats. |
| `findingCount` | `integer` | Output only. The count of findings belonging to this finding type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_scanConfigs_scanRuns_findingTypeStats_list` | `SELECT` | `projectsId, scanConfigsId, scanRunsId` |
