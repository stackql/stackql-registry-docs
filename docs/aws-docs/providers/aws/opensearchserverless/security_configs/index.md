---
title: security_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - security_configs
  - opensearchserverless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>security_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>security_configs</td></tr>
<tr><td><b>Id</b></td><td><code>aws.opensearchserverless.security_configs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>Security config description</td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>The identifier of the security config</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The friendly name of the security config</td></tr>
<tr><td><code>SamlOptions</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Type</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.opensearchserverless.security_configs<br/>WHERE region = 'us-east-1'
</pre>
