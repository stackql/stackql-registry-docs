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

Creates, updates, deletes or gets a <code>protection_group</code> resource or lists <code>protection_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>protection_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A grouping of protected resources so they can be handled as a collective. This resource grouping improves the accuracy of detection and reduces false positives.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.shield.protection_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="protection_group_id" /></td><td><code>string</code></td><td>The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it.</td></tr>
<tr><td><CopyableCode code="protection_group_arn" /></td><td><code>string</code></td><td>The ARN (Amazon Resource Name) of the protection group.</td></tr>
<tr><td><CopyableCode code="aggregation" /></td><td><code>string</code></td><td>Defines how AWS Shield combines resource data for the group in order to detect, mitigate, and report events.<br/>* Sum - Use the total traffic across the group. This is a good choice for most cases. Examples include Elastic IP addresses for EC2 instances that scale manually or automatically.<br/>* Mean - Use the average of the traffic across the group. This is a good choice for resources that share traffic uniformly. Examples include accelerators and load balancers.<br/>* Max - Use the highest traffic from each resource. This is useful for resources that don't share traffic and for resources that share that traffic in a non-uniform way. Examples include Amazon CloudFront and origin resources for CloudFront distributions.</td></tr>
<tr><td><CopyableCode code="pattern" /></td><td><code>string</code></td><td>The criteria to use to choose the protected resources for inclusion in the group. You can include all resources that have protections, provide a list of resource Amazon Resource Names (ARNs), or include all resources of a specified resource type.</td></tr>
<tr><td><CopyableCode code="members" /></td><td><code>array</code></td><td>The Amazon Resource Names (ARNs) of the resources to include in the protection group. You must set this when you set `Pattern` to `ARBITRARY` and you must not set it for any other `Pattern` setting.</td></tr>
<tr><td><CopyableCode code="resource_type" /></td><td><code>string</code></td><td>The resource type to include in the protection group. All protected resources of this type are included in the protection group. Newly protected resources of this type are automatically added to the group. You must set this when you set `Pattern` to `BY_RESOURCE_TYPE` and you must not set it for any other `Pattern` setting.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tag key-value pairs for the Protection object.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>protection_groups</code> in a region.
```sql
SELECT
region,
protection_group_arn
FROM aws.shield.protection_groups
;
```
Gets all properties from a <code>protection_group</code>.
```sql
SELECT
region,
protection_group_id,
protection_group_arn,
aggregation,
pattern,
members,
resource_type,
tags
FROM aws.shield.protection_groups
WHERE data__Identifier = '<ProtectionGroupArn>';
```


## `INSERT` example

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

## `DELETE` example

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

### Read
```json
shield:DescribeProtectionGroup,
shield:ListTagsForResource
```

### Update
```json
shield:UpdateProtectionGroup,
shield:ListTagsForResource,
shield:TagResource,
shield:UntagResource
```

### List
```json
shield:ListProtectionGroups
```

