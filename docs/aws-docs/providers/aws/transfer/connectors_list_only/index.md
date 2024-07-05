---
title: connectors_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors_list_only
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

Lists <code>connectors</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/connectors/"><code>connectors</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connectors_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Transfer::Connector</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.connectors_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="access_role" /></td><td><code>string</code></td><td>Specifies the access role for the connector.</td></tr>
<tr><td><CopyableCode code="as2_config" /></td><td><code>object</code></td><td>Configuration for an AS2 connector.</td></tr>
<tr><td><CopyableCode code="sftp_config" /></td><td><code>object</code></td><td>Configuration for an SFTP connector.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Specifies the unique Amazon Resource Name (ARN) for the connector.</td></tr>
<tr><td><CopyableCode code="connector_id" /></td><td><code>string</code></td><td>A unique identifier for the connector.</td></tr>
<tr><td><CopyableCode code="logging_role" /></td><td><code>string</code></td><td>Specifies the logging role for the connector.</td></tr>
<tr><td><CopyableCode code="service_managed_egress_ip_addresses" /></td><td><code>array</code></td><td>The list of egress IP addresses of this connector. These IP addresses are assigned automatically when you create the connector.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Key-value pairs that can be used to group and search for connectors. Tags are metadata attached to connectors for any purpose.</td></tr>
<tr><td><CopyableCode code="url" /></td><td><code>string</code></td><td>URL for Connector</td></tr>
<tr><td><CopyableCode code="security_policy_name" /></td><td><code>string</code></td><td>Security policy for SFTP Connector</td></tr>
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
Lists all <code>connectors</code> in a region.
```sql
SELECT
region,
connector_id
FROM aws.transfer.connectors_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>connectors_list_only</code> resource, see <a href="/providers/aws/transfer/connectors/#permissions"><code>connectors</code></a>


