---
title: ideas
hide_title: false
hide_table_of_contents: false
keywords:
  - ideas
  - ideahub
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
<tr><td><b>Name</b></td><td><code>ideas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.ideahub.ideas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `ideas` | `array` | Results for the ListIdeasRequest. |
| `nextPageToken` | `string` | Used to fetch the next page in a subsequent request. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `platforms_properties_ideas_list` | `SELECT` | `platformsId, propertiesId` |