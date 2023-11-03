---
title: agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - agreements
  - transfer
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>agreements</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agreements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.transfer.agreements</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>A textual description for the agreement.</td></tr><tr><td><code>ServerId</code></td><td><code>string</code></td><td>A unique identifier for the server.</td></tr><tr><td><code>LocalProfileId</code></td><td><code>string</code></td><td>A unique identifier for the local profile.</td></tr><tr><td><code>PartnerProfileId</code></td><td><code>string</code></td><td>A unique identifier for the partner profile.</td></tr><tr><td><code>BaseDirectory</code></td><td><code>string</code></td><td>Specifies the base directory for the agreement.</td></tr><tr><td><code>AccessRole</code></td><td><code>string</code></td><td>Specifies the access role for the agreement.</td></tr><tr><td><code>Status</code></td><td><code>string</code></td><td>Specifies the status of the agreement.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>Key-value pairs that can be used to group and search for agreements. Tags are metadata attached to agreements for any purpose.</td></tr><tr><td><code>AgreementId</code></td><td><code>string</code></td><td>A unique identifier for the agreement.</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>Specifies the unique Amazon Resource Name (ARN) for the agreement.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.transfer.agreements
WHERE region = 'us-east-1'
</pre>
