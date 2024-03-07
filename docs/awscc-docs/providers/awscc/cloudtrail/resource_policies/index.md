---
title: resource_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_policies
  - cloudtrail
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>resource_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource_policies</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudtrail.resource_policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>resource_arn</code></td><td><code>string</code></td><td>The ARN of the AWS CloudTrail resource to which the policy applies.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>resource_policies</code> resource, the following permissions are required:

### Create
```json
CloudTrail:PutResourcePolicy,
CloudTrail:GetResourcePolicy
```


## Example
```sql
SELECT
region,
resource_arn
FROM awscc.cloudtrail.resource_policies
WHERE region = 'us-east-1'
```
