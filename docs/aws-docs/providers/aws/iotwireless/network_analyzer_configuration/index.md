---
title: network_analyzer_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - network_analyzer_configuration
  - iotwireless
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


Gets or updates an individual <code>network_analyzer_configuration</code> resource, use <code>network_analyzer_configurations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_analyzer_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage NetworkAnalyzerConfiguration resource.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.network_analyzer_configuration" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the network analyzer configuration</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the new resource</td></tr>
<tr><td><CopyableCode code="trace_content" /></td><td><code>object</code></td><td>Trace content for your wireless gateway and wireless device resources</td></tr>
<tr><td><CopyableCode code="wireless_devices" /></td><td><code>array</code></td><td>List of wireless gateway resources that have been added to the network analyzer configuration</td></tr>
<tr><td><CopyableCode code="wireless_gateways" /></td><td><code>array</code></td><td>List of wireless gateway resources that have been added to the network analyzer configuration</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Arn for network analyzer configuration, Returned upon successful create.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
name,
description,
trace_content,
wireless_devices,
wireless_gateways,
arn,
tags
FROM aws.iotwireless.network_analyzer_configuration
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## Permissions

To operate on the <code>network_analyzer_configuration</code> resource, the following permissions are required:

### Read
```json
iotwireless:GetNetworkAnalyzerConfiguration,
iotwireless:ListTagsForResource
```

### Update
```json
iotwireless:UpdateNetworkAnalyzerConfiguration,
iotwireless:UntagResource,
iotwireless:ListTagsForResource
```

