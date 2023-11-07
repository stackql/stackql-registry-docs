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
<tr><td><b>Id</b></td><td><code>aws.certificatemanager.account</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ExpiryEventsConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>AccountId</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.certificatemanager.account<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;AccountId&gt;'
</pre>
