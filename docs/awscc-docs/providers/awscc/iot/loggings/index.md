---
title: loggings
hide_title: false
hide_table_of_contents: false
keywords:
  - loggings
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>loggings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>loggings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>loggings</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iot.loggings</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>account_id</code></td><td><code>string</code></td><td>Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>loggings</code> resource, the following permissions are required:

### Create
<pre>
iot:SetV2LoggingOptions,
iot:GetV2LoggingOptions,
iam:PassRole</pre>

### List
<pre>
iot:GetV2LoggingOptions</pre>


## Example
```sql
SELECT
region,
account_id
FROM awscc.iot.loggings
WHERE region = 'us-east-1'
```
