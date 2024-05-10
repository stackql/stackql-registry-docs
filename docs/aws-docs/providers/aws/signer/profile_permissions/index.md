---
title: profile_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - profile_permissions
  - signer
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


Used to retrieve a list of <code>profile_permissions</code> in a region or to create or delete a <code>profile_permissions</code> resource, use <code>profile_permission</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profile_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.signer.profile_permissions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="statement_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="profile_name" /></td><td><code>string</code></td><td></td></tr>
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
statement_id,
profile_name
FROM aws.signer.profile_permissions
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
 "ProfileName": "{{ ProfileName }}",
 "Action": "{{ Action }}",
 "Principal": "{{ Principal }}",
 "StatementId": "{{ StatementId }}"
}
>>>
--required properties only
INSERT INTO aws.signer.profile_permissions (
 ProfileName,
 Action,
 Principal,
 StatementId,
 region
)
SELECT 
{{ ProfileName }},
 {{ Action }},
 {{ Principal }},
 {{ StatementId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ProfileName": "{{ ProfileName }}",
 "ProfileVersion": "{{ ProfileVersion }}",
 "Action": "{{ Action }}",
 "Principal": "{{ Principal }}",
 "StatementId": "{{ StatementId }}"
}
>>>
--all properties
INSERT INTO aws.signer.profile_permissions (
 ProfileName,
 ProfileVersion,
 Action,
 Principal,
 StatementId,
 region
)
SELECT 
 {{ ProfileName }},
 {{ ProfileVersion }},
 {{ Action }},
 {{ Principal }},
 {{ StatementId }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.signer.profile_permissions
WHERE data__Identifier = '<StatementId|ProfileName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>profile_permissions</code> resource, the following permissions are required:

### Create
```json
signer:AddProfilePermission,
signer:ListProfilePermissions
```

### Delete
```json
signer:RemoveProfilePermission,
signer:ListProfilePermissions
```

### List
```json
signer:ListProfilePermissions,
signer:GetSigningProfile
```

