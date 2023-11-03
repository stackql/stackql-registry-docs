---
title: dedicated_ip_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_ip_pools
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
Retrieves a list of <code>dedicated_ip_pools</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dedicated_ip_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ses.dedicated_ip_pools</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>PoolName</code></td><td><code>string</code></td><td>The name of the dedicated IP pool.</td></tr><tr><td><code>ScalingMode</code></td><td><code>string</code></td><td>Specifies whether the dedicated IP pool is managed or not. The default value is STANDARD.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.ses.dedicated_ip_pools
WHERE region = 'us-east-1'
```
