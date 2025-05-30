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

Creates, updates, deletes or gets a <code>partnership</code> resource or lists <code>partnerships</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partnerships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::B2BI::Partnership Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.b2bi.partnerships" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="capabilities" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="capability_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="email" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="partnership_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="partnership_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="phone" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="profile_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="trading_partner_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-partnership.html"><code>AWS::B2BI::Partnership</code></a>.

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
    <td><CopyableCode code="Capabilities, Email, Name, ProfileId, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>partnerships</code> in a region.
```sql
SELECT
region,
capabilities,
capability_options,
created_at,
email,
modified_at,
name,
partnership_arn,
partnership_id,
phone,
profile_id,
tags,
trading_partner_id
FROM aws.b2bi.partnerships
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>partnership</code>.
```sql
SELECT
region,
capabilities,
capability_options,
created_at,
email,
modified_at,
name,
partnership_arn,
partnership_id,
phone,
profile_id,
tags,
trading_partner_id
FROM aws.b2bi.partnerships
WHERE region = 'us-east-1' AND data__Identifier = '<PartnershipId>';
```

## `INSERT` example

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
/*+ create */
INSERT INTO aws.b2bi.partnerships (
 Capabilities,
 Email,
 Name,
 ProfileId,
 region
)
SELECT 
'{{ Capabilities }}',
 '{{ Email }}',
 '{{ Name }}',
 '{{ ProfileId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.b2bi.partnerships (
 Capabilities,
 CapabilityOptions,
 Email,
 Name,
 Phone,
 ProfileId,
 Tags,
 region
)
SELECT 
 '{{ Capabilities }}',
 '{{ CapabilityOptions }}',
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
      - name: CapabilityOptions
        value:
          OutboundEdi: null
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
b2bi:GetPartnership,
b2bi:ListTagsForResource
```

### Update
```json
b2bi:TagResource,
b2bi:UntagResource,
b2bi:UpdatePartnership
```

### Delete
```json
b2bi:DeletePartnership
```

### List
```json
b2bi:ListPartnerships
```
