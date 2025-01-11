---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - lookoutvision
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
<tr><td><b>Description</b></td><td>The AWS::LookoutVision::Project type creates an Amazon Lookout for Vision project. A project is a grouping of the resources needed to create and manage a Lookout for Vision model.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lookoutvision.projects" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="project_name" /></td><td><code>string</code></td><td>The name of the Amazon Lookout for Vision project</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutvision-project.html"><code>AWS::LookoutVision::Project</code></a>.

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
    <td><CopyableCode code="ProjectName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>projects</code> in a region.
```sql
SELECT
region,
arn,
project_name
FROM aws.lookoutvision.projects
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>project</code>.
```sql
SELECT
region,
arn,
project_name
FROM aws.lookoutvision.projects
WHERE region = 'us-east-1' AND data__Identifier = '<ProjectName>';
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
INSERT INTO aws.lookoutvision.projects (
 ProjectName,
 region
)
SELECT 
'{{ ProjectName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.lookoutvision.projects (
 ProjectName,
 region
)
SELECT 
 '{{ ProjectName }}',
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
      - name: ProjectName
        value: '{{ ProjectName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.lookoutvision.projects
WHERE data__Identifier = '<ProjectName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>projects</code> resource, the following permissions are required:

### Create
```json
lookoutvision:CreateProject
```

### Read
```json
lookoutvision:DescribeProject
```

### Delete
```json
lookoutvision:DeleteProject
```

### List
```json
lookoutvision:ListProjects
```
