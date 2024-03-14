---
title: flywheel
hide_title: false
hide_table_of_contents: false
keywords:
  - flywheel
  - comprehend
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>flywheel</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flywheel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>flywheel</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.comprehend.flywheel</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>active_model_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>data_access_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>data_lake_s3_uri</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>data_security_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>flywheel_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>model_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>task_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
active_model_arn,
data_access_role_arn,
data_lake_s3_uri,
data_security_config,
flywheel_name,
model_type,
tags,
task_config,
arn
FROM awscc.comprehend.flywheel
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>flywheel</code> resource, the following permissions are required:

### Read
```json
comprehend:DescribeFlywheel,
comprehend:ListTagsForResource
```

### Update
```json
iam:PassRole,
comprehend:DescribeFlywheel,
comprehend:UpdateFlywheel,
comprehend:ListTagsForResource,
comprehend:TagResource,
comprehend:UntagResource
```

### Delete
```json
comprehend:DeleteFlywheel,
comprehend:DescribeFlywheel
```

