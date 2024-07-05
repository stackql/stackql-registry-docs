---
title: flow_entitlements_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_entitlements_list_only
  - mediaconnect
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

Lists <code>flow_entitlements</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/flow_entitlements/"><code>flow_entitlements</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_entitlements_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::FlowEntitlement</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediaconnect.flow_entitlements_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="flow_arn" /></td><td><code>string</code></td><td>The ARN of the flow.</td></tr>
<tr><td><CopyableCode code="entitlement_arn" /></td><td><code>string</code></td><td>The ARN of the entitlement.</td></tr>
<tr><td><CopyableCode code="data_transfer_subscriber_fee_percent" /></td><td><code>integer</code></td><td>Percentage from 0-100 of the data transfer cost to be billed to the subscriber.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the entitlement.</td></tr>
<tr><td><CopyableCode code="encryption" /></td><td><code>object</code></td><td>The type of encryption that will be used on the output that is associated with this entitlement.</td></tr>
<tr><td><CopyableCode code="entitlement_status" /></td><td><code>string</code></td><td>An indication of whether the entitlement is enabled.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the entitlement.</td></tr>
<tr><td><CopyableCode code="subscribers" /></td><td><code>array</code></td><td>The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.</td></tr>
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
Lists all <code>flow_entitlements</code> in a region.
```sql
SELECT
region,
entitlement_arn
FROM aws.mediaconnect.flow_entitlements_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>flow_entitlements_list_only</code> resource, see <a href="/providers/aws/mediaconnect/flow_entitlements/#permissions"><code>flow_entitlements</code></a>


