---
title: thing_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - thing_groups
  - iot
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


Used to retrieve a list of <code>thing_groups</code> in a region or to create or delete a <code>thing_groups</code> resource, use <code>thing_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>thing_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IoT::ThingGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.thing_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="thing_group_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
thing_group_name
FROM aws.iot.thing_groups
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>thing_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iot.thing_groups (
 ThingGroupName,
 ParentGroupName,
 QueryString,
 ThingGroupProperties,
 Tags,
 region
)
SELECT 
'{{ ThingGroupName }}',
 '{{ ParentGroupName }}',
 '{{ QueryString }}',
 '{{ ThingGroupProperties }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iot.thing_groups (
 ThingGroupName,
 ParentGroupName,
 QueryString,
 ThingGroupProperties,
 Tags,
 region
)
SELECT 
 '{{ ThingGroupName }}',
 '{{ ParentGroupName }}',
 '{{ QueryString }}',
 '{{ ThingGroupProperties }}',
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
  - name: thing_group
    props:
      - name: ThingGroupName
        value: '{{ ThingGroupName }}'
      - name: ParentGroupName
        value: '{{ ParentGroupName }}'
      - name: QueryString
        value: '{{ QueryString }}'
      - name: ThingGroupProperties
        value:
          AttributePayload:
            Attributes: {}
          ThingGroupDescription: '{{ ThingGroupDescription }}'
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
DELETE FROM aws.iot.thing_groups
WHERE data__Identifier = '<ThingGroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>thing_groups</code> resource, the following permissions are required:

### Create
```json
iot:DescribeThingGroup,
iot:ListTagsForResource,
iot:CreateThingGroup,
iot:CreateDynamicThingGroup,
iot:TagResource
```

### Delete
```json
iot:DescribeThingGroup,
iot:DeleteThingGroup,
iot:DeleteDynamicThingGroup
```

### List
```json
iot:ListThingGroups,
iot:ListTagsForResource
```

