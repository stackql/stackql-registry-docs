---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - xray
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

Creates, updates, deletes or gets a <code>group</code> resource or lists <code>groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This schema provides construct and validation rules for AWS-XRay Group resource parameters.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.xray.groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="filter_expression" /></td><td><code>string</code></td><td>The filter expression defining criteria by which to group traces.</td></tr>
<tr><td><CopyableCode code="group_name" /></td><td><code>string</code></td><td>The case-sensitive name of the new group. Names must be unique.</td></tr>
<tr><td><CopyableCode code="group_arn" /></td><td><code>string</code></td><td>The ARN of the group that was generated on creation.</td></tr>
<tr><td><CopyableCode code="insights_configuration" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="GroupName, region" /></td>
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
List all <code>groups</code> in a region.
```sql
SELECT
region,
group_arn
FROM aws.xray.groups
WHERE region = 'us-east-1';
```
Gets all properties from a <code>group</code>.
```sql
SELECT
region,
filter_expression,
group_name,
group_arn,
insights_configuration,
tags
FROM aws.xray.groups
WHERE region = 'us-east-1' AND data__Identifier = '<GroupARN>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.xray.groups (
 GroupName,
 region
)
SELECT 
'{{ GroupName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.xray.groups (
 FilterExpression,
 GroupName,
 InsightsConfiguration,
 Tags,
 region
)
SELECT 
 '{{ FilterExpression }}',
 '{{ GroupName }}',
 '{{ InsightsConfiguration }}',
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
  - name: group
    props:
      - name: FilterExpression
        value: '{{ FilterExpression }}'
      - name: GroupName
        value: '{{ GroupName }}'
      - name: InsightsConfiguration
        value:
          InsightsEnabled: '{{ InsightsEnabled }}'
          NotificationsEnabled: '{{ NotificationsEnabled }}'
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
DELETE FROM aws.xray.groups
WHERE data__Identifier = '<GroupARN>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>groups</code> resource, the following permissions are required:

### Create
```json
xray:CreateGroup,
xray:TagResource
```

### Read
```json
xray:GetGroup,
xray:ListTagsForResource
```

### Update
```json
xray:UpdateGroup,
xray:TagResource,
xray:UntagResource,
xray:ListTagsForResource
```

### Delete
```json
xray:DeleteGroup
```

### List
```json
xray:GetGroups,
xray:ListTagsForResource
```

