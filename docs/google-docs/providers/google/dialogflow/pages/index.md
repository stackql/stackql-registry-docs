---
title: pages
hide_title: false
hide_table_of_contents: false
keywords:
  - pages
  - dialogflow
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
<tr><td><b>Name</b></td><td><code>pages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.pages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `pages` | `array` | The list of pages. There will be a maximum number of items returned based on the page_size field in the request. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_flows_pages_get` | `SELECT` | `agentsId, flowsId, locationsId, pagesId, projectsId` | Retrieves the specified page. |
| `projects_locations_agents_flows_pages_list` | `SELECT` | `agentsId, flowsId, locationsId, projectsId` | Returns the list of all pages in the specified flow. |
| `projects_locations_agents_flows_pages_create` | `INSERT` | `agentsId, flowsId, locationsId, projectsId` | Creates a page in the specified flow. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_flows_pages_delete` | `DELETE` | `agentsId, flowsId, locationsId, pagesId, projectsId` | Deletes the specified page. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_flows_pages_patch` | `EXEC` | `agentsId, flowsId, locationsId, pagesId, projectsId` | Updates the specified page. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
