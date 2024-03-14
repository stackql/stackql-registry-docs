---
title: rotation
hide_title: false
hide_table_of_contents: false
keywords:
  - rotation
  - ssmcontacts
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>rotation</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rotation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>rotation</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ssmcontacts.rotation</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the Rotation</td></tr>
<tr><td><code>contact_ids</code></td><td><code>array</code></td><td>Members of the rotation</td></tr>
<tr><td><code>start_time</code></td><td><code>string</code></td><td>Start time of the first shift of Oncall Schedule</td></tr>
<tr><td><code>time_zone_id</code></td><td><code>string</code></td><td>TimeZone Identifier for the Oncall Schedule</td></tr>
<tr><td><code>recurrence</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the rotation.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
contact_ids,
start_time,
time_zone_id,
recurrence,
tags,
arn
FROM awscc.ssmcontacts.rotation
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>rotation</code> resource, the following permissions are required:

### Read
```json
ssm-contacts:GetRotation,
ssm-contacts:TagResource,
ssm-contacts:ListTagsForResource,
ssm-contacts:UntagResource
```

### Update
```json
ssm-contacts:UpdateRotation,
ssm-contacts:GetRotation,
ssm-contacts:TagResource,
ssm-contacts:ListTagsForResource,
ssm-contacts:UntagResource
```

### Delete
```json
ssm-contacts:DeleteRotation,
ssm-contacts:GetRotation,
ssm-contacts:ListTagsForResource,
ssm-contacts:UntagResource
```

