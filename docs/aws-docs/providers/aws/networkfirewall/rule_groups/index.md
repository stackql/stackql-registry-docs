---
title: rule_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_groups
  - networkfirewall
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

Creates, updates, deletes or gets a <code>rule_group</code> resource or lists <code>rule_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::NetworkFirewall::RuleGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkfirewall.rule_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="rule_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_group_arn" /></td><td><code>string</code></td><td>A resource ARN.</td></tr>
<tr><td><CopyableCode code="rule_group_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_group" /></td><td><code>object</code></td><td>Resource type definition for AWS::NetworkFirewall::RuleGroup</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="capacity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="Type, Capacity, RuleGroupName, region" /></td>
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
List all <code>rule_groups</code> in a region.
```sql
SELECT
region,
rule_group_arn
FROM aws.networkfirewall.rule_groups
WHERE region = 'us-east-1';
```
Gets all properties from a <code>rule_group</code>.
```sql
SELECT
region,
rule_group_name,
rule_group_arn,
rule_group_id,
rule_group,
type,
capacity,
description,
tags
FROM aws.networkfirewall.rule_groups
WHERE region = 'us-east-1' AND data__Identifier = '<RuleGroupArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>rule_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.networkfirewall.rule_groups (
 RuleGroupName,
 Type,
 Capacity,
 region
)
SELECT 
'{{ RuleGroupName }}',
 '{{ Type }}',
 '{{ Capacity }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.networkfirewall.rule_groups (
 RuleGroupName,
 RuleGroup,
 Type,
 Capacity,
 Description,
 Tags,
 region
)
SELECT 
 '{{ RuleGroupName }}',
 '{{ RuleGroup }}',
 '{{ Type }}',
 '{{ Capacity }}',
 '{{ Description }}',
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
  - name: rule_group
    props:
      - name: RuleGroupName
        value: '{{ RuleGroupName }}'
      - name: RuleGroup
        value:
          RuleGroupName: '{{ RuleGroupName }}'
          RuleGroup: null
          Type: '{{ Type }}'
          Capacity: '{{ Capacity }}'
          Description: '{{ Description }}'
          Tags:
            - Key: '{{ Key }}'
              Value: '{{ Value }}'
      - name: Type
        value: '{{ Type }}'
      - name: Capacity
        value: '{{ Capacity }}'
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value:
          - null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.networkfirewall.rule_groups
WHERE data__Identifier = '<RuleGroupArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>rule_groups</code> resource, the following permissions are required:

### Create
```json
network-firewall:CreateRuleGroup,
network-firewall:DescribeRuleGroup,
network-firewall:TagResource,
network-firewall:ListRuleGroups,
iam:CreateServiceLinkedRole,
ec2:GetManagedPrefixListEntries
```

### Read
```json
network-firewall:DescribeRuleGroup,
network-firewall:ListTagsForResources
```

### Update
```json
network-firewall:UpdateRuleGroup,
network-firewall:DescribeRuleGroup,
network-firewall:TagResource,
network-firewall:UntagResource,
iam:CreateServiceLinkedRole,
ec2:GetManagedPrefixListEntries
```

### Delete
```json
network-firewall:DeleteRuleGroup,
network-firewall:DescribeRuleGroup,
network-firewall:UntagResource
```

### List
```json
network-firewall:ListRuleGroups
```

