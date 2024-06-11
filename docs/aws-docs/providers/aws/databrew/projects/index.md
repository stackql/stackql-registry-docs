---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - databrew
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

Creates, updates, deletes or gets a <code>project</code> resource or lists <code>projects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataBrew::Project.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.databrew.projects" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="dataset_name" /></td><td><code>string</code></td><td>Dataset name</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Project name</td></tr>
<tr><td><CopyableCode code="recipe_name" /></td><td><code>string</code></td><td>Recipe name</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>Role arn</td></tr>
<tr><td><CopyableCode code="sample" /></td><td><code>object</code></td><td>Sample</td></tr>
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
    <td><CopyableCode code="DatasetName, Name, RecipeName, RoleArn, region" /></td>
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
List all <code>projects</code> in a region.
```sql
SELECT
region,
name
FROM aws.databrew.projects
WHERE region = 'us-east-1';
```
Gets all properties from a <code>project</code>.
```sql
SELECT
region,
dataset_name,
name,
recipe_name,
role_arn,
sample,
tags
FROM aws.databrew.projects
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>project</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.databrew.projects (
 DatasetName,
 Name,
 RecipeName,
 RoleArn,
 region
)
SELECT 
'{{ DatasetName }}',
 '{{ Name }}',
 '{{ RecipeName }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.databrew.projects (
 DatasetName,
 Name,
 RecipeName,
 RoleArn,
 Sample,
 Tags,
 region
)
SELECT 
 '{{ DatasetName }}',
 '{{ Name }}',
 '{{ RecipeName }}',
 '{{ RoleArn }}',
 '{{ Sample }}',
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
  - name: project
    props:
      - name: DatasetName
        value: '{{ DatasetName }}'
      - name: Name
        value: '{{ Name }}'
      - name: RecipeName
        value: '{{ RecipeName }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Sample
        value:
          Size: '{{ Size }}'
          Type: '{{ Type }}'
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
DELETE FROM aws.databrew.projects
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>projects</code> resource, the following permissions are required:

### Create
```json
databrew:CreateProject,
databrew:TagResource,
databrew:UntagResource,
iam:PassRole
```

### Read
```json
databrew:DescribeProject,
databrew:ListTagsForResource,
iam:ListRoles
```

### Update
```json
databrew:UpdateProject,
iam:PassRole
```

### Delete
```json
databrew:DeleteProject
```

### List
```json
databrew:ListProjects,
databrew:ListTagsForResource,
iam:ListRoles
```

