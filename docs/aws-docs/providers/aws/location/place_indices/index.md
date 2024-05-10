---
title: place_indices
hide_title: false
hide_table_of_contents: false
keywords:
  - place_indices
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


Used to retrieve a list of <code>place_indices</code> in a region or to create or delete a <code>place_indices</code> resource, use <code>place_index</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>place_indices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Location::PlaceIndex Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.location.place_indices" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="index_name" /></td><td><code>string</code></td><td></td></tr>
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
index_name
FROM aws.location.place_indices
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
 "DataSource": "{{ DataSource }}",
 "IndexName": "{{ IndexName }}"
}
>>>
--required properties only
INSERT INTO aws.location.place_indices (
 DataSource,
 IndexName,
 region
)
SELECT 
{{ DataSource }},
 {{ IndexName }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DataSource": "{{ DataSource }}",
 "DataSourceConfiguration": {
  "IntendedUse": "{{ IntendedUse }}"
 },
 "Description": "{{ Description }}",
 "IndexName": "{{ IndexName }}",
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
INSERT INTO aws.location.place_indices (
 DataSource,
 DataSourceConfiguration,
 Description,
 IndexName,
 PricingPlan,
 Tags,
 region
)
SELECT 
 {{ DataSource }},
 {{ DataSourceConfiguration }},
 {{ Description }},
 {{ IndexName }},
 {{ PricingPlan }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.location.place_indices
WHERE data__Identifier = '<IndexName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>place_indices</code> resource, the following permissions are required:

### Create
```json
geo:CreatePlaceIndex,
geo:DescribePlaceIndex,
geo:TagResource,
geo:UntagResource
```

### Delete
```json
geo:DeletePlaceIndex,
geo:DescribePlaceIndex
```

### List
```json
geo:ListPlaceIndexes
```

