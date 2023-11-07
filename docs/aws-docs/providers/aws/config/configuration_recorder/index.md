---
title: configuration_recorder
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_recorder
  - config
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>configuration_recorder</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_recorder</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>configuration_recorder</td></tr>
<tr><td><b>Id</b></td><td><code>aws.config.configuration_recorder</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RecordingGroup</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>RoleARN</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.config.configuration_recorder<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>
