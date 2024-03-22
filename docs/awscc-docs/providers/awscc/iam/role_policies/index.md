---
title: role_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - role_policies
  - iam
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
List of policies by RoleName (requires `aws` provider to be installed)

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>List of policies by RoleName (requires `aws` provider to be installed)</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iam.role_policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>role_name</code></td><td><code>string</code></td><td>The IAM role name</td></tr>
<tr><td><code>policy_name</code></td><td><code>string</code></td><td>The role policy name</td></tr>
<tr><td><code>policy_document</code></td><td><code>string</code></td><td>The role policy document</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
role_name,
policy_name,
policy_document,
region
FROM awscc.iam.role_policies
WHERE RoleName = '<RoleName>';
```




