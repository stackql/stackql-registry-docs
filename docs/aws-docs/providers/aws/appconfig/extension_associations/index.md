---
title: extension_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - extension_associations
  - appconfig
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>extension_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>extension_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>extension_associations</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appconfig.extension_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ExtensionArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ResourceArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ExtensionIdentifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ResourceIdentifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ExtensionVersionNumber</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>Parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.appconfig.extension_associations<br/>WHERE region = 'us-east-1'
</pre>
