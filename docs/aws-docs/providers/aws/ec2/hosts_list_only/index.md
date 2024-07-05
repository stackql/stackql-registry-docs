---
title: hosts_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - hosts_list_only
  - ec2
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

Lists <code>hosts</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/hosts/"><code>hosts</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hosts_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::Host</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.hosts_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="host_id" /></td><td><code>string</code></td><td>ID of the host created.</td></tr>
<tr><td><CopyableCode code="auto_placement" /></td><td><code>string</code></td><td>Indicates whether the host accepts any untargeted instance launches that match its instance type configuration, or if it only accepts Host tenancy instance launches that specify its unique host ID.</td></tr>
<tr><td><CopyableCode code="availability_zone" /></td><td><code>string</code></td><td>The Availability Zone in which to allocate the Dedicated Host.</td></tr>
<tr><td><CopyableCode code="host_recovery" /></td><td><code>string</code></td><td>Indicates whether to enable or disable host recovery for the Dedicated Host. Host recovery is disabled by default.</td></tr>
<tr><td><CopyableCode code="instance_type" /></td><td><code>string</code></td><td>Specifies the instance type to be supported by the Dedicated Hosts. If you specify an instance type, the Dedicated Hosts support instances of the specified instance type only.</td></tr>
<tr><td><CopyableCode code="instance_family" /></td><td><code>string</code></td><td>Specifies the instance family to be supported by the Dedicated Hosts. If you specify an instance family, the Dedicated Hosts support multiple instance types within that instance family.</td></tr>
<tr><td><CopyableCode code="outpost_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon Web Services Outpost on which to allocate the Dedicated Host.</td></tr>
<tr><td><CopyableCode code="host_maintenance" /></td><td><code>string</code></td><td>Automatically allocates a new dedicated host and moves your instances on to it if a degradation is detected on your current host.</td></tr>
<tr><td><CopyableCode code="asset_id" /></td><td><code>string</code></td><td>The ID of the Outpost hardware asset.</td></tr>
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
Lists all <code>hosts</code> in a region.
```sql
SELECT
region,
host_id
FROM aws.ec2.hosts_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>hosts_list_only</code> resource, see <a href="/providers/aws/ec2/hosts/#permissions"><code>hosts</code></a>


