---
title: simple_ads
hide_title: false
hide_table_of_contents: false
keywords:
  - simple_ads
  - directoryservice
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

Used to retrieve a list of <code>simple_ads</code> in a region or create a <code>simple_ads</code> resource, use <code>simple_ad</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>simple_ads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::DirectoryService::SimpleAD</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.directoryservice.simple_ads" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="directory_id" /></td><td><code>string</code></td><td>The unique identifier for a directory.</td></tr>
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
directory_id
FROM aws.directoryservice.simple_ads
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>simple_ads</code> resource, the following permissions are required:

### Create
```json
ds:CreateDirectory,
ds:CreateAlias,
ds:EnableSso,
ds:DescribeDirectories,
ec2:DescribeSubnets,
ec2:DescribeVpcs,
ec2:CreateSecurityGroup,
ec2:CreateNetworkInterface,
ec2:DescribeNetworkInterfaces,
ec2:AuthorizeSecurityGroupIngress,
ec2:AuthorizeSecurityGroupEgress,
ec2:CreateTags
```

### List
```json
ds:DescribeDirectories
```

