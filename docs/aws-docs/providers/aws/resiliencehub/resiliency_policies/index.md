---
title: resiliency_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - resiliency_policies
  - resiliencehub
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


Used to retrieve a list of <code>resiliency_policies</code> in a region or to create or delete a <code>resiliency_policies</code> resource, use <code>resiliency_policy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resiliency_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for Resiliency Policy.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.resiliencehub.resiliency_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="policy_arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the Resiliency Policy.</td></tr>
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
policy_arn
FROM aws.resiliencehub.resiliency_policies
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>resiliency_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- resiliency_policy.iql (required properties only)
INSERT INTO aws.resiliencehub.resiliency_policies (
 PolicyName,
 Tier,
 Policy,
 region
)
SELECT 
'{{ PolicyName }}',
 '{{ Tier }}',
 '{{ Policy }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- resiliency_policy.iql (all properties)
INSERT INTO aws.resiliencehub.resiliency_policies (
 PolicyName,
 PolicyDescription,
 DataLocationConstraint,
 Tier,
 Policy,
 Tags,
 region
)
SELECT 
 '{{ PolicyName }}',
 '{{ PolicyDescription }}',
 '{{ DataLocationConstraint }}',
 '{{ Tier }}',
 '{{ Policy }}',
 '{{ Tags }}',
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
  - name: resiliency_policy
    props:
      - name: PolicyName
        value: '{{ PolicyName }}'
      - name: PolicyDescription
        value: '{{ PolicyDescription }}'
      - name: DataLocationConstraint
        value: '{{ DataLocationConstraint }}'
      - name: Tier
        value: '{{ Tier }}'
      - name: Policy
        value:
          AZ:
            RtoInSecs: '{{ RtoInSecs }}'
            RpoInSecs: '{{ RpoInSecs }}'
          Hardware: null
          Software: null
          Region: null
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.resiliencehub.resiliency_policies
WHERE data__Identifier = '<PolicyArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resiliency_policies</code> resource, the following permissions are required:

### Create
```json
resiliencehub:CreateResiliencyPolicy,
resiliencehub:DescribeResiliencyPolicy,
resiliencehub:TagResource
```

### Delete
```json
resiliencehub:DeleteResiliencyPolicy,
resiliencehub:UntagResource
```

### List
```json
resiliencehub:ListResiliencyPolicies
```

