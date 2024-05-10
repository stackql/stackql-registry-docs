---
title: crls
hide_title: false
hide_table_of_contents: false
keywords:
  - crls
  - rolesanywhere
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


Used to retrieve a list of <code>crls</code> in a region or to create or delete a <code>crls</code> resource, use <code>crl</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>crls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RolesAnywhere::CRL Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rolesanywhere.crls" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="crl_id" /></td><td><code>string</code></td><td></td></tr>
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
crl_id
FROM aws.rolesanywhere.crls
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
 "CrlData": "{{ CrlData }}",
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.rolesanywhere.crls (
 CrlData,
 Name,
 region
)
SELECT 
{{ .CrlData }},
 {{ .Name }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "CrlData": "{{ CrlData }}",
 "Enabled": "{{ Enabled }}",
 "Name": "{{ Name }}",
 "TrustAnchorArn": "{{ TrustAnchorArn }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.rolesanywhere.crls (
 CrlData,
 Enabled,
 Name,
 TrustAnchorArn,
 Tags,
 region
)
SELECT 
 {{ .CrlData }},
 {{ .Enabled }},
 {{ .Name }},
 {{ .TrustAnchorArn }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.rolesanywhere.crls
WHERE data__Identifier = '<CrlId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>crls</code> resource, the following permissions are required:

### Create
```json
rolesanywhere:ImportCrl,
rolesanywhere:TagResource,
rolesanywhere:ListTagsForResource
```

### Delete
```json
rolesanywhere:DeleteCrl
```

### List
```json
rolesanywhere:ListCrls,
rolesanywhere:ListTagsForResource
```

