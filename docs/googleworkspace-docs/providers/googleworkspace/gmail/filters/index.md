---
title: filters
hide_title: false
hide_table_of_contents: false
keywords:
  - filters
  - gmail
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.gmail.filters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The server assigned ID of the filter. |
| `action` | `object` | A set of actions to perform on a message. |
| `criteria` | `object` | Message matching criteria. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `users_settings_filters_get` | `SELECT` | `id, userId` | Gets a filter. |
| `users_settings_filters_list` | `SELECT` | `userId` | Lists the message filters of a Gmail user. |
| `users_settings_filters_create` | `INSERT` | `userId` | Creates a filter. Note: you can only create a maximum of 1,000 filters. |
| `users_settings_filters_delete` | `DELETE` | `id, userId` | Immediately and permanently deletes the specified filter. |
