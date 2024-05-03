---
title: static_ips
hide_title: false
hide_table_of_contents: false
keywords:
  - static_ips
  - lightsail
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

Used to retrieve a list of <code>static_ips</code> in a region or create a <code>static_ips</code> resource, use <code>static_ip</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>static_ips</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::StaticIp</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.static_ips" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="static_ip_name" /></td><td><code>string</code></td><td>The name of the static IP address.</td></tr>
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
static_ip_name
FROM aws.lightsail.static_ips
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>static_ips</code> resource, the following permissions are required:

### Create
```json
lightsail:AllocateStaticIp,
lightsail:AttachStaticIp,
lightsail:DetachStaticIp,
lightsail:GetInstance,
lightsail:GetStaticIp,
lightsail:GetStaticIps
```

### List
```json
lightsail:GetStaticIps
```

