---
title: flows_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - flows_list_only
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

Lists <code>flows</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/flows/"><code>flows</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flows_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::Flow</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediaconnect.flows_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="flow_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.</td></tr>
<tr><td><CopyableCode code="egress_ip" /></td><td><code>string</code></td><td>The IP address from which video will be sent to output destinations.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the flow.</td></tr>
<tr><td><CopyableCode code="availability_zone" /></td><td><code>string</code></td><td>The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.</td></tr>
<tr><td><CopyableCode code="flow_availability_zone" /></td><td><code>string</code></td><td>The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.(ReadOnly)</td></tr>
<tr><td><CopyableCode code="source" /></td><td><code>object</code></td><td>The source of the flow.</td></tr>
<tr><td><CopyableCode code="source_failover_config" /></td><td><code>object</code></td><td>The source failover config of the flow.</td></tr>
<tr><td><CopyableCode code="vpc_interfaces" /></td><td><code>array</code></td><td>The VPC interfaces that you added to this flow.</td></tr>
<tr><td><CopyableCode code="media_streams" /></td><td><code>array</code></td><td>The media streams associated with the flow. You can associate any of these media streams with sources and outputs on the flow.</td></tr>
<tr><td><CopyableCode code="maintenance" /></td><td><code>object</code></td><td>The maintenance settings you want to use for the flow.</td></tr>
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
Lists all <code>flows</code> in a region.
```sql
SELECT
region,
flow_arn
FROM aws.mediaconnect.flows_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>flows_list_only</code> resource, see <a href="/providers/aws/mediaconnect/flows/#permissions"><code>flows</code></a>


