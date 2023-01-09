---
title: saved
hide_title: false
hide_table_of_contents: false
keywords:
  - saved
  - adsense
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>saved</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adsense.saved</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `savedReports` | `array` | The reports returned in this list response. |
| `nextPageToken` | `string` | Continuation token used to page through reports. To retrieve the next page of the results, set the next request's "page_token" value to this. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_reports_saved_list` | `SELECT` | `accountsId` | Lists saved reports. |
| `accounts_reports_saved_generate` | `EXEC` | `accountsId, reportsId` | Generates a saved report. |
| `accounts_reports_saved_generateCsv` | `EXEC` | `accountsId, reportsId` | Generates a csv formatted saved report. |
