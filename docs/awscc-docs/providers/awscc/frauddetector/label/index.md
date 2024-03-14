---
title: label
hide_title: false
hide_table_of_contents: false
keywords:
  - label
  - frauddetector
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>label</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>label</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>label</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.frauddetector.label</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the label.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Tags associated with this label.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The label description.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The label ARN.</td></tr>
<tr><td><code>created_time</code></td><td><code>string</code></td><td>The timestamp when the label was created.</td></tr>
<tr><td><code>last_updated_time</code></td><td><code>string</code></td><td>The timestamp when the label was last updated.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
tags,
description,
arn,
created_time,
last_updated_time
FROM awscc.frauddetector.label
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>label</code> resource, the following permissions are required:

### Read
```json
frauddetector:GetLabels,
frauddetector:ListTagsForResource
```

### Update
```json
frauddetector:GetLabels,
frauddetector:PutLabel,
frauddetector:ListTagsForResource,
frauddetector:TagResource,
frauddetector:UntagResource
```

### Delete
```json
frauddetector:GetLabels,
frauddetector:DeleteLabel
```

