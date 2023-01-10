---
title: vendors
hide_title: false
hide_table_of_contents: false
keywords:
  - vendors
  - androiddeviceprovisioning
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vendors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androiddeviceprovisioning.vendors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `vendors` | `array` | List of vendors of the reseller partner. Fields `name`, `companyId` and `companyName` are populated to the Company object. |
| `nextPageToken` | `string` | A token to retrieve the next page of results. Omitted if no further results are available. |
| `totalSize` | `integer` | The total count of items in the list irrespective of pagination. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `partners_vendors_list` | `SELECT` | `partnersId` |
