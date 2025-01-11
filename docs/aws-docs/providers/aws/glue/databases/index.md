---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - glue
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

Creates, updates, deletes or gets a <code>database</code> resource or lists <code>databases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Glue::Database</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.glue.databases" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="catalog_id" /></td><td><code>string</code></td><td>The AWS account ID for the account in which to create the catalog object.</td></tr>
<tr><td><CopyableCode code="database_input" /></td><td><code>object</code></td><td>The metadata for the database.</td></tr>
<tr><td><CopyableCode code="database_name" /></td><td><code>string</code></td><td>The name of the database. For hive compatibility, this is folded to lowercase when it is store.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-database.html"><code>AWS::Glue::Database</code></a>.

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
    <td><CopyableCode code="DatabaseInput, CatalogId, region" /></td>
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
Gets all <code>databases</code> in a region.
```sql
SELECT
region,
catalog_id,
database_input,
database_name
FROM aws.glue.databases
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>database</code>.
```sql
SELECT
region,
catalog_id,
database_input,
database_name
FROM aws.glue.databases
WHERE region = 'us-east-1' AND data__Identifier = '<DatabaseName>';
```

## `INSERT` example

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
INSERT INTO aws.glue.databases (
 CatalogId,
 DatabaseInput,
 region
)
SELECT 
'{{ CatalogId }}',
 '{{ DatabaseInput }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.glue.databases (
 CatalogId,
 DatabaseInput,
 DatabaseName,
 region
)
SELECT 
 '{{ CatalogId }}',
 '{{ DatabaseInput }}',
 '{{ DatabaseName }}',
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
      - name: CatalogId
        value: '{{ CatalogId }}'
      - name: DatabaseInput
        value:
          LocationUri: '{{ LocationUri }}'
          CreateTableDefaultPermissions:
            - Permissions:
                - '{{ Permissions[0] }}'
              Principal:
                DataLakePrincipalIdentifier: '{{ DataLakePrincipalIdentifier }}'
          Description: '{{ Description }}'
          Parameters: {}
          TargetDatabase:
            DatabaseName: '{{ DatabaseName }}'
            Region: '{{ Region }}'
            CatalogId: '{{ CatalogId }}'
          FederatedDatabase:
            ConnectionName: '{{ ConnectionName }}'
            Identifier: '{{ Identifier }}'
          Name: '{{ Name }}'
      - name: DatabaseName
        value: '{{ DatabaseName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.glue.databases
WHERE data__Identifier = '<DatabaseName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>databases</code> resource, the following permissions are required:

### Create
```json
glue:CreateDatabase,
glue:GetDatabase,
glue:PassConnection,
glue:CreateConnection,
lakeformation:ListResources,
lakeformation:DescribeResource,
lakeformation:DescribeLakeFormationIdentityCenterConfiguration
```

### Read
```json
glue:GetDatabase,
glue:GetConnection,
lakeformation:ListResources,
lakeformation:DescribeResource,
lakeformation:DescribeLakeFormationIdentityCenterConfiguration
```

### Update
```json
glue:UpdateDatabase,
glue:UpdateConnection,
lakeformation:ListResources,
lakeformation:DescribeResource,
lakeformation:DescribeLakeFormationIdentityCenterConfiguration
```

### Delete
```json
glue:DeleteDatabase,
glue:GetDatabase,
glue:DeleteConnection,
glue:GetConnection,
lakeformation:ListResources,
lakeformation:DescribeResource,
lakeformation:DescribeLakeFormationIdentityCenterConfiguration
```

### List
```json
glue:GetDatabases,
lakeformation:ListResources,
lakeformation:DescribeResource,
lakeformation:DescribeLakeFormationIdentityCenterConfiguration
```
