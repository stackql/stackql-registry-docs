---
title: instance_connect_endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_connect_endpoint
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>instance_connect_endpoint</code> resource, use <code>instance_connect_endpoints</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_connect_endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::InstanceConnectEndpoint</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.instance_connect_endpoint" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The id of the instance connect endpoint</td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>The subnet id of the instance connect endpoint</td></tr>
<tr><td><CopyableCode code="client_token" /></td><td><code>string</code></td><td>The client token of the instance connect endpoint.</td></tr>
<tr><td><CopyableCode code="preserve_client_ip" /></td><td><code>boolean</code></td><td>If true, the address of the instance connect endpoint client is preserved when connecting to the end resource</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags of the instance connect endpoint.</td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td>The security group IDs of the instance connect endpoint.</td></tr>
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
id,
subnet_id,
client_token,
preserve_client_ip,
tags,
security_group_ids
FROM aws.ec2.instance_connect_endpoint
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## Permissions

To operate on the <code>instance_connect_endpoint</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeInstanceConnectEndpoints
```

### Update
```json
ec2:DescribeInstanceConnectEndpoints,
ec2:CreateTags,
ec2:DeleteTags
```

