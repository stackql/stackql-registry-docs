---
title: fleet
hide_title: false
hide_table_of_contents: false
keywords:
  - fleet
  - codebuild
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>fleet</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleet</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>fleet</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.codebuild.fleet</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>base_capacity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>environment_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>compute_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>fleet</code> resource, the following permissions are required:

### Delete
```json
codebuild:BatchGetFleets,
codebuild:DeleteFleet
```

### Read
```json
codebuild:BatchGetFleets
```

### Update
```json
codebuild:BatchGetFleets,
codebuild:UpdateFleet
```


## Example
```sql
SELECT
region,
name,
base_capacity,
environment_type,
compute_type,
tags,
arn
FROM awscc.codebuild.fleet
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
