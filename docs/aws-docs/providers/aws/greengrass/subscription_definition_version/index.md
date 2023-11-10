---
title: subscription_definition_version
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_definition_version
  - greengrass
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>subscription_definition_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscription_definition_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>subscription_definition_version</td></tr>
<tr><td><b>Id</b></td><td><code>aws.greengrass.subscription_definition_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subscription_definition_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subscriptions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
subscription_definition_id,
subscriptions
FROM aws.greengrass.subscription_definition_version
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
