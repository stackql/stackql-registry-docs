---
title: campaign_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - campaign_tags
  - connectcampaigns
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
<tr><td><b>Description</b></td><td>Definition of AWS::ConnectCampaigns::Campaign Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connectcampaigns.campaign_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="connect_instance_arn" /></td><td><code>string</code></td><td>Amazon Connect Instance Arn</td></tr>
<tr><td><CopyableCode code="dialer_config" /></td><td><code>object</code></td><td>The possible types of dialer config parameters</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Connect Campaign Arn</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Amazon Connect Campaign Name</td></tr>
<tr><td><CopyableCode code="outbound_call_config" /></td><td><code>object</code></td><td>The configuration used for outbound calls.</td></tr>
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
connect_instance_arn,
dialer_config,
arn,
name,
outbound_call_config,
tag_key,
tag_value
FROM aws.connectcampaigns.campaign_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>campaign_tags</code> resource, see <a href="/providers/aws/connectcampaigns/campaigns/#permissions"><code>campaigns</code></a>


