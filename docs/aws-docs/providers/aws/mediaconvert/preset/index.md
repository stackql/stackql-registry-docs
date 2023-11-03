---
title: preset
hide_title: false
hide_table_of_contents: false
keywords:
  - preset
  - mediaconvert
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>preset</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>preset</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mediaconvert.preset</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Category</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SettingsJson</code></td><td><code>object</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>object</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.mediaconvert.preset
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
```
