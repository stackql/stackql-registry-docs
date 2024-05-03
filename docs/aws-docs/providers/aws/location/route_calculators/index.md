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

Used to retrieve a list of <code>route_calculators</code> in a region or create a <code>route_calculators</code> resource, use <code>route_calculator</code> to operate on an individual resource.

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
WHERE region = 'us-east-1'
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

### List
```json
geo:ListRouteCalculators
```

