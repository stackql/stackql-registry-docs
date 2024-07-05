---
title: network_interface_attachments_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - network_interface_attachments_list_only
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

Lists <code>network_interface_attachments</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/network_interface_attachments/"><code>network_interface_attachments</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_interface_attachments_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::NetworkInterfaceAttachment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.network_interface_attachments_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="attachment_id" /></td><td><code>string</code></td><td>The ID of the network interface attachment.</td></tr>
<tr><td><CopyableCode code="delete_on_termination" /></td><td><code>boolean</code></td><td>Whether to delete the network interface when the instance terminates. By default, this value is set to true.</td></tr>
<tr><td><CopyableCode code="device_index" /></td><td><code>string</code></td><td>The network interface's position in the attachment order. For example, the first attached network interface has a DeviceIndex of 0.</td></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>string</code></td><td>The ID of the instance to which you will attach the ENI.</td></tr>
<tr><td><CopyableCode code="network_interface_id" /></td><td><code>string</code></td><td>The ID of the ENI that you want to attach.</td></tr>
<tr><td><CopyableCode code="ena_srd_specification" /></td><td><code>object</code></td><td></td></tr>
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
Lists all <code>network_interface_attachments</code> in a region.
```sql
SELECT
region,
attachment_id
FROM aws.ec2.network_interface_attachments_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>network_interface_attachments_list_only</code> resource, see <a href="/providers/aws/ec2/network_interface_attachments/#permissions"><code>network_interface_attachments</code></a>


