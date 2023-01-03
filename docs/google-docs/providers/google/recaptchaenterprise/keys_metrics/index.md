---
title: keys_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - keys_metrics
  - recaptchaenterprise
  - google    
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
<tr><td><b>Name</b></td><td><code>keys_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recaptchaenterprise.keys_metrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The name of the metrics, in the format "projects/{project}/keys/{key}/metrics". |
| `challengeMetrics` | `array` | Metrics will be continuous and in order by dates, and in the granularity of day. Only challenge-based keys (CHECKBOX, INVISIBLE), will have challenge-based data. |
| `scoreMetrics` | `array` | Metrics will be continuous and in order by dates, and in the granularity of day. All Key types should have score-based data. |
| `startTime` | `string` | Inclusive start time aligned to a day (UTC). |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_keys_getMetrics` | `SELECT` | `keysId, projectsId` |
