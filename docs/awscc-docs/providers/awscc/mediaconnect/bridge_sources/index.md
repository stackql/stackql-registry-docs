---
title: bridge_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - bridge_sources
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
Retrieves a list of <code>bridge_sources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bridge_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>bridge_sources</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mediaconnect.bridge_sources</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>bridge_arn</code></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of the bridge.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the source.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>bridge_sources</code> resource, the following permissions are required:

### Create
<pre>
mediaconnect:AddBridgeSources,
mediaconnect:DescribeBridge</pre>


## Example
```sql
SELECT
region,
bridge_arn,
name
FROM awscc.mediaconnect.bridge_sources
WHERE region = 'us-east-1'
```
