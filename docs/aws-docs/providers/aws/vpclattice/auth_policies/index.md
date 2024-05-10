---
title: auth_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - auth_policies
  - vpclattice
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


Used to retrieve a list of <code>auth_policies</code> in a region or to create or delete a <code>auth_policies</code> resource, use <code>auth_policy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auth_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates or updates the auth policy.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.auth_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
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
resource_identifier
FROM aws.vpclattice.auth_policies
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
 "ResourceIdentifier": "{{ ResourceIdentifier }}",
 "Policy": {}
}
>>>
--required properties only
INSERT INTO aws.vpclattice.auth_policies (
 ResourceIdentifier,
 Policy,
 region
)
SELECT 
{{ .ResourceIdentifier }},
 {{ .Policy }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ResourceIdentifier": "{{ ResourceIdentifier }}",
 "Policy": {}
}
>>>
--all properties
INSERT INTO aws.vpclattice.auth_policies (
 ResourceIdentifier,
 Policy,
 region
)
SELECT 
 {{ .ResourceIdentifier }},
 {{ .Policy }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.vpclattice.auth_policies
WHERE data__Identifier = '<ResourceIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>auth_policies</code> resource, the following permissions are required:

### Create
```json
vpc-lattice:GetAuthPolicy,
vpc-lattice:PutAuthPolicy
```

### Delete
```json
vpc-lattice:GetAuthPolicy,
vpc-lattice:DeleteAuthPolicy
```

