---
title: api_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - api_keys
  - location
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


Used to retrieve a list of <code>api_keys</code> in a region or to create or delete a <code>api_keys</code> resource, use <code>api_key</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Location::APIKey Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.location.api_keys" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="key_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="KeyName, Restrictions, region" /></td>
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
key_name
FROM aws.location.api_keys
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>api_key</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.location.api_keys (
 KeyName,
 Restrictions,
 region
)
SELECT 
'{{ KeyName }}',
 '{{ Restrictions }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.location.api_keys (
 Description,
 ExpireTime,
 ForceUpdate,
 KeyName,
 NoExpiry,
 Restrictions,
 Tags,
 ForceDelete,
 region
)
SELECT 
 '{{ Description }}',
 '{{ ExpireTime }}',
 '{{ ForceUpdate }}',
 '{{ KeyName }}',
 '{{ NoExpiry }}',
 '{{ Restrictions }}',
 '{{ Tags }}',
 '{{ ForceDelete }}',
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
  - name: api_key
    props:
      - name: Description
        value: '{{ Description }}'
      - name: ExpireTime
        value: '{{ ExpireTime }}'
      - name: ForceUpdate
        value: '{{ ForceUpdate }}'
      - name: KeyName
        value: '{{ KeyName }}'
      - name: NoExpiry
        value: '{{ NoExpiry }}'
      - name: Restrictions
        value:
          AllowActions:
            - '{{ AllowActions[0] }}'
          AllowResources:
            - '{{ AllowResources[0] }}'
          AllowReferers:
            - '{{ AllowReferers[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: ForceDelete
        value: '{{ ForceDelete }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.location.api_keys
WHERE data__Identifier = '<KeyName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>api_keys</code> resource, the following permissions are required:

### Create
```json
geo:CreateKey,
geo:DescribeKey,
geo:TagResource,
geo:UntagResource,
geo:GetMapTile,
geo:GetMapStyleDescriptor,
geo:GetMapSprites,
geo:GetMapGlyphs,
geo:SearchPlaceIndexForText,
geo:SearchPlaceIndexForPosition,
geo:SearchPlaceIndexForSuggestions,
geo:GetPlace,
geo:CalculateRoute,
geo:CalculateRouteMatrix
```

### Delete
```json
geo:DeleteKey,
geo:DescribeKey
```

### List
```json
geo:ListKeys
```

