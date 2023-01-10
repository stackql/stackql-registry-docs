---
title: super_chat_events
hide_title: false
hide_table_of_contents: false
keywords:
  - super_chat_events
  - youtube
  - youtube    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/youtube/stackql-youtube-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>super_chat_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtube.super_chat_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID that YouTube assigns to uniquely identify the Super Chat event. |
| `snippet` | `object` |  |
| `etag` | `string` | Etag of this resource. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string `"youtube#superChatEvent"`. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `superChatEvents_list` | `SELECT` | `part` |
