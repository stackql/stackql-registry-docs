---
title: trust_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - trust_stores
  - workspacesweb
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


Used to retrieve a list of <code>trust_stores</code> in a region or to create or delete a <code>trust_stores</code> resource, use <code>trust_store</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trust_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::WorkSpacesWeb::TrustStore Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspacesweb.trust_stores" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="trust_store_arn" /></td><td><code>string</code></td><td></td></tr>
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
trust_store_arn
FROM aws.workspacesweb.trust_stores
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
 "CertificateList": [
  "{{ CertificateList[0] }}"
 ]
}
>>>
--required properties only
INSERT INTO aws.workspacesweb.trust_stores (
 CertificateList,
 region
)
SELECT 
{{ .CertificateList }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "CertificateList": [
  "{{ CertificateList[0] }}"
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.workspacesweb.trust_stores (
 CertificateList,
 Tags,
 region
)
SELECT 
 {{ .CertificateList }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.workspacesweb.trust_stores
WHERE data__Identifier = '<TrustStoreArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>trust_stores</code> resource, the following permissions are required:

### Create
```json
workspaces-web:CreateTrustStore,
workspaces-web:GetTrustStore,
workspaces-web:GetTrustStoreCertificate,
workspaces-web:ListTrustStoreCertificates,
workspaces-web:ListTagsForResource,
workspaces-web:TagResource
```

### Delete
```json
workspaces-web:GetTrustStore,
workspaces-web:GetTrustStoreCertificate,
workspaces-web:DeleteTrustStore
```

### List
```json
workspaces-web:ListTrustStores,
workspaces-web:ListTrustStoreCertificates
```

