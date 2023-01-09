---
title: shoppingadsprogram
hide_title: false
hide_table_of_contents: false
keywords:
  - shoppingadsprogram
  - content
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
<tr><td><b>Name</b></td><td><code>shoppingadsprogram</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.shoppingadsprogram</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `globalState` | `string` | State of the program. `ENABLED` if there are offers for at least one region. |
| `regionStatuses` | `array` | Status of the program in each region. Regions with the same status and review eligibility are grouped together in `regionCodes`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `merchantId` | Retrieves the status and review eligibility for the Shopping Ads program. Returns errors and warnings if they require action to resolve, will become disapprovals, or impact impressions. Use `accountstatuses` to view all issues for an account. |
| `requestreview` | `EXEC` | `merchantId` | Requests a review of Shopping ads in a specific region. This method is only available to selected merchants. |
