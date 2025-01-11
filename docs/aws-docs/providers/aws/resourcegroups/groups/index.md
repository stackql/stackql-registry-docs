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

Creates, updates, deletes or gets a <code>group</code> resource or lists <code>groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for ResourceGroups::Group</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.resourcegroups.groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the resource group</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the resource group</td></tr>
<tr><td><CopyableCode code="resource_query" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Resource Group ARN.</td></tr>
<tr><td><CopyableCode code="configuration" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="resources" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html"><code>AWS::ResourceGroups::Group</code></a>.

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
    <td><CopyableCode code="Name, region" /></td>
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
Gets all <code>groups</code> in a region.
```sql
SELECT
region,
name,
description,
resource_query,
tags,
arn,
configuration,
resources
FROM aws.resourcegroups.groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>group</code>.
```sql
SELECT
region,
name,
description,
resource_query,
tags,
arn,
configuration,
resources
FROM aws.resourcegroups.groups
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
resource-groups:GetGroup,
resource-groups:GetGroupQuery,
resource-groups:GetTags,
resource-groups:GetGroupConfiguration,
resource-groups:ListGroupResources
```

### Update
```json
resource-groups:UpdateGroup,
resource-groups:GetTags,
resource-groups:GetGroupQuery,
resource-groups:UpdateGroupQuery,
resource-groups:Tag,
resource-groups:Untag,
resource-groups:PutGroupConfiguration,
resource-groups:GetGroupConfiguration,
resource-groups:ListGroupResources,
resource-groups:GroupResources,
resource-groups:UnGroupResources
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
