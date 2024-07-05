---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - iotsitewise
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
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::Project</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotsitewise.projects" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="portal_id" /></td><td><code>string</code></td><td>The ID of the portal in which to create the project.</td></tr>
<tr><td><CopyableCode code="project_id" /></td><td><code>string</code></td><td>The ID of the project.</td></tr>
<tr><td><CopyableCode code="project_name" /></td><td><code>string</code></td><td>A friendly name for the project.</td></tr>
<tr><td><CopyableCode code="project_description" /></td><td><code>string</code></td><td>A description for the project.</td></tr>
<tr><td><CopyableCode code="project_arn" /></td><td><code>string</code></td><td>The ARN of the project.</td></tr>
<tr><td><CopyableCode code="asset_ids" /></td><td><code>array</code></td><td>The IDs of the assets to be associated to the project.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the project.</td></tr>
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
    <td><CopyableCode code="PortalId, ProjectName, region" /></td>
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
Gets all <code>projects</code> in a region.
```sql
SELECT
region,
portal_id,
project_id,
project_name,
project_description,
project_arn,
asset_ids,
tags
FROM aws.iotsitewise.projects
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>project</code>.
```sql
SELECT
region,
portal_id,
project_id,
project_name,
project_description,
project_arn,
asset_ids,
tags
FROM aws.iotsitewise.projects
WHERE region = 'us-east-1' AND data__Identifier = '<ProjectId>';
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
INSERT INTO aws.iotsitewise.projects (
 PortalId,
 ProjectName,
 region
)
SELECT 
'{{ PortalId }}',
 '{{ ProjectName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotsitewise.projects (
 PortalId,
 ProjectName,
 ProjectDescription,
 AssetIds,
 Tags,
 region
)
SELECT 
 '{{ PortalId }}',
 '{{ ProjectName }}',
 '{{ ProjectDescription }}',
 '{{ AssetIds }}',
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
      - name: PortalId
        value: '{{ PortalId }}'
      - name: ProjectName
        value: '{{ ProjectName }}'
      - name: ProjectDescription
        value: '{{ ProjectDescription }}'
      - name: AssetIds
        value:
          - '{{ AssetIds[0] }}'
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
DELETE FROM aws.iotsitewise.projects
WHERE data__Identifier = '<ProjectId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>projects</code> resource, the following permissions are required:

### Create
```json
iotsitewise:CreateProject,
iotsitewise:DescribeProject,
iotsitewise:ListProjectAssets,
iotsitewise:ListTagsForResource,
iotsitewise:TagResource,
iotsitewise:BatchAssociateProjectAssets
```

### Read
```json
iotsitewise:DescribeProject,
iotsitewise:ListTagsForResource,
iotsitewise:ListProjectAssets
```

### Update
```json
iotsitewise:DescribeProject,
iotsitewise:UpdateProject,
iotsitewise:BatchAssociateProjectAssets,
iotsitewise:BatchDisAssociateProjectAssets,
iotsitewise:ListProjectAssets,
iotsitewise:TagResource,
iotsitewise:UntagResource,
iotsitewise:ListTagsForResource
```

### Delete
```json
iotsitewise:DescribeProject,
iotsitewise:DeleteProject
```

### List
```json
iotsitewise:ListProjects
```

