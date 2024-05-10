---
title: host
hide_title: false
hide_table_of_contents: false
keywords:
  - host
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


Gets or updates an individual <code>host</code> resource, use <code>hosts</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>host</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::Host</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.host" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="host_id" /></td><td><code>string</code></td><td>ID of the host created.</td></tr>
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
host_id,
auto_placement,
availability_zone,
host_recovery,
instance_type,
instance_family,
outpost_arn,
host_maintenance,
asset_id
FROM aws.ec2.host
WHERE region = 'us-east-1' AND data__Identifier = '<HostId>';
```


## Permissions

To operate on the <code>host</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeHosts
```

### Update
```json
ec2:ModifyHosts,
ec2:DescribeHosts
```

