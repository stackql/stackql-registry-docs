---
title: collectors
hide_title: false
hide_table_of_contents: false
keywords:
  - collectors
  - ingest_budgets
  - sumologic    
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
<tr><td><b>Name</b></td><td><code>collectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.ingest_budgets.collectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier for the Collector. |
| `name` | `string` | The name of the Collector. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getAssignedCollectors` | `SELECT` | `id` | Get a list of Collectors assigned to an ingest budget. The response is paginated with a default limit of 100 Collectors per page. |
| `removeCollectorFromBudget` | `DELETE` | `collectorId, id` | Remove Collector from a budget. |
| `assignCollectorToBudget` | `EXEC` | `collectorId, id` | Assign a Collector to a budget. |
