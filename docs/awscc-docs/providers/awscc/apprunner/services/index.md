---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - apprunner
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>services</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>services</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apprunner.services</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>service_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the AppRunner Service.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>services</code> resource, the following permissions are required:

### Create
<pre>
apprunner:CreateService,
apprunner:TagResource,
iam:PassRole,
iam:CreateServiceLinkedRole,
logs:CreateLogGroup,
logs:PutRetentionPolicy,
logs:CreateLogStream,
logs:PutLogEvents,
logs:DescribeLogStreams,
events:PutRule,
events:PutTargets</pre>

### List
<pre>
apprunner:ListServices,
iam:PassRole</pre>


## Example
```sql
SELECT
region,
service_arn
FROM awscc.apprunner.services
WHERE region = 'us-east-1'
```
