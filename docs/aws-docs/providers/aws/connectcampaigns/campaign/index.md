---
title: campaign
hide_title: false
hide_table_of_contents: false
keywords:
  - campaign
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


Gets or updates an individual <code>campaign</code> resource, use <code>campaigns</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>campaign</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ConnectCampaigns::Campaign Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connectcampaigns.campaign" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="connect_instance_arn" /></td><td><code>string</code></td><td>Amazon Connect Instance Arn</td></tr>
<tr><td><CopyableCode code="dialer_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Connect Campaign Arn</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Amazon Connect Campaign Name</td></tr>
<tr><td><CopyableCode code="outbound_call_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags.</td></tr>
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
connect_instance_arn,
dialer_config,
arn,
name,
outbound_call_config,
tags
FROM aws.connectcampaigns.campaign
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>campaign</code> resource, the following permissions are required:

### Read
```json
connect-campaigns:DescribeCampaign
```

### Update
```json
connect-campaigns:UpdateCampaignDialerConfig,
connect-campaigns:UpdateCampaignName,
connect-campaigns:UpdateCampaignOutboundCallConfig,
connect-campaigns:TagResource,
connect-campaigns:UntagResource,
connect-campaigns:DescribeCampaign
```

