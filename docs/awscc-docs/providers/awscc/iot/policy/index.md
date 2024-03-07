---
title: policy
hide_title: false
hide_table_of_contents: false
keywords:
  - policy
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iot.policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy_document</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>policy_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>policy</code> resource, the following permissions are required:

### Read
<pre>
iot:GetPolicy,
iot:ListTagsForResource</pre>

### Delete
<pre>
iot:DeletePolicy,
iot:GetPolicy,
iot:ListPolicyVersions,
iot:DeletePolicyVersion</pre>

### Update
<pre>
iot:GetPolicy,
iot:ListPolicyVersions,
iot:CreatePolicyVersion,
iot:DeletePolicyVersion,
iot:SetDefaultPolicyVersion,
iot:TagResource,
iot:UntagResource,
iot:ListTagsForResource</pre>


## Example
```sql
SELECT
region,
id,
arn,
policy_document,
policy_name,
tags
FROM awscc.iot.policy
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
