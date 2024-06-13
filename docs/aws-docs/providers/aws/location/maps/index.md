---
title: maps
hide_title: false
hide_table_of_contents: false
keywords:
  - maps
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

Creates, updates, deletes or gets a <code>map</code> resource or lists <code>maps</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Location::Map Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.location.maps" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="create_time" /></td><td><code>string</code></td><td>The datetime value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ss.sssZ)</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="map_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="map_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pricing_plan" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="update_time" /></td><td><code>string</code></td><td>The datetime value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ss.sssZ)</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="Configuration, MapName, region" /></td>
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
List all <code>maps</code> in a region.
```sql
SELECT
region,
map_name
FROM aws.location.maps
WHERE region = 'us-east-1';
```
Gets all properties from a <code>map</code>.
```sql
SELECT
region,
configuration,
create_time,
description,
map_arn,
map_name,
pricing_plan,
tags,
update_time,
arn
FROM aws.location.maps
WHERE region = 'us-east-1' AND data__Identifier = '<MapName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>map</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.location.maps (
 Configuration,
 MapName,
 region
)
SELECT 
'{{ Configuration }}',
 '{{ MapName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.location.maps (
 Configuration,
 Description,
 MapName,
 PricingPlan,
 Tags,
 region
)
SELECT 
 '{{ Configuration }}',
 '{{ Description }}',
 '{{ MapName }}',
 '{{ PricingPlan }}',
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
  - name: map
    props:
      - name: Configuration
        value:
          Style: '{{ Style }}'
          PoliticalView: '{{ PoliticalView }}'
          CustomLayers:
            - '{{ CustomLayers[0] }}'
      - name: Description
        value: '{{ Description }}'
      - name: MapName
        value: '{{ MapName }}'
      - name: PricingPlan
        value: '{{ PricingPlan }}'
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
DELETE FROM aws.location.maps
WHERE data__Identifier = '<MapName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>maps</code> resource, the following permissions are required:

### Create
```json
geo:CreateMap,
geo:DescribeMap,
geo:TagResource,
geo:UntagResource
```

### Read
```json
geo:DescribeMap
```

### Update
```json
geo:CreateMap,
geo:DescribeMap,
geo:TagResource,
geo:UntagResource,
geo:UpdateMap
```

### Delete
```json
geo:DeleteMap,
geo:DescribeMap
```

### List
```json
geo:ListMaps
```

