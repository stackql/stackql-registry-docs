---
title: configuration_set
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_set
  - ses
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>configuration_set</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>configuration_set</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ses.configuration_set</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the configuration set.</td></tr>
<tr><td><code>tracking_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>delivery_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>reputation_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>sending_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>suppression_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>vdm_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
tracking_options,
delivery_options,
reputation_options,
sending_options,
suppression_options,
vdm_options
FROM aws.ses.configuration_set
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Name&gt;'
```
