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
Gets an individual <code>campaign</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>campaign</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ConnectCampaigns::Campaign Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.connectcampaigns.campaign</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>connect_instance_arn</code></td><td><code>string</code></td><td>Amazon Connect Instance Arn</td></tr>
<tr><td><code>dialer_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Amazon Connect Campaign Arn</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Amazon Connect Campaign Name</td></tr>
<tr><td><code>outbound_call_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>One or more tags.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
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
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>campaign</code> resource, the following permissions are required:

### Read
```json
connect-campaigns:DescribeCampaign
```

### Delete
```json
connect-campaigns:DeleteCampaign
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

