---
title: analyses
hide_title: false
hide_table_of_contents: false
keywords:
  - analyses
  - contactcenterinsights
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
<tr><td><b>Name</b></td><td><code>analyses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contactcenterinsights.analyses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `analyses` | `array` | The analyses that match the request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `analysesId, conversationsId, locationsId, projectsId` | Gets an analysis. |
| `list` | `SELECT` | `conversationsId, locationsId, projectsId` | Lists analyses. |
| `create` | `INSERT` | `conversationsId, locationsId, projectsId` | Creates an analysis. The long running operation is done when the analysis has completed. |
| `delete` | `DELETE` | `analysesId, conversationsId, locationsId, projectsId` | Deletes an analysis. |
