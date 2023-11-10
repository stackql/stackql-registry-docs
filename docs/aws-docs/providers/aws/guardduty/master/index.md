---
title: master
hide_title: false
hide_table_of_contents: false
keywords:
  - master
  - guardduty
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>master</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>master</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>master</td></tr>
<tr><td><b>Id</b></td><td><code>aws.guardduty.master</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>detector_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>master_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>invitation_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
detector_id,
master_id,
invitation_id
FROM aws.guardduty.master
WHERE region = 'us-east-1'
AND data__Identifier = '<MasterId>'
```
