---
title: user_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - user_policies
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
List of user policies by UserName (requires `aws` provider to be installed)

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>List of user policies by UserName (requires `aws` provider to be installed)</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.user_policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>user_name</code></td><td><code>string</code></td><td>The IAM user name</td></tr>
<tr><td><code>member</code></td><td><code>string</code></td><td>The user policy name</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>view</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
user_name,
member,
region
FROM aws.iam.user_policies
WHERE UserName = '<UserName>';
```




