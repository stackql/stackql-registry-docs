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

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "DatasetName": "{{ DatasetName }}",
 "Name": "{{ Name }}",
 "RecipeName": "{{ RecipeName }}",
 "RoleArn": "{{ RoleArn }}"
}
>>>
--required properties only
INSERT INTO aws.databrew.projects (
 DatasetName,
 Name,
 RecipeName,
 RoleArn,
 region
)
SELECT 
{{ DatasetName }},
 {{ Name }},
 {{ RecipeName }},
 {{ RoleArn }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DatasetName": "{{ DatasetName }}",
 "Name": "{{ Name }}",
 "RecipeName": "{{ RecipeName }}",
 "RoleArn": "{{ RoleArn }}",
 "Sample": {
  "Size": "{{ Size }}",
  "Type": "{{ Type }}"
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
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
 {{ DatasetName }},
 {{ Name }},
 {{ RecipeName }},
 {{ RoleArn }},
 {{ Sample }},
 {{ Tags }},
 'us-east-1';
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

