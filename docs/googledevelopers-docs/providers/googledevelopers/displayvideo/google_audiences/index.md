---
title: google_audiences
hide_title: false
hide_table_of_contents: false
keywords:
  - google_audiences
  - displayvideo
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
<tr><td><b>Name</b></td><td><code>google_audiences</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.google_audiences</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the google audience. |
| `googleAudienceType` | `string` | Output only. The type of Google audience. . |
| `displayName` | `string` | Output only. The display name of the Google audience. . |
| `googleAudienceId` | `string` | Output only. The unique ID of the Google audience. Assigned by the system. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `googleAudiences_get` | `SELECT` | `googleAudiencesId` | Gets a Google audience. |
| `googleAudiences_list` | `SELECT` |  | Lists Google audiences. The order is defined by the order_by parameter. |
