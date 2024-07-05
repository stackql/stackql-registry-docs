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

Creates, updates, deletes or gets a <code>rule_groups_namespace</code> resource or lists <code>rule_groups_namespaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_groups_namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>RuleGroupsNamespace schema for cloudformation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.aps.rule_groups_namespaces" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="workspace" /></td><td><code>string</code></td><td>Required to identify a specific APS Workspace associated with this RuleGroupsNamespace.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The RuleGroupsNamespace name.</td></tr>
<tr><td><CopyableCode code="data" /></td><td><code>string</code></td><td>The RuleGroupsNamespace data.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The RuleGroupsNamespace ARN.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>rule_groups_namespaces</code> in a region.
```sql
SELECT
region,
workspace,
name,
data,
arn,
tags
FROM aws.aps.rule_groups_namespaces
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>rule_groups_namespace</code>.
```sql
SELECT
region,
workspace,
name,
data,
arn,
tags
FROM aws.aps.rule_groups_namespaces
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

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

## `DELETE` example

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

### Read
```json
aps:DescribeRuleGroupsNamespace,
aps:ListTagsForResource
```

### Update
```json
aps:PutRuleGroupsNamespace,
aps:DescribeRuleGroupsNamespace,
aps:TagResource,
aps:UntagResource,
aps:ListTagsForResource
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

