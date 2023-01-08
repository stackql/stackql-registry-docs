---
title: locales
hide_title: false
hide_table_of_contents: false
keywords:
  - locales
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
<tr><td><b>Name</b></td><td><code>locales</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.ideahub.locales</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `availableLocales` | `array` | Locales for which ideas are available for the given Creator. |
| `nextPageToken` | `string` | A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `platforms_properties_locales_list` | `SELECT` | `platformsId, propertiesId` |
