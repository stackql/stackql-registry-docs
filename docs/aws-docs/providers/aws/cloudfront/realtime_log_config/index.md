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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>realtime_log_config</code> resource, use <code>realtime_log_configs</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>realtime_log_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CloudFront::RealtimeLogConfig</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.realtime_log_config" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="end_points" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="fields" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sampling_rate" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
end_points,
fields,
name,
sampling_rate
FROM aws.cloudfront.realtime_log_config
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

