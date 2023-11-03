---
title: label
hide_title: false
hide_table_of_contents: false
keywords:
  - label
  - frauddetector
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>label</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>label</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.frauddetector.label</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the label.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>Tags associated with this label.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>The label description.</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>The label ARN.</td></tr><tr><td><code>CreatedTime</code></td><td><code>string</code></td><td>The timestamp when the label was created.</td></tr><tr><td><code>LastUpdatedTime</code></td><td><code>string</code></td><td>The timestamp when the label was last updated.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.frauddetector.label
WHERE region = 'us-east-1' AND data__Identifier = '{Arn}'
```
