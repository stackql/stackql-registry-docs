---
title: user_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - user_profiles
  - opsworks
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>user_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>user_profiles</td></tr>
<tr><td><b>Id</b></td><td><code>aws.opsworks.user_profiles</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SshUsername</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AllowSelfManagement</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>IamUserArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SshPublicKey</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.opsworks.user_profiles<br/>WHERE region = 'us-east-1'
</pre>
