---
title: protection_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - protection_groups
  - shield
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


Used to retrieve a list of <code>protection_groups</code> in a region or to create or delete a <code>protection_groups</code> resource, use <code>protection_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>protection_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A grouping of protected resources so they can be handled as a collective. This resource grouping improves the accuracy of detection and reduces false positives.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.shield.protection_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="protection_group_arn" /></td><td><code>string</code></td><td>The ARN (Amazon Resource Name) of the protection group.</td></tr>
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
    <td><CopyableCode code="Aggregation, Pattern, ProtectionGroupId, region" /></td>
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
protection_group_arn
FROM aws.shield.protection_groups
;
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>protection_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
INSERT INTO aws.shield.protection_groups (
 ProtectionGroupId,
 Aggregation,
 Pattern,
 region
)
SELECT 
'{{ ProtectionGroupId }}',
 '{{ Aggregation }}',
 '{{ Pattern }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.shield.protection_groups (
 ProtectionGroupId,
 Aggregation,
 Pattern,
 Members,
 ResourceType,
 Tags,
 region
)
SELECT 
 '{{ ProtectionGroupId }}',
 '{{ Aggregation }}',
 '{{ Pattern }}',
 '{{ Members }}',
 '{{ ResourceType }}',
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
  - name: protection_group
    props:
      - name: ProtectionGroupId
        value: '{{ ProtectionGroupId }}'
      - name: Aggregation
        value: '{{ Aggregation }}'
      - name: Pattern
        value: '{{ Pattern }}'
      - name: Members
        value:
          - '{{ Members[0] }}'
      - name: ResourceType
        value: '{{ ResourceType }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.shield.protection_groups
WHERE data__Identifier = '<ProtectionGroupArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>protection_groups</code> resource, the following permissions are required:

### Create
```json
shield:CreateProtectionGroup,
shield:TagResource
```

### Delete
```json
shield:DeleteProtectionGroup,
shield:UntagResource
```

### List
```json
shield:ListProtectionGroups
```

