---
title: resource_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_policy
  - ssm
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
<tr><td><b>Id</b></td><td><code>aws.ssm.resource_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>resource_arn</code></td><td><code>string</code></td><td>Arn of OpsItemGroup etc.</td></tr>
<tr><td><code>policy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy_id</code></td><td><code>string</code></td><td>An unique identifier within the policies of a resource. </td></tr>
<tr><td><code>policy_hash</code></td><td><code>string</code></td><td>A snapshot identifier for the policy over time.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
resource_arn,
policy,
policy_id,
policy_hash
FROM aws.ssm.resource_policy
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;PolicyId&gt;'
AND data__Identifier = '&lt;ResourceArn&gt;'
```
