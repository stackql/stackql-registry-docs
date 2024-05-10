---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - resourcegroups
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


Used to retrieve a list of <code>groups</code> in a region or to create or delete a <code>groups</code> resource, use <code>group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for ResourceGroups::Group</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.resourcegroups.groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the resource group</td></tr>
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
name
FROM aws.resourcegroups.groups
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- group.iql (required properties only)
INSERT INTO aws.resourcegroups.groups (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- group.iql (all properties)
INSERT INTO aws.resourcegroups.groups (
 Name,
 Description,
 ResourceQuery,
 Tags,
 Configuration,
 Resources,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ ResourceQuery }}',
 '{{ Tags }}',
 '{{ Configuration }}',
 '{{ Resources }}',
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
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: ResourceQuery
        value:
          Type: '{{ Type }}'
          Query:
            ResourceTypeFilters:
              - '{{ ResourceTypeFilters[0] }}'
            StackIdentifier: '{{ StackIdentifier }}'
            TagFilters:
              - Key: '{{ Key }}'
                Values:
                  - '{{ Values[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Configuration
        value:
          - Type: '{{ Type }}'
            Parameters:
              - Name: '{{ Name }}'
                Values:
                  - '{{ Values[0] }}'
      - name: Resources
        value:
          - '{{ Resources[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.resourcegroups.groups
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>groups</code> resource, the following permissions are required:

### Create
```json
resource-groups:CreateGroup,
resource-groups:Tag,
cloudformation:DescribeStacks,
cloudformation:ListStackResources,
resource-groups:ListGroupResources,
resource-groups:GroupResources
```

### Delete
```json
resource-groups:DeleteGroup,
resource-groups:UnGroupResources
```

### List
```json
resource-groups:ListGroups
```

