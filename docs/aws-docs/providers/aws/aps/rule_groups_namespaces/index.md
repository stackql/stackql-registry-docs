---
title: rule_groups_namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_groups_namespaces
  - aps
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


Used to retrieve a list of <code>rule_groups_namespaces</code> in a region or to create or delete a <code>rule_groups_namespaces</code> resource, use <code>rule_groups_namespace</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_groups_namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>RuleGroupsNamespace schema for cloudformation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.aps.rule_groups_namespaces" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The RuleGroupsNamespace ARN.</td></tr>
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
    <td><CopyableCode code="Workspace, Data, Name, region" /></td>
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
arn
FROM aws.aps.rule_groups_namespaces
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>rule_groups_namespace</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.aps.rule_groups_namespaces (
 Workspace,
 Name,
 Data,
 region
)
SELECT 
'{{ Workspace }}',
 '{{ Name }}',
 '{{ Data }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.aps.rule_groups_namespaces (
 Workspace,
 Name,
 Data,
 Tags,
 region
)
SELECT 
 '{{ Workspace }}',
 '{{ Name }}',
 '{{ Data }}',
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
  - name: rule_groups_namespace
    props:
      - name: Workspace
        value: '{{ Workspace }}'
      - name: Name
        value: '{{ Name }}'
      - name: Data
        value: '{{ Data }}'
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
DELETE FROM aws.aps.rule_groups_namespaces
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>rule_groups_namespaces</code> resource, the following permissions are required:

### Create
```json
aps:CreateRuleGroupsNamespace,
aps:DescribeRuleGroupsNamespace,
aps:TagResource
```

### Delete
```json
aps:DeleteRuleGroupsNamespace,
aps:DescribeRuleGroupsNamespace
```

### List
```json
aps:ListRuleGroupsNamespaces,
aps:ListTagsForResource
```

