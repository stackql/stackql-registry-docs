---
title: billing_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_groups
  - iot
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

Creates, updates, deletes or gets a <code>billing_group</code> resource or lists <code>billing_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IoT::BillingGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.billing_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="billing_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="billing_group_properties" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="region" /></td>
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
List all <code>billing_groups</code> in a region.
```sql
SELECT
region,
billing_group_name
FROM aws.iot.billing_groups
WHERE region = 'us-east-1';
```
Gets all properties from a <code>billing_group</code>.
```sql
SELECT
region,
id,
arn,
billing_group_name,
tags,
billing_group_properties
FROM aws.iot.billing_groups
WHERE region = 'us-east-1' AND data__Identifier = '<BillingGroupName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>billing_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iot.billing_groups (
 BillingGroupName,
 Tags,
 BillingGroupProperties,
 region
)
SELECT 
'{{ BillingGroupName }}',
 '{{ Tags }}',
 '{{ BillingGroupProperties }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iot.billing_groups (
 BillingGroupName,
 Tags,
 BillingGroupProperties,
 region
)
SELECT 
 '{{ BillingGroupName }}',
 '{{ Tags }}',
 '{{ BillingGroupProperties }}',
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
  - name: billing_group
    props:
      - name: BillingGroupName
        value: '{{ BillingGroupName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: BillingGroupProperties
        value:
          BillingGroupDescription: '{{ BillingGroupDescription }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iot.billing_groups
WHERE data__Identifier = '<BillingGroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>billing_groups</code> resource, the following permissions are required:

### Create
```json
iot:DescribeBillingGroup,
iot:ListTagsForResource,
iot:CreateBillingGroup,
iot:TagResource
```

### Delete
```json
iot:DescribeBillingGroup,
iot:DeleteBillingGroup
```

### List
```json
iot:ListBillingGroups,
iot:ListTagsForResource
```

### Read
```json
iot:DescribeBillingGroup,
iot:ListTagsForResource
```

### Update
```json
iot:DescribeBillingGroup,
iot:UpdateBillingGroup,
iot:ListTagsForResource,
iot:TagResource,
iot:UntagResource
```

