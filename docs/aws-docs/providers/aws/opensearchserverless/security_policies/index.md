---
title: security_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - security_policies
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>security_policies</code> in a region or to create or delete a <code>security_policies</code> resource, use <code>security_policy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Amazon OpenSearchServerless security policy resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.opensearchserverless.security_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="type" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the policy</td></tr>
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
type,
name
FROM aws.opensearchserverless.security_policies
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>security_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
-- security_policy.iql (required properties only)
INSERT INTO aws.opensearchserverless.security_policies (
 Policy,
 Name,
 Type,
 region
)
SELECT 
'{{ Policy }}',
 '{{ Name }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- security_policy.iql (all properties)
INSERT INTO aws.opensearchserverless.security_policies (
 Description,
 Policy,
 Name,
 Type,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Policy }}',
 '{{ Name }}',
 '{{ Type }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: security_policy
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Policy
        value: '{{ Policy }}'
      - name: Name
        value: '{{ Name }}'
      - name: Type
        value: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.opensearchserverless.security_policies
WHERE data__Identifier = '<Type|Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>security_policies</code> resource, the following permissions are required:

### Create
```json
aoss:GetSecurityPolicy,
aoss:CreateSecurityPolicy,
kms:DescribeKey,
kms:CreateGrant
```

### Delete
```json
aoss:GetSecurityPolicy,
aoss:DeleteSecurityPolicy
```

### List
```json
aoss:ListSecurityPolicies
```

