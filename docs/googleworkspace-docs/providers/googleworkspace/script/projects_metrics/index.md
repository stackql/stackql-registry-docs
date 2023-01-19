---
title: projects_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - projects_metrics
  - script
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.script.projects_metrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `failedExecutions` | `array` | Number of failed executions. |
| `totalExecutions` | `array` | Number of total executions. |
| `activeUsers` | `array` | Number of active users. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_getMetrics` | `SELECT` | `scriptId` |
