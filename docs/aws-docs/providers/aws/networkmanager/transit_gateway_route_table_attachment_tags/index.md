---
title: transit_gateway_route_table_attachment_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_route_table_attachment_tags
  - networkmanager
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

Expands all tag keys and values for <code>transit_gateway_route_table_attachments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_route_table_attachment_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::NetworkManager::TransitGatewayRouteTableAttachment Resource Type definition.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.transit_gateway_route_table_attachment_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="peering_id" /></td><td><code>string</code></td><td>The Id of peering between transit gateway and core network.</td></tr>
<tr><td><CopyableCode code="transit_gateway_route_table_arn" /></td><td><code>string</code></td><td>The Arn of transit gateway route table.</td></tr>
<tr><td><CopyableCode code="core_network_id" /></td><td><code>string</code></td><td>The ID of a core network where you're creating a site-to-site VPN attachment.</td></tr>
<tr><td><CopyableCode code="core_network_arn" /></td><td><code>string</code></td><td>The ARN of a core network for the VPC attachment.</td></tr>
<tr><td><CopyableCode code="attachment_id" /></td><td><code>string</code></td><td>The ID of the attachment.</td></tr>
<tr><td><CopyableCode code="owner_account_id" /></td><td><code>string</code></td><td>Owner account of the attachment.</td></tr>
<tr><td><CopyableCode code="attachment_type" /></td><td><code>string</code></td><td>The type of attachment.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the attachment.</td></tr>
<tr><td><CopyableCode code="edge_location" /></td><td><code>string</code></td><td>The Region where the edge is located.</td></tr>
<tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td>The ARN of the Resource.</td></tr>
<tr><td><CopyableCode code="attachment_policy_rule_number" /></td><td><code>integer</code></td><td>The policy rule number associated with the attachment.</td></tr>
<tr><td><CopyableCode code="segment_name" /></td><td><code>string</code></td><td>The name of the segment that attachment is in.</td></tr>
<tr><td><CopyableCode code="proposed_segment_change" /></td><td><code>object</code></td><td>The attachment to move from one segment to another.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Creation time of the attachment.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>Last update time of the attachment.</td></tr>
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
Expands tags for all <code>transit_gateway_route_table_attachments</code> in a region.
```sql
SELECT
region,
peering_id,
transit_gateway_route_table_arn,
core_network_id,
core_network_arn,
attachment_id,
owner_account_id,
attachment_type,
state,
edge_location,
resource_arn,
attachment_policy_rule_number,
segment_name,
proposed_segment_change,
created_at,
updated_at,
tag_key,
tag_value
FROM aws.networkmanager.transit_gateway_route_table_attachment_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>transit_gateway_route_table_attachment_tags</code> resource, see <a href="/providers/aws/networkmanager/transit_gateway_route_table_attachments/#permissions"><code>transit_gateway_route_table_attachments</code></a>


