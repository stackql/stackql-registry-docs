---
title: dns_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_peerings
  - datafusion
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
<tr><td><b>Name</b></td><td><code>dns_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datafusion.dns_peerings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `dnsPeerings` | `array` | List of dns peering. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `instancesId, locationsId, projectsId` | Lists DNS peerings for a given resource. |
| `create` | `INSERT` | `instancesId, locationsId, projectsId` | Creates DNS peering on the given resource. |
| `delete` | `DELETE` | `dnsPeeringsId, instancesId, locationsId, projectsId` | Deletes DNS peering on the given resource. |
