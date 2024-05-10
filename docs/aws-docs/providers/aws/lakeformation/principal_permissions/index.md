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


Gets or updates an individual <code>principal_permissions</code> resource, use <code>principal_permissions</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>principal_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::LakeFormation::PrincipalPermissions`` resource represents the permissions that a principal has on a GLUDC resource (such as GLUlong databases or GLUlong tables). When you create a ``PrincipalPermissions`` resource, the permissions are granted via the LFlong ``GrantPermissions`` API operation. When you delete a ``PrincipalPermissions`` resource, the permissions on principal-resource pair are revoked via the LFlong ``RevokePermissions`` API operation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lakeformation.principal_permissions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="catalog" /></td><td><code>string</code></td><td>The identifier for the GLUDC. By default, the account ID. The GLUDC is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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


## Permissions

To operate on the <code>principal_permissions</code> resource, the following permissions are required:

### Read
```json
lakeformation:ListPermissions,
glue:GetTable,
glue:GetDatabase
```

