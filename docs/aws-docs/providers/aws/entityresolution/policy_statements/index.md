---
title: policy_statements
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_statements
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>policy_statements</code> in a region or to create or delete a <code>policy_statements</code> resource, use <code>policy_statement</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy_statements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Policy Statement defined in AWS Entity Resolution Service</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.entityresolution.policy_statements" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="statement_id" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
statement_id
FROM aws.entityresolution.policy_statements
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Arn": "{{ Arn }}",
 "StatementId": "{{ StatementId }}"
}
>>>
--required properties only
INSERT INTO aws.entityresolution.policy_statements (
 Arn,
 StatementId,
 region
)
SELECT 
{{ Arn }},
 {{ StatementId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Arn": "{{ Arn }}",
 "StatementId": "{{ StatementId }}",
 "Effect": "{{ Effect }}",
 "Action": [
  "{{ Action[0] }}"
 ],
 "Principal": [
  "{{ Principal[0] }}"
 ],
 "Condition": "{{ Condition }}"
}
>>>
--all properties
INSERT INTO aws.entityresolution.policy_statements (
 Arn,
 StatementId,
 Effect,
 Action,
 Principal,
 Condition,
 region
)
SELECT 
 {{ Arn }},
 {{ StatementId }},
 {{ Effect }},
 {{ Action }},
 {{ Principal }},
 {{ Condition }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.entityresolution.policy_statements
WHERE data__Identifier = '<Arn|StatementId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>policy_statements</code> resource, the following permissions are required:

### Create
```json
entityresolution:AddPolicyStatement
```

### Delete
```json
entityresolution:DeletePolicyStatement,
entityresolution:GetPolicy
```

### List
```json
entityresolution:GetPolicy
```

