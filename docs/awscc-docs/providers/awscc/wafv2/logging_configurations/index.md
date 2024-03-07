---
title: logging_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - logging_configurations
  - wafv2
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
<tr><td><b>Id</b></td><td><code>awscc.wafv2.logging_configurations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>resource_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the web ACL that you want to associate with LogDestinationConfigs.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>logging_configurations</code> resource, the following permissions are required:

### Create
<pre>
wafv2:PutLoggingConfiguration,
wafv2:GetLoggingConfiguration,
firehose:ListDeliveryStreams,
iam:CreateServiceLinkedRole,
iam:DescribeOrganization,
logs:CreateLogDelivery,
s3:PutBucketPolicy,
s3:GetBucketPolicy,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups</pre>

### List
<pre>
wafv2:ListLoggingConfigurations</pre>


## Example
```sql
SELECT
region,
resource_arn
FROM awscc.wafv2.logging_configurations

```
