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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

List of policies by RoleName (requires `aws` provider to be installed)

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>List of policies by RoleName (requires `aws` provider to be installed)</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.role_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="role_name" /></td><td><code>string</code></td><td>The IAM role name</td></tr>
<tr><td><CopyableCode code="policy_name" /></td><td><code>string</code></td><td>The role policy name</td></tr>
<tr><td><CopyableCode code="policy_document" /></td><td><code>string</code></td><td>The role policy document</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="view" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
role_name,
policy_name,
policy_document,
region
FROM aws.iam.role_policies
WHERE RoleName = '<RoleName>';
```




