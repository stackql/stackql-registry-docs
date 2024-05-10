---
title: static_ip
hide_title: false
hide_table_of_contents: false
keywords:
  - static_ip
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>static_ip</code> resource, use <code>static_ips</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>static_ip</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::StaticIp</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.static_ip" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="static_ip_name" /></td><td><code>string</code></td><td>The name of the static IP address.</td></tr>
<tr><td><CopyableCode code="attached_to" /></td><td><code>string</code></td><td>The instance where the static IP is attached.</td></tr>
<tr><td><CopyableCode code="is_attached" /></td><td><code>boolean</code></td><td>A Boolean value indicating whether the static IP is attached.</td></tr>
<tr><td><CopyableCode code="ip_address" /></td><td><code>string</code></td><td>The static IP address.</td></tr>
<tr><td><CopyableCode code="static_ip_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
static_ip_name,
attached_to,
is_attached,
ip_address,
static_ip_arn
FROM aws.lightsail.static_ip
WHERE region = 'us-east-1' AND data__Identifier = '<StaticIpName>';
```


## Permissions

To operate on the <code>static_ip</code> resource, the following permissions are required:

### Read
```json
lightsail:GetStaticIp,
lightsail:GetStaticIps
```

### Update
```json
lightsail:AttachStaticIp,
lightsail:DetachStaticIp,
lightsail:GetInstance,
lightsail:GetStaticIp,
lightsail:GetStaticIps
```

