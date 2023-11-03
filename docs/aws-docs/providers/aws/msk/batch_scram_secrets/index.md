---
title: batch_scram_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - batch_scram_secrets
  - msk
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>batch_scram_secrets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>batch_scram_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.msk.batch_scram_secrets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ClusterArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SecretArnList</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.msk.batch_scram_secrets
WHERE region = 'us-east-1'
```
