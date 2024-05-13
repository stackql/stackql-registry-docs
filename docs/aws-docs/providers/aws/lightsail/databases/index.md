---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - lightsail
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


Used to retrieve a list of <code>databases</code> in a region or to create or delete a <code>databases</code> resource, use <code>database</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::Database</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.databases" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="relational_database_name" /></td><td><code>string</code></td><td>The name to use for your new Lightsail database resource.</td></tr>
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
    <td><CopyableCode code="RelationalDatabaseName, RelationalDatabaseBlueprintId, RelationalDatabaseBundleId, MasterDatabaseName, MasterUsername, region" /></td>
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
relational_database_name
FROM aws.lightsail.databases
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>database</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.lightsail.databases (
 RelationalDatabaseName,
 RelationalDatabaseBlueprintId,
 RelationalDatabaseBundleId,
 MasterDatabaseName,
 MasterUsername,
 region
)
SELECT 
'{{ RelationalDatabaseName }}',
 '{{ RelationalDatabaseBlueprintId }}',
 '{{ RelationalDatabaseBundleId }}',
 '{{ MasterDatabaseName }}',
 '{{ MasterUsername }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.lightsail.databases (
 RelationalDatabaseName,
 AvailabilityZone,
 RelationalDatabaseBlueprintId,
 RelationalDatabaseBundleId,
 MasterDatabaseName,
 MasterUsername,
 MasterUserPassword,
 PreferredBackupWindow,
 PreferredMaintenanceWindow,
 PubliclyAccessible,
 CaCertificateIdentifier,
 BackupRetention,
 RotateMasterUserPassword,
 RelationalDatabaseParameters,
 Tags,
 region
)
SELECT 
 '{{ RelationalDatabaseName }}',
 '{{ AvailabilityZone }}',
 '{{ RelationalDatabaseBlueprintId }}',
 '{{ RelationalDatabaseBundleId }}',
 '{{ MasterDatabaseName }}',
 '{{ MasterUsername }}',
 '{{ MasterUserPassword }}',
 '{{ PreferredBackupWindow }}',
 '{{ PreferredMaintenanceWindow }}',
 '{{ PubliclyAccessible }}',
 '{{ CaCertificateIdentifier }}',
 '{{ BackupRetention }}',
 '{{ RotateMasterUserPassword }}',
 '{{ RelationalDatabaseParameters }}',
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
  - name: database
    props:
      - name: RelationalDatabaseName
        value: '{{ RelationalDatabaseName }}'
      - name: AvailabilityZone
        value: '{{ AvailabilityZone }}'
      - name: RelationalDatabaseBlueprintId
        value: '{{ RelationalDatabaseBlueprintId }}'
      - name: RelationalDatabaseBundleId
        value: '{{ RelationalDatabaseBundleId }}'
      - name: MasterDatabaseName
        value: '{{ MasterDatabaseName }}'
      - name: MasterUsername
        value: '{{ MasterUsername }}'
      - name: MasterUserPassword
        value: '{{ MasterUserPassword }}'
      - name: PreferredBackupWindow
        value: '{{ PreferredBackupWindow }}'
      - name: PreferredMaintenanceWindow
        value: '{{ PreferredMaintenanceWindow }}'
      - name: PubliclyAccessible
        value: '{{ PubliclyAccessible }}'
      - name: CaCertificateIdentifier
        value: '{{ CaCertificateIdentifier }}'
      - name: BackupRetention
        value: '{{ BackupRetention }}'
      - name: RotateMasterUserPassword
        value: '{{ RotateMasterUserPassword }}'
      - name: RelationalDatabaseParameters
        value:
          - AllowedValues: '{{ AllowedValues }}'
            ApplyMethod: '{{ ApplyMethod }}'
            ApplyType: '{{ ApplyType }}'
            DataType: '{{ DataType }}'
            Description: '{{ Description }}'
            IsModifiable: '{{ IsModifiable }}'
            ParameterName: '{{ ParameterName }}'
            ParameterValue: '{{ ParameterValue }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.lightsail.databases
WHERE data__Identifier = '<RelationalDatabaseName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>databases</code> resource, the following permissions are required:

### Create
```json
lightsail:CreateRelationalDatabase,
lightsail:GetRelationalDatabase,
lightsail:GetRelationalDatabases,
lightsail:GetRegions,
lightsail:TagResource,
lightsail:UntagResource,
lightsail:UpdateRelationalDatabase,
lightsail:UpdateRelationalDatabaseParameters
```

### Delete
```json
lightsail:DeleteRelationalDatabase,
lightsail:GetRelationalDatabase,
lightsail:GetRelationalDatabases
```

### List
```json
lightsail:GetRelationalDatabases
```

