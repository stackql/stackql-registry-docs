---
title: logging_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - logging_configuration
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
Gets an individual <code>logging_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logging_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>logging_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ivschat.logging_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>LoggingConfiguration ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The system-generated ID of the logging configuration.</td></tr>
<tr><td><code>destination_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the logging configuration. The value does not need to be unique.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of the logging configuration. When the state is ACTIVE, the configuration is ready to log chat content.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>logging_configuration</code> resource, the following permissions are required:

### Read
<pre>
ivschat:GetLoggingConfiguration,
ivschat:ListTagsForResource</pre>

### Update
<pre>
ivschat:UpdateLoggingConfiguration,
ivschat:GetLoggingConfiguration,
ivschat:TagResource,
ivschat:UnTagResource,
ivschat:ListTagsForResource,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:ListLogDeliveries,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
s3:PutBucketPolicy,
s3:GetBucketPolicy,
iam:CreateServiceLinkedRole,
firehose:TagDeliveryStream</pre>

### Delete
<pre>
ivschat:DeleteLoggingConfiguration,
ivschat:GetLoggingConfiguration,
logs:DeleteLogDelivery,
logs:ListLogDeliveries,
ivschat:UntagResource,
logs:GetLogDelivery</pre>


## Example
```sql
SELECT
region,
arn,
id,
destination_configuration,
name,
state,
tags
FROM awscc.ivschat.logging_configuration
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
