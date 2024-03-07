---
title: lifecycle_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_policies
  - opensearchserverless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>lifecycle_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lifecycle_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>lifecycle_policies</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.opensearchserverless.lifecycle_policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>type</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the policy</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>lifecycle_policies</code> resource, the following permissions are required:

### Create
<pre>
aoss:CreateLifecyclePolicy</pre>

### List
<pre>
aoss:ListLifecyclePolicies</pre>


## Example
```sql
SELECT
region,
type,
name
FROM awscc.opensearchserverless.lifecycle_policies
WHERE region = 'us-east-1'
```
