---
title: server_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - server_tags
  - transfer
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

Expands all tag keys and values for <code>servers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Transfer::Server Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.server_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="as2_service_managed_egress_ip_addresses" /></td><td><code>array</code></td><td>The list of egress IP addresses of this server. These IP addresses are only relevant for servers that use the AS2 protocol. They are used for sending asynchronous MDNs. These IP addresses are assigned automatically when you create an AS2 server. Additionally, if you update an existing server and add the AS2 protocol, static IP addresses are assigned as well.</td></tr>
<tr><td><CopyableCode code="certificate" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_details" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_provider_details" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_provider_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="logging_role" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="post_authentication_login_banner" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pre_authentication_login_banner" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="protocol_details" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="protocols" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="s3_storage_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="security_policy_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="server_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="structured_log_destinations" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="workflow_details" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>servers</code> in a region.
```sql
SELECT
region,
arn,
as2_service_managed_egress_ip_addresses,
certificate,
domain,
endpoint_details,
endpoint_type,
identity_provider_details,
identity_provider_type,
logging_role,
post_authentication_login_banner,
pre_authentication_login_banner,
protocol_details,
protocols,
s3_storage_options,
security_policy_name,
server_id,
state,
structured_log_destinations,
workflow_details,
tag_key,
tag_value
FROM aws.transfer.server_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>server_tags</code> resource, see <a href="/providers/aws/transfer/servers/#permissions"><code>servers</code></a>

