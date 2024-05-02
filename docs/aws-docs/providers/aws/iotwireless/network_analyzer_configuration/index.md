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
Gets or operates on an individual <code>network_analyzer_configuration</code> resource, use <code>network_analyzer_configurations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_analyzer_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage NetworkAnalyzerConfiguration resource.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotwireless.network_analyzer_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the network analyzer configuration</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the new resource</td></tr>
<tr><td><code>trace_content</code></td><td><code>object</code></td><td>Trace content for your wireless gateway and wireless device resources</td></tr>
<tr><td><code>wireless_devices</code></td><td><code>array</code></td><td>List of wireless gateway resources that have been added to the network analyzer configuration</td></tr>
<tr><td><code>wireless_gateways</code></td><td><code>array</code></td><td>List of wireless gateway resources that have been added to the network analyzer configuration</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Arn for network analyzer configuration, Returned upon successful create.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
name,
description,
trace_content,
wireless_devices,
wireless_gateways,
arn,
tags
FROM aws.iotwireless.network_analyzer_configuration
WHERE data__Identifier = '<Name>';
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

### Delete
```json
iotwireless:DeleteNetworkAnalyzerConfiguration
```

