---
title: combined_audiences
hide_title: false
hide_table_of_contents: false
keywords:
  - combined_audiences
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
<tr><td><b>Name</b></td><td><code>combined_audiences</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.combined_audiences</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the combined audience. |
| `combinedAudienceId` | `string` | Output only. The unique ID of the combined audience. Assigned by the system. |
| `displayName` | `string` | Output only. The display name of the combined audience. . |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `combinedAudiences_get` | `SELECT` | `combinedAudiencesId` | Gets a combined audience. |
| `combinedAudiences_list` | `SELECT` |  | Lists combined audiences. The order is defined by the order_by parameter. |
