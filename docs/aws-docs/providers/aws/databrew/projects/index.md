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


Used to retrieve a list of <code>projects</code> in a region or to create or delete a <code>projects</code> resource, use <code>project</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataBrew::Project.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.databrew.projects" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Project name</td></tr>
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
FROM aws.databrew.projects
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>project</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- project.iql (required properties only)
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
-- project.iql (all properties)
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

## `DELETE` Example

```sql
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

