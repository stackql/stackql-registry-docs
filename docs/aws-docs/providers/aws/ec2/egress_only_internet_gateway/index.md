---
title: egress_only_internet_gateway
hide_title: false
hide_table_of_contents: false
keywords:
  - egress_only_internet_gateway
  - ec2
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

Gets or operates on an individual <code>egress_only_internet_gateway</code> resource, use <code>egress_only_internet_gateways</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>egress_only_internet_gateway</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::EgressOnlyInternetGateway</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.egress_only_internet_gateway" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Service Generated ID of the EgressOnlyInternetGateway</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC for which to create the egress-only internet gateway.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id,
vpc_id
FROM aws.ec2.egress_only_internet_gateway
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>egress_only_internet_gateway</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeEgressOnlyInternetGateways
```

### Delete
```json
ec2:DeleteEgressOnlyInternetGateway,
ec2:DescribeEgressOnlyInternetGateways,
ec2:DescribeVpcs
```
