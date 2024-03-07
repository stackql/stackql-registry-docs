---
title: network_analyzer_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - network_analyzer_configurations
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
Retrieves a list of <code>network_analyzer_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_analyzer_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>network_analyzer_configurations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotwireless.network_analyzer_configurations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the network analyzer configuration</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>network_analyzer_configurations</code> resource, the following permissions are required:

### Create
<pre>
iotwireless:CreateNetworkAnalyzerConfiguration,
iotwireless:TagResource,
iotwireless:ListTagsForResource</pre>

### List
<pre>
iotwireless:ListNetworkAnalyzerConfigurations,
iotwireless:ListTagsForResource</pre>


## Example
```sql
SELECT
region,
name
FROM awscc.iotwireless.network_analyzer_configurations
WHERE region = 'us-east-1'
```
