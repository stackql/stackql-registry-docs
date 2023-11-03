---
title: dnssecs
hide_title: false
hide_table_of_contents: false
keywords:
  - dnssecs
  - route53
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>dnssecs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dnssecs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53.dnssecs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>HostedZoneId</code></td><td><code>string</code></td><td>The unique string (ID) used to identify a hosted zone.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.route53.dnssecs
WHERE region = 'us-east-1'
```
