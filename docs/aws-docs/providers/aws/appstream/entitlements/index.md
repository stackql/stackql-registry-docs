---
title: entitlements
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlements
  - appstream
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>entitlements</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entitlements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>entitlements</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appstream.entitlements</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>StackName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AppVisibility</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Attributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>CreatedTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>LastModifiedTime</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.appstream.entitlements
WHERE region = 'us-east-1'
</pre>
