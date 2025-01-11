---
title: data_migrations
hide_title: false
hide_table_of_contents: false
keywords:
  - data_migrations
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

Creates, updates, deletes or gets a <code>data_migration</code> resource or lists <code>data_migrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_migrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DMS::DataMigration.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dms.data_migrations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="data_migration_name" /></td><td><code>string</code></td><td>The property describes a name to identify the data migration.</td></tr>
<tr><td><CopyableCode code="data_migration_arn" /></td><td><code>string</code></td><td>The property describes an ARN of the data migration.</td></tr>
<tr><td><CopyableCode code="data_migration_identifier" /></td><td><code>string</code></td><td>The property describes an ARN of the data migration.</td></tr>
<tr><td><CopyableCode code="data_migration_create_time" /></td><td><code>string</code></td><td>The property describes the create time of the data migration.</td></tr>
<tr><td><CopyableCode code="service_access_role_arn" /></td><td><code>string</code></td><td>The property describes Amazon Resource Name (ARN) of the service access role.</td></tr>
<tr><td><CopyableCode code="migration_project_identifier" /></td><td><code>string</code></td><td>The property describes an identifier for the migration project. It is used for describing/deleting/modifying can be name/arn</td></tr>
<tr><td><CopyableCode code="data_migration_type" /></td><td><code>string</code></td><td>The property describes the type of migration.</td></tr>
<tr><td><CopyableCode code="data_migration_settings" /></td><td><code>object</code></td><td>The property describes the settings for the data migration.</td></tr>
<tr><td><CopyableCode code="source_data_settings" /></td><td><code>array</code></td><td>The property describes the settings for the data migration.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-datamigration.html"><code>AWS::DMS::DataMigration</code></a>.

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
    <td><CopyableCode code="DataMigrationType, MigrationProjectIdentifier, ServiceAccessRoleArn, region" /></td>
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
Gets all <code>data_migrations</code> in a region.
```sql
SELECT
region,
data_migration_name,
data_migration_arn,
data_migration_identifier,
data_migration_create_time,
service_access_role_arn,
migration_project_identifier,
data_migration_type,
data_migration_settings,
source_data_settings,
tags
FROM aws.dms.data_migrations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>data_migration</code>.
```sql
SELECT
region,
data_migration_name,
data_migration_arn,
data_migration_identifier,
data_migration_create_time,
service_access_role_arn,
migration_project_identifier,
data_migration_type,
data_migration_settings,
source_data_settings,
tags
FROM aws.dms.data_migrations
WHERE region = 'us-east-1' AND data__Identifier = '<DataMigrationArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_migration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.dms.data_migrations (
 ServiceAccessRoleArn,
 MigrationProjectIdentifier,
 DataMigrationType,
 region
)
SELECT 
'{{ ServiceAccessRoleArn }}',
 '{{ MigrationProjectIdentifier }}',
 '{{ DataMigrationType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.dms.data_migrations (
 DataMigrationName,
 DataMigrationIdentifier,
 ServiceAccessRoleArn,
 MigrationProjectIdentifier,
 DataMigrationType,
 DataMigrationSettings,
 SourceDataSettings,
 Tags,
 region
)
SELECT 
 '{{ DataMigrationName }}',
 '{{ DataMigrationIdentifier }}',
 '{{ ServiceAccessRoleArn }}',
 '{{ MigrationProjectIdentifier }}',
 '{{ DataMigrationType }}',
 '{{ DataMigrationSettings }}',
 '{{ SourceDataSettings }}',
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
  - name: data_migration
    props:
      - name: DataMigrationName
        value: '{{ DataMigrationName }}'
      - name: DataMigrationIdentifier
        value: '{{ DataMigrationIdentifier }}'
      - name: ServiceAccessRoleArn
        value: '{{ ServiceAccessRoleArn }}'
      - name: MigrationProjectIdentifier
        value: '{{ MigrationProjectIdentifier }}'
      - name: DataMigrationType
        value: '{{ DataMigrationType }}'
      - name: DataMigrationSettings
        value:
          CloudwatchLogsEnabled: '{{ CloudwatchLogsEnabled }}'
          NumberOfJobs: '{{ NumberOfJobs }}'
          SelectionRules: '{{ SelectionRules }}'
      - name: SourceDataSettings
        value:
          - CDCStartPosition: '{{ CDCStartPosition }}'
            CDCStartTime: '{{ CDCStartTime }}'
            CDCStopTime: '{{ CDCStopTime }}'
            SlotName: '{{ SlotName }}'
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
DELETE FROM aws.dms.data_migrations
WHERE data__Identifier = '<DataMigrationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>data_migrations</code> resource, the following permissions are required:

### Create
```json
dms:CreateDataMigration,
dms:DescribeDataMigrations,
dms:AddTagsToResource,
dms:ListTagsForResource,
iam:PassRole
```

### Read
```json
dms:DescribeDataMigrations,
dms:ListTagsForResource
```

### Update
```json
dms:ModifyDataMigration,
dms:AddTagsToResource,
dms:RemoveTagsFromResource,
dms:ListTagsForResource,
iam:PassRole
```

### Delete
```json
dms:DeleteDataMigration,
dms:RemoveTagsFromResource
```

### List
```json
dms:DescribeDataMigrations,
dms:ListTagsForResource
```
