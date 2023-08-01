---
title: phrase_matchers
hide_title: false
hide_table_of_contents: false
keywords:
  - phrase_matchers
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
<tr><td><b>Name</b></td><td><code>phrase_matchers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contactcenterinsights.phrase_matchers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `phraseMatchers` | `array` | The phrase matchers that match the request. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, phraseMatchersId, projectsId` | Gets a phrase matcher. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists phrase matchers. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a phrase matcher. |
| `delete` | `DELETE` | `locationsId, phraseMatchersId, projectsId` | Deletes a phrase matcher. |
| `patch` | `EXEC` | `locationsId, phraseMatchersId, projectsId` | Updates a phrase matcher. |
