---
title: delegated_admins
hide_title: false
hide_table_of_contents: false
keywords:
  - delegated_admins
  - securityhub
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


Used to retrieve a list of <code>delegated_admins</code> in a region or to create or delete a <code>delegated_admins</code> resource, use <code>delegated_admin</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delegated_admins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::DelegatedAdmin resource represents the AWS Security Hub delegated admin account in your organization. One delegated admin resource is allowed to create for the organization in each region in which you configure the AdminAccountId.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.delegated_admins" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="delegated_admin_identifier" /></td><td><code>string</code></td><td>The identifier of the DelegatedAdmin being created and assigned as the unique identifier</td></tr>
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
delegated_admin_identifier
FROM aws.securityhub.delegated_admins
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
 "AdminAccountId": "{{ AdminAccountId }}"
}
>>>
--required properties only
INSERT INTO aws.securityhub.delegated_admins (
 AdminAccountId,
 region
)
SELECT 
{{ .AdminAccountId }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AdminAccountId": "{{ AdminAccountId }}"
}
>>>
--all properties
INSERT INTO aws.securityhub.delegated_admins (
 AdminAccountId,
 region
)
SELECT 
 {{ .AdminAccountId }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.securityhub.delegated_admins
WHERE data__Identifier = '<DelegatedAdminIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>delegated_admins</code> resource, the following permissions are required:

### Create
```json
securityhub:EnableOrganizationAdminAccount,
organizations:DescribeOrganization,
organizations:EnableAWSServiceAccess,
organizations:RegisterDelegatedAdministrator
```

### Delete
```json
securityhub:DisableOrganizationAdminAccount,
organizations:DescribeOrganization
```

### List
```json
securityhub:ListOrganizationAdminAccounts,
organizations:DescribeOrganization
```

