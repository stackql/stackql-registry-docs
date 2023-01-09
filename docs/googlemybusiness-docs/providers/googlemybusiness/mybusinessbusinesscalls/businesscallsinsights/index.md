---
title: businesscallsinsights
hide_title: false
hide_table_of_contents: false
keywords:
  - businesscallsinsights
  - mybusinessbusinesscalls
  - googlemybusiness    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googlemybusiness/stackql-googlemybusiness-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>businesscallsinsights</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googlemybusiness.mybusinessbusinesscalls.businesscallsinsights</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `businessCallsInsights` | `array` | A collection of business calls insights for the location. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. Some of the metric_types (e.g, AGGREGATE_COUNT) returns a single page. For these metrics, the next_page_token will be empty. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `locations_businesscallsinsights_list` | `SELECT` | `locationsId` |
