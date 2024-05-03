---
title: policy_statement
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_statement
  - entityresolution
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

Gets or operates on an individual <code>policy_statement</code> resource, use <code>policy_statements</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy_statement</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Policy Statement defined in AWS Entity Resolution Service</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.entityresolution.policy_statement" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="statement_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="effect" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="action" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="principal" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="condition" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
statement_id,
effect,
action,
principal,
condition
FROM aws.entityresolution.policy_statement
WHERE data__Identifier = '<Arn>|<StatementId>';
```

## Permissions

To operate on the <code>policy_statement</code> resource, the following permissions are required:

### Read
```json
entityresolution:GetPolicy
```

### Update
```json
entityresolution:AddPolicyStatement,
entityresolution:DeletePolicyStatement
```

### Delete
```json
entityresolution:DeletePolicyStatement,
entityresolution:GetPolicy
```

