---
title: partnerships
hide_title: false
hide_table_of_contents: false
keywords:
  - partnerships
  - b2bi
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


Used to retrieve a list of <code>partnerships</code> in a region or to create or delete a <code>partnerships</code> resource, use <code>partnership</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partnerships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::B2BI::Partnership Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.b2bi.partnerships" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="partnership_id" /></td><td><code>string</code></td><td></td></tr>
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
partnership_id
FROM aws.b2bi.partnerships
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>partnership</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- partnership.iql (required properties only)
INSERT INTO aws.b2bi.partnerships (
 Email,
 Name,
 ProfileId,
 region
)
SELECT 
'{{ Email }}',
 '{{ Name }}',
 '{{ ProfileId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- partnership.iql (all properties)
INSERT INTO aws.b2bi.partnerships (
 Capabilities,
 Email,
 Name,
 Phone,
 ProfileId,
 Tags,
 region
)
SELECT 
 '{{ Capabilities }}',
 '{{ Email }}',
 '{{ Name }}',
 '{{ Phone }}',
 '{{ ProfileId }}',
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
  - name: partnership
    props:
      - name: Capabilities
        value:
          - '{{ Capabilities[0] }}'
      - name: Email
        value: '{{ Email }}'
      - name: Name
        value: '{{ Name }}'
      - name: Phone
        value: '{{ Phone }}'
      - name: ProfileId
        value: '{{ ProfileId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.b2bi.partnerships
WHERE data__Identifier = '<PartnershipId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>partnerships</code> resource, the following permissions are required:

### Create
```json
b2bi:CreatePartnership,
b2bi:TagResource,
s3:PutObject
```

### Delete
```json
b2bi:DeletePartnership
```

### List
```json
b2bi:ListPartnerships
```

