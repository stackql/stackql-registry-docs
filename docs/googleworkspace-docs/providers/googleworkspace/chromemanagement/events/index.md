---
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
  - chromemanagement
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
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.chromemanagement.events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `telemetryEvents` | `array` | Telemetry events returned in the response. |
| `nextPageToken` | `string` | Token to specify next page in the list. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `customers_telemetry_events_list` | `SELECT` | `customersId` |
