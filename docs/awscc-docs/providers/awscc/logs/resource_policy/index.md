---
title: resource_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_policy
  - logs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>resource_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.logs.resource_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>policy_name</code></td><td><code>string</code></td><td>A name for resource policy</td></tr>
<tr><td><code>policy_document</code></td><td><code>string</code></td><td>The policy document</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>resource_policy</code> resource, the following permissions are required:

### Read
```json
logs:DescribeResourcePolicies
```

### Update
```json
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DeleteResourcePolicy
```

### Delete
```json
logs:DeleteResourcePolicy
```


## Example
```sql
SELECT
region,
policy_name,
policy_document
FROM awscc.logs.resource_policy
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;PolicyName&gt;'
```
