---
title: account
hide_title: false
hide_table_of_contents: false
keywords:
  - account
  - certificatemanager
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>account</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>account</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.certificatemanager.account</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>expiry_events_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>account</code> resource, the following permissions are required:

### Read
<pre>
acm:GetAccountConfiguration</pre>

### Update
<pre>
acm:GetAccountConfiguration,
acm:PutAccountConfiguration</pre>

### Delete
<pre>
acm:GetAccountConfiguration,
acm:PutAccountConfiguration</pre>


## Example
```sql
SELECT
region,
expiry_events_configuration,
account_id
FROM awscc.certificatemanager.account
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AccountId&gt;'
```
