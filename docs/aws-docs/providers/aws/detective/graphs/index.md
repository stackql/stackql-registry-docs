---
title: graphs
hide_title: false
hide_table_of_contents: false
keywords:
  - graphs
  - detective
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

Creates, updates, deletes or gets a <code>graph</code> resource or lists <code>graphs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>graphs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Detective::Graph</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.detective.graphs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Detective graph ARN</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="auto_enable_members" /></td><td><code>boolean</code></td><td>Indicates whether to automatically enable new organization accounts as member accounts in the organization behavior graph.</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>graphs</code> in a region.
```sql
SELECT
region,
arn,
tags,
auto_enable_members
FROM aws.detective.graphs
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>graph</code>.
```sql
SELECT
region,
arn,
tags,
auto_enable_members
FROM aws.detective.graphs
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>graph</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.detective.graphs (
 Tags,
 AutoEnableMembers,
 region
)
SELECT 
'{{ Tags }}',
 '{{ AutoEnableMembers }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.detective.graphs (
 Tags,
 AutoEnableMembers,
 region
)
SELECT 
 '{{ Tags }}',
 '{{ AutoEnableMembers }}',
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
  - name: graph
    props:
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: AutoEnableMembers
        value: '{{ AutoEnableMembers }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.detective.graphs
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>graphs</code> resource, the following permissions are required:

### Create
```json
detective:CreateGraph,
detective:UpdateOrganizationConfiguration,
organizations:DescribeOrganization
```

### Update
```json
detective:UntagResource,
detective:TagResource,
detective:ListTagsForResource,
detective:UpdateOrganizationConfiguration,
organizations:DescribeOrganization
```

### Read
```json
detective:ListGraphs,
detective:ListTagsForResource,
detective:DescribeOrganizationConfiguration,
organizations:DescribeOrganization
```

### Delete
```json
detective:DeleteGraph
```

### List
```json
detective:ListGraphs,
detective:ListTagsForResource,
detective:DescribeOrganizationConfiguration,
organizations:DescribeOrganization
```

