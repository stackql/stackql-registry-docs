---
title: principal_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - principal_permissions
  - lakeformation
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

Creates, updates, deletes or gets a <code>principal_permission</code> resource or lists <code>principal_permissions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>principal_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::LakeFormation::PrincipalPermissions</code> resource represents the permissions that a principal has on a GLUDC resource (such as GLUlong databases or GLUlong tables). When you create a <code>PrincipalPermissions</code> resource, the permissions are granted via the LFlong <code>GrantPermissions</code> API operation. When you delete a <code>PrincipalPermissions</code> resource, the permissions on principal-resource pair are revoked via the LFlong <code>RevokePermissions</code> API operation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lakeformation.principal_permissions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="catalog" /></td><td><code>string</code></td><td>The identifier for the GLUDC. By default, the account ID. The GLUDC is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.</td></tr>
<tr><td><CopyableCode code="principal" /></td><td><code>object</code></td><td>The principal to be granted a permission.</td></tr>
<tr><td><CopyableCode code="resource" /></td><td><code>object</code></td><td>The resource to be granted or revoked permissions.</td></tr>
<tr><td><CopyableCode code="permissions" /></td><td><code>array</code></td><td>The permissions granted or revoked.</td></tr>
<tr><td><CopyableCode code="permissions_with_grant_option" /></td><td><code>array</code></td><td>Indicates the ability to grant permissions (as a subset of permissions granted).</td></tr>
<tr><td><CopyableCode code="principal_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_identifier" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="Principal, Resource, Permissions, PermissionsWithGrantOption, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from an individual <code>principal_permission</code>.
```sql
SELECT
region,
catalog,
principal,
resource,
permissions,
permissions_with_grant_option,
principal_identifier,
resource_identifier
FROM aws.lakeformation.principal_permissions
WHERE region = 'us-east-1' AND data__Identifier = '<PrincipalIdentifier>|<ResourceIdentifier>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>principal_permission</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.lakeformation.principal_permissions (
 Principal,
 Resource,
 Permissions,
 PermissionsWithGrantOption,
 region
)
SELECT 
'{{ Principal }}',
 '{{ Resource }}',
 '{{ Permissions }}',
 '{{ PermissionsWithGrantOption }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.lakeformation.principal_permissions (
 Catalog,
 Principal,
 Resource,
 Permissions,
 PermissionsWithGrantOption,
 region
)
SELECT 
 '{{ Catalog }}',
 '{{ Principal }}',
 '{{ Resource }}',
 '{{ Permissions }}',
 '{{ PermissionsWithGrantOption }}',
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
  - name: principal_permission
    props:
      - name: Catalog
        value: '{{ Catalog }}'
      - name: Principal
        value:
          DataLakePrincipalIdentifier: '{{ DataLakePrincipalIdentifier }}'
      - name: Resource
        value:
          Catalog: {}
          Database:
            CatalogId: null
            Name: '{{ Name }}'
          Table:
            CatalogId: null
            DatabaseName: null
            Name: null
            TableWildcard: {}
          TableWithColumns:
            CatalogId: null
            DatabaseName: null
            Name: null
            ColumnNames:
              - null
      - name: Permissions
        value:
          - '{{ Permissions[0] }}'
      - name: PermissionsWithGrantOption
        value: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.lakeformation.principal_permissions
WHERE data__Identifier = '<PrincipalIdentifier|ResourceIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>principal_permissions</code> resource, the following permissions are required:

### Create
```json
lakeformation:GrantPermissions,
lakeformation:ListPermissions,
glue:GetTable,
glue:GetDatabase
```

### Read
```json
lakeformation:ListPermissions,
glue:GetTable,
glue:GetDatabase
```

### Delete
```json
lakeformation:RevokePermissions,
lakeformation:ListPermissions,
glue:GetTable,
glue:GetDatabase
```

