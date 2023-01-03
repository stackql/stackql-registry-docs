---
title: health_events
hide_title: false
hide_table_of_contents: false
keywords:
  - health_events
  - health_events
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>health_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.health_events.health_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `resourceIdentity` | `object` |  |
| `severityLevel` | `string` | The criticality of the event. It is either `Error` or `Warning` |
| `subsystem` | `string` | The product area of the event. |
| `details` | `object` |  |
| `eventId` | `string` | The unique identifier of the event. |
| `eventName` | `string` | The name of the event. |
| `eventTime` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `listAllHealthEvents` | `SELECT` |  |
