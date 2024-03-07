---
title: signing_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - signing_profiles
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
Retrieves a list of <code>signing_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>signing_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>signing_profiles</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.signer.signing_profiles</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>undefined</code></td><td>The Amazon Resource Name (ARN) of the specified signing profile.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>signing_profiles</code> resource, the following permissions are required:

### Create
<pre>
signer:PutSigningProfile,
signer:TagResource</pre>

### List
<pre>
signer:ListSigningProfiles</pre>


## Example
```sql
SELECT
region,
arn
FROM awscc.signer.signing_profiles
WHERE region = 'us-east-1'
```