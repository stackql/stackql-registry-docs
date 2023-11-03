---
title: profile_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - profile_permissions
  - signer
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>profile_permissions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profile_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.signer.profile_permissions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ProfileName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ProfileVersion</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Action</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Principal</code></td><td><code>string</code></td><td></td></tr><tr><td><code>StatementId</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.signer.profile_permissions
WHERE region = 'us-east-1'
</pre>
