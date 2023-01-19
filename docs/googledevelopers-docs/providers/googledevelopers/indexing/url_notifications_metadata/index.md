---
title: url_notifications_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - url_notifications_metadata
  - indexing
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
<tr><td><b>Name</b></td><td><code>url_notifications_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.indexing.url_notifications_metadata</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `latestUpdate` | `object` | `UrlNotification` is the resource used in all Indexing API calls. It describes one event in the life cycle of a Web Document. |
| `url` | `string` | URL to which this metadata refers. |
| `latestRemove` | `object` | `UrlNotification` is the resource used in all Indexing API calls. It describes one event in the life cycle of a Web Document. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `urlNotifications_getMetadata` | `SELECT` |  |
