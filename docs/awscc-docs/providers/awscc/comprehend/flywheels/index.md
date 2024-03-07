---
title: flywheels
hide_title: false
hide_table_of_contents: false
keywords:
  - flywheels
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
Retrieves a list of <code>flywheels</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flywheels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>flywheels</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.comprehend.flywheels</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>flywheels</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
comprehend:CreateFlywheel,
comprehend:DescribeFlywheel,
comprehend:ListTagsForResource
```

### List
```json
comprehend:ListFlywheels
```


## Example
```sql
SELECT
region,
arn
FROM awscc.comprehend.flywheels
WHERE region = 'us-east-1'
```
