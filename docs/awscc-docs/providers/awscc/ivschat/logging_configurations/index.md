---
title: logging_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - logging_configurations
  - ivschat
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>logging_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logging_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>logging_configurations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ivschat.logging_configurations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>LoggingConfiguration ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>logging_configurations</code> resource, the following permissions are required:

### Create
<pre>
ivschat:CreateLoggingConfiguration,
ivschat:GetLoggingConfiguration,
logs:CreateLogDelivery,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
s3:PutBucketPolicy,
s3:GetBucketPolicy,
iam:CreateServiceLinkedRole,
firehose:TagDeliveryStream,
ivschat:TagResource</pre>

### List
<pre>
ivschat:ListLoggingConfigurations,
ivschat:ListTagsForResource</pre>


## Example
```sql
SELECT
region,
arn
FROM awscc.ivschat.logging_configurations
WHERE region = 'us-east-1'
```
