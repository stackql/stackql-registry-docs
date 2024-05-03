---
title: dedicated_ip_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_ip_pools
  - ses
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

Used to retrieve a list of <code>dedicated_ip_pools</code> in a region or create a <code>dedicated_ip_pools</code> resource, use <code>dedicated_ip_pool</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dedicated_ip_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SES::DedicatedIpPool</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ses.dedicated_ip_pools" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="pool_name" /></td><td><code>string</code></td><td>The name of the dedicated IP pool.</td></tr>
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
pool_name
FROM aws.ses.dedicated_ip_pools
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>dedicated_ip_pools</code> resource, the following permissions are required:

### Create
```json
ses:CreateDedicatedIpPool,
ses:GetDedicatedIpPool,
ses:GetDedicatedIps
```

### List
```json
ses:ListDedicatedIpPools
```

