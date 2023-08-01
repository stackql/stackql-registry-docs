---
title: uptime_check_ips
hide_title: false
hide_table_of_contents: false
keywords:
  - uptime_check_ips
  - monitoring
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
<tr><td><b>Name</b></td><td><code>uptime_check_ips</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.monitoring.uptime_check_ips</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | This field represents the pagination token to retrieve the next page of results. If the value is empty, it means no further results for the request. To retrieve the next page of results, the value of the next_page_token is passed to the subsequent List method call (in the request message's page_token field). NOTE: this field is not yet implemented |
| `uptimeCheckIps` | `array` | The returned list of IP addresses (including region and location) that the checkers run from. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `uptime_check_ips_list` | `SELECT` |  |
