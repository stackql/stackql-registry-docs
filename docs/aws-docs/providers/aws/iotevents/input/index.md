---
title: input
hide_title: false
hide_table_of_contents: false
keywords:
  - input
  - iotevents
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>input</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>input</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotevents.input</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>InputDefinition</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>InputDescription</code></td><td><code>string</code></td><td>A brief description of the input.</td></tr><tr><td><code>InputName</code></td><td><code>string</code></td><td>The name of the input.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.

For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.iotevents.input
WHERE region = 'us-east-1' AND data__Identifier = '{InputName}'
```
