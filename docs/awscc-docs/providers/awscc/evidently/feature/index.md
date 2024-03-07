---
title: feature
hide_title: false
hide_table_of_contents: false
keywords:
  - feature
  - evidently
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>feature</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feature</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>feature</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.evidently.feature</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>project</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>evaluation_strategy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>variations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>default_variation</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>entity_overrides</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
project,
name,
description,
evaluation_strategy,
variations,
default_variation,
entity_overrides,
tags
FROM awscc.evidently.feature
WHERE region = 'us-east-1'
AND data__Identifier = '{Arn}';
```

## Permissions

To operate on the <code>feature</code> resource, the following permissions are required:

### Read
```json
evidently:GetFeature,
evidently:ListTagsForResource
```

### Update
```json
evidently:UpdateFeature,
evidently:ListTagsForResource,
evidently:TagResource,
evidently:UntagResource,
evidently:GetFeature
```

### Delete
```json
evidently:DeleteFeature,
evidently:UntagResource,
evidently:GetFeature
```

