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


Used to retrieve a list of <code>maps</code> in a region or to create or delete a <code>maps</code> resource, use <code>map</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Location::Map Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.location.maps" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="map_name" /></td><td><code>string</code></td><td></td></tr>
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
map_name
FROM aws.location.maps
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
 "Configuration": {
  "Style": "{{ Style }}",
  "PoliticalView": "{{ PoliticalView }}",
  "CustomLayers": [
   "{{ CustomLayers[0] }}"
  ]
 },
 "MapName": "{{ MapName }}"
}
>>>
--required properties only
INSERT INTO aws.location.maps (
 Configuration,
 MapName,
 region
)
SELECT 
{{ .Configuration }},
 {{ .MapName }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Configuration": {
  "Style": "{{ Style }}",
  "PoliticalView": "{{ PoliticalView }}",
  "CustomLayers": [
   "{{ CustomLayers[0] }}"
  ]
 },
 "Description": "{{ Description }}",
 "MapName": "{{ MapName }}",
 "PricingPlan": "{{ PricingPlan }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.location.maps (
 Configuration,
 Description,
 MapName,
 PricingPlan,
 Tags,
 region
)
SELECT 
 {{ .Configuration }},
 {{ .Description }},
 {{ .MapName }},
 {{ .PricingPlan }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
geo:DeleteMap,
geo:DescribeMap
```

### List
```json
geo:ListMaps
```

