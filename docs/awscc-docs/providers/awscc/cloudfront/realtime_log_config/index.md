---
title: realtime_log_config
hide_title: false
hide_table_of_contents: false
keywords:
  - realtime_log_config
  - cloudfront
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>realtime_log_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>realtime_log_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>realtime_log_config</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudfront.realtime_log_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>end_points</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>fields</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sampling_rate</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
end_points,
fields,
name,
sampling_rate
FROM awscc.cloudfront.realtime_log_config
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>realtime_log_config</code> resource, the following permissions are required:

### Delete
```json
cloudfront:DeleteRealtimeLogConfig,
cloudfront:GetRealtimeLogConfig
```

### Read
```json
cloudfront:GetRealtimeLogConfig
```

### Update
```json
cloudfront:UpdateRealtimeLogConfig,
cloudfront:GetRealtimeLogConfig,
iam:PassRole
```

