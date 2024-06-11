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

Creates, updates, deletes or gets a <code>crl</code> resource or lists <code>crls</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>crls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RolesAnywhere::CRL Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rolesanywhere.crls" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="crl_data" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="crl_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="trust_anchor_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="Name, CrlData, region" /></td>
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
List all <code>crls</code> in a region.
```sql
SELECT
region,
crl_id
FROM aws.rolesanywhere.crls
WHERE region = 'us-east-1';
```
Gets all properties from a <code>crl</code>.
```sql
SELECT
region,
crl_data,
crl_id,
enabled,
name,
trust_anchor_arn,
tags
FROM aws.rolesanywhere.crls
WHERE region = 'us-east-1' AND data__Identifier = '<CrlId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>crl</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.rolesanywhere.crls (
 CrlData,
 Name,
 region
)
SELECT 
'{{ CrlData }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.rolesanywhere.crls (
 CrlData,
 Enabled,
 Name,
 TrustAnchorArn,
 Tags,
 region
)
SELECT 
 '{{ CrlData }}',
 '{{ Enabled }}',
 '{{ Name }}',
 '{{ TrustAnchorArn }}',
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
  - name: crl
    props:
      - name: CrlData
        value: '{{ CrlData }}'
      - name: Enabled
        value: '{{ Enabled }}'
      - name: Name
        value: '{{ Name }}'
      - name: TrustAnchorArn
        value: '{{ TrustAnchorArn }}'
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

### Read
```json
rolesanywhere:GetCrl,
rolesanywhere:ListTagsForResource
```

### Update
```json
rolesanywhere:EnableCrl,
rolesanywhere:DisableCrl,
rolesanywhere:UpdateCrl,
rolesanywhere:TagResource,
rolesanywhere:UntagResource,
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

