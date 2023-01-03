---
title: continuous_test_results
hide_title: false
hide_table_of_contents: false
keywords:
  - continuous_test_results
  - dialogflow
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
<tr><td><b>Name</b></td><td><code>continuous_test_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.continuous_test_results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `continuousTestResults` | `array` | The list of continuous test results. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_agents_environments_continuousTestResults_list` | `SELECT` | `agentsId, environmentsId, locationsId, projectsId` |
