---
title: grants
hide_title: false
hide_table_of_contents: false
keywords:
  - grants
  - licensemanager
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


Used to retrieve a list of <code>grants</code> in a region or to create or delete a <code>grants</code> resource, use <code>grant</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.licensemanager.grants" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="grant_arn" /></td><td><code>undefined</code></td><td>Arn of the grant.</td></tr>
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
grant_arn
FROM aws.licensemanager.grants
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
{}
>>>
--required properties only
INSERT INTO aws.licensemanager.grants (
 ,
 region
)
SELECT 
{{  }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "GrantName": "{{ GrantName }}",
 "LicenseArn": "{{ LicenseArn }}",
 "HomeRegion": "{{ HomeRegion }}",
 "AllowedOperations": [
  "{{ AllowedOperations[0] }}"
 ],
 "Principals": [
  null
 ],
 "Status": "{{ Status }}"
}
>>>
--all properties
INSERT INTO aws.licensemanager.grants (
 GrantName,
 LicenseArn,
 HomeRegion,
 AllowedOperations,
 Principals,
 Status,
 region
)
SELECT 
 {{ GrantName }},
 {{ LicenseArn }},
 {{ HomeRegion }},
 {{ AllowedOperations }},
 {{ Principals }},
 {{ Status }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.licensemanager.grants
WHERE data__Identifier = '<GrantArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>grants</code> resource, the following permissions are required:

### Create
```json
license-manager:CreateGrant
```

### Delete
```json
license-manager:DeleteGrant
```

### List
```json
license-manager:ListDistributedGrants
```

