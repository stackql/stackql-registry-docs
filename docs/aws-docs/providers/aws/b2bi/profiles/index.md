---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
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

Creates, updates, deletes or gets a <code>profile</code> resource or lists <code>profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::B2BI::Profile Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.b2bi.profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="business_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="email" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="log_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="logging" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="phone" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="profile_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="profile_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="BusinessName, Logging, Name, Phone, region" /></td>
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
List all <code>profiles</code> in a region.
```sql
SELECT
region,
profile_id
FROM aws.b2bi.profiles
WHERE region = 'us-east-1';
```
Gets all properties from a <code>profile</code>.
```sql
SELECT
region,
business_name,
created_at,
email,
log_group_name,
logging,
modified_at,
name,
phone,
profile_arn,
profile_id,
tags
FROM aws.b2bi.profiles
WHERE region = 'us-east-1' AND data__Identifier = '<ProfileId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>profile</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.b2bi.profiles (
 BusinessName,
 Logging,
 Name,
 Phone,
 region
)
SELECT 
'{{ BusinessName }}',
 '{{ Logging }}',
 '{{ Name }}',
 '{{ Phone }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.b2bi.profiles (
 BusinessName,
 Email,
 Logging,
 Name,
 Phone,
 Tags,
 region
)
SELECT 
 '{{ BusinessName }}',
 '{{ Email }}',
 '{{ Logging }}',
 '{{ Name }}',
 '{{ Phone }}',
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
  - name: profile
    props:
      - name: BusinessName
        value: '{{ BusinessName }}'
      - name: Email
        value: '{{ Email }}'
      - name: Logging
        value: '{{ Logging }}'
      - name: Name
        value: '{{ Name }}'
      - name: Phone
        value: '{{ Phone }}'
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
DELETE FROM aws.b2bi.profiles
WHERE data__Identifier = '<ProfileId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>profiles</code> resource, the following permissions are required:

### Create
```json
b2bi:CreateProfile,
b2bi:TagResource,
logs:CreateLogDelivery,
logs:CreateLogGroup,
logs:CreateLogStream,
logs:DescribeLogGroups,
logs:DescribeLogStreams,
logs:DescribeResourcePolicies,
logs:ListLogDeliveries,
logs:PutLogEvents,
logs:PutResourcePolicy
```

### Read
```json
b2bi:GetProfile,
b2bi:ListTagsForResource
```

### Update
```json
b2bi:TagResource,
b2bi:UntagResource,
b2bi:UpdateProfile
```

### Delete
```json
b2bi:DeleteProfile,
logs:DeleteLogDelivery,
logs:ListLogDeliveries
```

### List
```json
b2bi:ListProfiles
```

