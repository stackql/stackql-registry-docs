---
title: campaign_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - campaign_tags
  - connectcampaignsv2
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

Expands all tag keys and values for <code>campaigns</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>campaign_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ConnectCampaignsV2::Campaign Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connectcampaignsv2.campaign_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Connect Campaign Arn</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Campaign name</td></tr>
<tr><td><CopyableCode code="connect_instance_id" /></td><td><code>string</code></td><td>Amazon Connect Instance Id</td></tr>
<tr><td><CopyableCode code="channel_subtype_config" /></td><td><code>object</code></td><td>The possible types of channel subtype config parameters</td></tr>
<tr><td><CopyableCode code="source" /></td><td><code>object</code></td><td>The possible source of the campaign</td></tr>
<tr><td><CopyableCode code="connect_campaign_flow_arn" /></td><td><code>string</code></td><td>Arn</td></tr>
<tr><td><CopyableCode code="schedule" /></td><td><code>object</code></td><td>Campaign schedule</td></tr>
<tr><td><CopyableCode code="communication_time_config" /></td><td><code>object</code></td><td>Campaign communication time config</td></tr>
<tr><td><CopyableCode code="communication_limits_override" /></td><td><code>object</code></td><td>Communication limits config</td></tr>
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
Expands tags for all <code>campaigns</code> in a region.
```sql
SELECT
region,
arn,
name,
connect_instance_id,
channel_subtype_config,
source,
connect_campaign_flow_arn,
schedule,
communication_time_config,
communication_limits_override,
tag_key,
tag_value
FROM aws.connectcampaignsv2.campaign_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>campaign_tags</code> resource, see <a href="/providers/aws/connectcampaignsv2/campaigns/#permissions"><code>campaigns</code></a>

