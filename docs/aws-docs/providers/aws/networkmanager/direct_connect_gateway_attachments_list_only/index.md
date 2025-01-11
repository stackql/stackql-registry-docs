---
title: direct_connect_gateway_attachments_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - direct_connect_gateway_attachments_list_only
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

Lists <code>direct_connect_gateway_attachments</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/direct_connect_gateway_attachments/"><code>direct_connect_gateway_attachments</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>direct_connect_gateway_attachments_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::NetworkManager::DirectConnectGatewayAttachment Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.direct_connect_gateway_attachments_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="attachment_id" /></td><td><code>string</code></td><td>Id of the attachment.</td></tr>
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
Lists all <code>direct_connect_gateway_attachments</code> in a region.
```sql
SELECT
region,
attachment_id
FROM aws.networkmanager.direct_connect_gateway_attachments_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>direct_connect_gateway_attachments_list_only</code> resource, see <a href="/providers/aws/networkmanager/direct_connect_gateway_attachments/#permissions"><code>direct_connect_gateway_attachments</code></a>

