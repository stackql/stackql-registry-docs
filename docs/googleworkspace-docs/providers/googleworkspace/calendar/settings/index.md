---
title: settings
hide_title: false
hide_table_of_contents: false
keywords:
  - settings
  - calendar
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
<tr><td><b>Name</b></td><td><code>settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.calendar.settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The id of the user setting. |
| `etag` | `string` | ETag of the resource. |
| `kind` | `string` | Type of the resource ("calendar#setting"). |
| `value` | `string` | Value of the user setting. The format of the value depends on the ID of the setting. It must always be a UTF-8 string of length up to 1024 characters. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `setting` | Returns a single user setting. |
| `list` | `SELECT` |  | Returns all user settings for the authenticated user. |
| `watch` | `EXEC` |  | Watch for changes to Settings resources. |
