---
title: instance_connect_endpoint_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_connect_endpoint_tags
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

Expands all tag keys and values for <code>instance_connect_endpoints</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_connect_endpoint_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::InstanceConnectEndpoint</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.instance_connect_endpoint_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The id of the instance connect endpoint</td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>The subnet id of the instance connect endpoint</td></tr>
<tr><td><CopyableCode code="client_token" /></td><td><code>string</code></td><td>The client token of the instance connect endpoint.</td></tr>
<tr><td><CopyableCode code="preserve_client_ip" /></td><td><code>boolean</code></td><td>If true, the address of the instance connect endpoint client is preserved when connecting to the end resource</td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td>The security group IDs of the instance connect endpoint.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>instance_connect_endpoints</code> in a region.
```sql
SELECT
region,
id,
subnet_id,
client_token,
preserve_client_ip,
security_group_ids,
tag_key,
tag_value
FROM aws.ec2.instance_connect_endpoint_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>instance_connect_endpoint_tags</code> resource, see <a href="/providers/aws/ec2/instance_connect_endpoints/#permissions"><code>instance_connect_endpoints</code></a>

