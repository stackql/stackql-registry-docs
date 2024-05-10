---
title: route_calculators
hide_title: false
hide_table_of_contents: false
keywords:
  - route_calculators
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


Used to retrieve a list of <code>route_calculators</code> in a region or to create or delete a <code>route_calculators</code> resource, use <code>route_calculator</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>route_calculators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Location::RouteCalculator Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.location.route_calculators" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="calculator_name" /></td><td><code>string</code></td><td></td></tr>
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
calculator_name
FROM aws.location.route_calculators
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
 "CalculatorName": "{{ CalculatorName }}",
 "DataSource": "{{ DataSource }}"
}
>>>
--required properties only
INSERT INTO aws.location.route_calculators (
 CalculatorName,
 DataSource,
 region
)
SELECT 
{{ CalculatorName }},
 {{ DataSource }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "CalculatorName": "{{ CalculatorName }}",
 "DataSource": "{{ DataSource }}",
 "Description": "{{ Description }}",
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
INSERT INTO aws.location.route_calculators (
 CalculatorName,
 DataSource,
 Description,
 PricingPlan,
 Tags,
 region
)
SELECT 
 {{ CalculatorName }},
 {{ DataSource }},
 {{ Description }},
 {{ PricingPlan }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.location.route_calculators
WHERE data__Identifier = '<CalculatorName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>route_calculators</code> resource, the following permissions are required:

### Create
```json
geo:CreateRouteCalculator,
geo:DescribeRouteCalculator,
geo:TagResource,
geo:UntagResource
```

### Delete
```json
geo:DeleteRouteCalculator,
geo:DescribeRouteCalculator
```

### List
```json
geo:ListRouteCalculators
```

