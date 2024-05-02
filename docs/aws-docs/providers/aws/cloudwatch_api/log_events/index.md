---
title: log_events
hide_title: false
hide_table_of_contents: false
keywords:
  - log_events
  - cloudwatch_api
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudwatch_api.log_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `ingestionTime` | `number` | The time the event was ingested, expressed as the number of milliseconds after &lt;code&gt;Jan 1, 1970 00:00:00 UTC&lt;/code&gt;. |
| `message` | `string` | The data contained in the log event. |
| `timestamp` | `number` | The time the event occurred, expressed as the number of milliseconds after &lt;code&gt;Jan 1, 1970 00:00:00 UTC&lt;/code&gt;. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `GetLogEvents` | `SELECT` | `data__logStreamName, region` |
