---
title: outcomes
hide_title: false
hide_table_of_contents: false
keywords:
  - outcomes
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
Retrieves a list of <code>outcomes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>outcomes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>outcomes</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.frauddetector.outcomes</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The outcome ARN.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>outcomes</code> resource, the following permissions are required:

### Create
```json
frauddetector:GetOutcomes,
frauddetector:PutOutcome,
frauddetector:ListTagsForResource,
frauddetector:TagResource
```

### List
```json
frauddetector:GetOutcomes,
frauddetector:ListTagsForResource
```


## Example
```sql
SELECT
region,
arn
FROM awscc.frauddetector.outcomes
WHERE region = 'us-east-1'
```
