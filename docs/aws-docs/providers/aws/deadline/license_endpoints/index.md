---
title: license_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - license_endpoints
  - deadline
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

Used to retrieve a list of <code>license_endpoints</code> in a region or create a <code>license_endpoints</code> resource, use <code>license_endpoint</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>license_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::LicenseEndpoint Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.deadline.license_endpoints" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
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
arn
FROM aws.deadline.license_endpoints
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>license_endpoints</code> resource, the following permissions are required:

### Create
```json
deadline:CreateLicenseEndpoint,
deadline:GetLicenseEndpoint,
ec2:CreateTags,
ec2:CreateVpcEndpoint,
ec2:DescribeVpcEndpoints
```

### List
```json
deadline:ListLicenseEndpoints
```

