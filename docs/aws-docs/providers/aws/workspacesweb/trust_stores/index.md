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

Creates, updates, deletes or gets a <code>trust_store</code> resource or lists <code>trust_stores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trust_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::WorkSpacesWeb::TrustStore Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspacesweb.trust_stores" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="associated_portal_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_list" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="CertificateList, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>trust_stores</code> in a region.
```sql
SELECT
region,
trust_store_arn
FROM aws.workspacesweb.trust_stores
WHERE region = 'us-east-1';
```
Gets all properties from a <code>trust_store</code>.
```sql
SELECT
region,
associated_portal_arns,
certificate_list,
tags,
trust_store_arn
FROM aws.workspacesweb.trust_stores
WHERE region = 'us-east-1' AND data__Identifier = '<TrustStoreArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>trust_store</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.workspacesweb.trust_stores (
 CertificateList,
 region
)
SELECT 
'{{ CertificateList }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.workspacesweb.trust_stores (
 CertificateList,
 Tags,
 region
)
SELECT 
 '{{ CertificateList }}',
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
  - name: trust_store
    props:
      - name: CertificateList
        value:
          - '{{ CertificateList[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
workspaces-web:GetTrustStore,
workspaces-web:GetTrustStoreCertificate,
workspaces-web:ListTagsForResource,
workspaces-web:ListTrustStoreCertificates
```

### Update
```json
workspaces-web:UpdateTrustStore,
workspaces-web:TagResource,
workspaces-web:UntagResource,
workspaces-web:GetTrustStore,
workspaces-web:GetTrustStoreCertificate,
workspaces-web:ListTagsForResource,
workspaces-web:ListTrustStoreCertificates
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

