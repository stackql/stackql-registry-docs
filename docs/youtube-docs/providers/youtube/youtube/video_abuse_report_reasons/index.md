---
title: video_abuse_report_reasons
hide_title: false
hide_table_of_contents: false
keywords:
  - video_abuse_report_reasons
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
<tr><td><b>Name</b></td><td><code>video_abuse_report_reasons</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtube.video_abuse_report_reasons</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of this abuse report reason. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string `"youtube#videoAbuseReportReason"`. |
| `snippet` | `object` | Basic details about a video category, such as its localized title. |
| `etag` | `string` | Etag of this resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `videoAbuseReportReasons_list` | `SELECT` | `part` |
