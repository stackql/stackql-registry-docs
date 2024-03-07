---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
  - lambda
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>versions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lambda.versions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>function_arn</code></td><td><code>string</code></td><td>The ARN of the version.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>versions</code> resource, the following permissions are required:

### Create
```json
lambda:PublishVersion,
lambda:GetFunctionConfiguration,
lambda:PutProvisionedConcurrencyConfig,
lambda:GetProvisionedConcurrencyConfig,
lambda:PutRuntimeManagementConfig,
lambda:GetRuntimeManagementConfig
```

### List
```json
lambda:ListVersionsByFunction
```


## Example
```sql
SELECT
region,
function_arn
FROM awscc.lambda.versions
WHERE region = 'us-east-1'
```
