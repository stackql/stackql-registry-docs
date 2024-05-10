---
title: migration_projects
hide_title: false
hide_table_of_contents: false
keywords:
  - migration_projects
  - dms
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


Used to retrieve a list of <code>migration_projects</code> in a region or to create or delete a <code>migration_projects</code> resource, use <code>migration_project</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>migration_projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DMS::MigrationProject</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dms.migration_projects" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="migration_project_arn" /></td><td><code>string</code></td><td>The property describes an ARN of the migration project.</td></tr>
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
migration_project_arn
FROM aws.dms.migration_projects
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>migration_project</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- migration_project.iql (required properties only)
INSERT INTO aws.dms.migration_projects (
 MigrationProjectName,
 MigrationProjectIdentifier,
 MigrationProjectCreationTime,
 InstanceProfileIdentifier,
 InstanceProfileName,
 InstanceProfileArn,
 TransformationRules,
 Description,
 SchemaConversionApplicationAttributes,
 SourceDataProviderDescriptors,
 TargetDataProviderDescriptors,
 Tags,
 region
)
SELECT 
'{{ MigrationProjectName }}',
 '{{ MigrationProjectIdentifier }}',
 '{{ MigrationProjectCreationTime }}',
 '{{ InstanceProfileIdentifier }}',
 '{{ InstanceProfileName }}',
 '{{ InstanceProfileArn }}',
 '{{ TransformationRules }}',
 '{{ Description }}',
 '{{ SchemaConversionApplicationAttributes }}',
 '{{ SourceDataProviderDescriptors }}',
 '{{ TargetDataProviderDescriptors }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- migration_project.iql (all properties)
INSERT INTO aws.dms.migration_projects (
 MigrationProjectName,
 MigrationProjectIdentifier,
 MigrationProjectCreationTime,
 InstanceProfileIdentifier,
 InstanceProfileName,
 InstanceProfileArn,
 TransformationRules,
 Description,
 SchemaConversionApplicationAttributes,
 SourceDataProviderDescriptors,
 TargetDataProviderDescriptors,
 Tags,
 region
)
SELECT 
 '{{ MigrationProjectName }}',
 '{{ MigrationProjectIdentifier }}',
 '{{ MigrationProjectCreationTime }}',
 '{{ InstanceProfileIdentifier }}',
 '{{ InstanceProfileName }}',
 '{{ InstanceProfileArn }}',
 '{{ TransformationRules }}',
 '{{ Description }}',
 '{{ SchemaConversionApplicationAttributes }}',
 '{{ SourceDataProviderDescriptors }}',
 '{{ TargetDataProviderDescriptors }}',
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
  - name: migration_project
    props:
      - name: MigrationProjectName
        value: '{{ MigrationProjectName }}'
      - name: MigrationProjectIdentifier
        value: '{{ MigrationProjectIdentifier }}'
      - name: MigrationProjectCreationTime
        value: '{{ MigrationProjectCreationTime }}'
      - name: InstanceProfileIdentifier
        value: '{{ InstanceProfileIdentifier }}'
      - name: InstanceProfileName
        value: '{{ InstanceProfileName }}'
      - name: InstanceProfileArn
        value: '{{ InstanceProfileArn }}'
      - name: TransformationRules
        value: '{{ TransformationRules }}'
      - name: Description
        value: '{{ Description }}'
      - name: SchemaConversionApplicationAttributes
        value:
          S3BucketPath: '{{ S3BucketPath }}'
          S3BucketRoleArn: '{{ S3BucketRoleArn }}'
      - name: SourceDataProviderDescriptors
        value:
          - DataProviderIdentifier: '{{ DataProviderIdentifier }}'
            DataProviderName: '{{ DataProviderName }}'
            DataProviderArn: '{{ DataProviderArn }}'
            SecretsManagerSecretId: '{{ SecretsManagerSecretId }}'
            SecretsManagerAccessRoleArn: '{{ SecretsManagerAccessRoleArn }}'
      - name: TargetDataProviderDescriptors
        value:
          - null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.dms.migration_projects
WHERE data__Identifier = '<MigrationProjectArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>migration_projects</code> resource, the following permissions are required:

### Create
```json
dms:CreateMigrationProject,
dms:ListMigrationProjects,
dms:DescribeMigrationProjects,
dms:AddTagsToResource,
dms:ListTagsForResource,
iam:PassRole
```

### Delete
```json
dms:DeleteMigrationProject
```

### List
```json
dms:ListMigrationProjects,
dms:DescribeMigrationProjects,
dms:ListTagsForResource
```

