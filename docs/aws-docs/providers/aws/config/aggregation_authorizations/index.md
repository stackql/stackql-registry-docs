---
title: aggregation_authorizations
hide_title: false
hide_table_of_contents: false
keywords:
  - aggregation_authorizations
  - config
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

Used to retrieve a list of <code>aggregation_authorizations</code> in a region or create a <code>aggregation_authorizations</code> resource, use <code>aggregation_authorization</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aggregation_authorizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Config::AggregationAuthorization</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.config.aggregation_authorizations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="authorized_account_id" /></td><td><code>string</code></td><td>The 12-digit account ID of the account authorized to aggregate data.</td></tr>
<tr><td><CopyableCode code="authorized_aws_region" /></td><td><code>string</code></td><td>The region authorized to collect aggregated data.</td></tr>
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
authorized_account_id,
authorized_aws_region
FROM aws.config.aggregation_authorizations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>aggregation_authorizations</code> resource, the following permissions are required:

### Create
```json
config:DescribeAggregationAuthorizations,
config:PutAggregationAuthorization,
config:TagResource
```

### List
```json
config:DescribeAggregationAuthorizations
```

