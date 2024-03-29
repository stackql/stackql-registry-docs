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
| `region` | `string` | A broad region category in which the IP address is located. |
| `ipAddress` | `string` | The IP address from which the Uptime check originates. This is a fully specified IP address (not an IP address range). Most IP addresses, as of this publication, are in IPv4 format; however, one should not rely on the IP addresses being in IPv4 format indefinitely, and should support interpreting this field in either IPv4 or IPv6 format. |
| `location` | `string` | A more specific location within the region that typically encodes a particular city/town/metro (and its containing state/province or country) within the broader umbrella region category. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `uptime_check_ips_list` | `SELECT` |  |
| `_uptime_check_ips_list` | `EXEC` |  |
