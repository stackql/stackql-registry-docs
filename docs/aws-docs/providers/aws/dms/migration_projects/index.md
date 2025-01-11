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

Creates, updates, deletes or gets a <code>migration_project</code> resource or lists <code>migration_projects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>migration_projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DMS::MigrationProject</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dms.migration_projects" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="migration_project_name" /></td><td><code>string</code></td><td>The property describes a name to identify the migration project.</td></tr>
<tr><td><CopyableCode code="migration_project_identifier" /></td><td><code>string</code></td><td>The property describes an identifier for the migration project. It is used for describing/deleting/modifying can be name/arn</td></tr>
<tr><td><CopyableCode code="migration_project_arn" /></td><td><code>string</code></td><td>The property describes an ARN of the migration project.</td></tr>
<tr><td><CopyableCode code="migration_project_creation_time" /></td><td><code>string</code></td><td>The property describes a creating time of the migration project.</td></tr>
<tr><td><CopyableCode code="instance_profile_identifier" /></td><td><code>string</code></td><td>The property describes an instance profile identifier for the migration project. For create</td></tr>
<tr><td><CopyableCode code="instance_profile_name" /></td><td><code>string</code></td><td>The property describes an instance profile name for the migration project. For read</td></tr>
<tr><td><CopyableCode code="instance_profile_arn" /></td><td><code>string</code></td><td>The property describes an instance profile arn for the migration project. For read</td></tr>
<tr><td><CopyableCode code="transformation_rules" /></td><td><code>string</code></td><td>The property describes transformation rules for the migration project.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The optional description of the migration project.</td></tr>
<tr><td><CopyableCode code="schema_conversion_application_attributes" /></td><td><code>object</code></td><td>The property describes schema conversion application attributes for the migration project.</td></tr>
<tr><td><CopyableCode code="source_data_provider_descriptors" /></td><td><code>array</code></td><td>The property describes source data provider descriptors for the migration project.</td></tr>
<tr><td><CopyableCode code="target_data_provider_descriptors" /></td><td><code>array</code></td><td>The property describes target data provider descriptors for the migration project.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-migrationproject.html"><code>AWS::DMS::MigrationProject</code></a>.

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
Gets all <code>migration_projects</code> in a region.
```sql
SELECT
region,
migration_project_name,
migration_project_identifier,
migration_project_arn,
migration_project_creation_time,
instance_profile_identifier,
instance_profile_name,
instance_profile_arn,
transformation_rules,
description,
schema_conversion_application_attributes,
source_data_provider_descriptors,
target_data_provider_descriptors,
tags
FROM aws.dms.migration_projects
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>migration_project</code>.
```sql
SELECT
region,
migration_project_name,
migration_project_identifier,
migration_project_arn,
migration_project_creation_time,
instance_profile_identifier,
instance_profile_name,
instance_profile_arn,
transformation_rules,
description,
schema_conversion_application_attributes,
source_data_provider_descriptors,
target_data_provider_descriptors,
tags
FROM aws.dms.migration_projects
WHERE region = 'us-east-1' AND data__Identifier = '<MigrationProjectArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>migration_project</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
dms:DescribeMigrationProjects,
dms:ListMigrationProjects,
dms:ListTagsForResource
```

### Update
```json
dms:UpdateMigrationProject,
dms:ModifyMigrationProject,
dms:AddTagsToResource,
dms:RemoveTagsFromResource,
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
