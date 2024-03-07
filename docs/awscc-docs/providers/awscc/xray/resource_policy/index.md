---
title: resource_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_policy
  - xray
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
<tr><td><b>Id</b></td><td><code>awscc.xray.resource_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>policy_name</code></td><td><code>string</code></td><td>The name of the resource policy. Must be unique within a specific AWS account.</td></tr>
<tr><td><code>policy_document</code></td><td><code>string</code></td><td>The resource policy document, which can be up to 5kb in size.</td></tr>
<tr><td><code>bypass_policy_lockout_check</code></td><td><code>boolean</code></td><td>A flag to indicate whether to bypass the resource policy lockout safety check</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>resource_policy</code> resource, the following permissions are required:

### Read
```json
xray:ListResourcePolicies
```

### Update
```json
xray:PutResourcePolicy,
xray:ListResourcePolicies
```

### Delete
```json
xray:DeleteResourcePolicy
```


## Example
```sql
SELECT
region,
policy_name,
policy_document,
bypass_policy_lockout_check
FROM awscc.xray.resource_policy
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;PolicyName&gt;'
```
