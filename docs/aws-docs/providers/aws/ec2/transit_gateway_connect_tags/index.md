---
title: transit_gateway_connect_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_connect_tags
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

Expands all tag keys and values for <code>transit_gateway_connects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_connect_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::TransitGatewayConnect type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.transit_gateway_connect_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="transit_gateway_attachment_id" /></td><td><code>string</code></td><td>The ID of the Connect attachment.</td></tr>
<tr><td><CopyableCode code="transport_transit_gateway_attachment_id" /></td><td><code>string</code></td><td>The ID of the attachment from which the Connect attachment was created.</td></tr>
<tr><td><CopyableCode code="transit_gateway_id" /></td><td><code>string</code></td><td>The ID of the transit gateway.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the attachment.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The creation time.</td></tr>
<tr><td><CopyableCode code="options" /></td><td><code>object</code></td><td>The Connect attachment options.</td></tr>
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
Expands tags for all <code>transit_gateway_connects</code> in a region.
```sql
SELECT
region,
transit_gateway_attachment_id,
transport_transit_gateway_attachment_id,
transit_gateway_id,
state,
creation_time,
options,
tag_key,
tag_value
FROM aws.ec2.transit_gateway_connect_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>transit_gateway_connect_tags</code> resource, see <a href="/providers/aws/ec2/transit_gateway_connects/#permissions"><code>transit_gateway_connects</code></a>


