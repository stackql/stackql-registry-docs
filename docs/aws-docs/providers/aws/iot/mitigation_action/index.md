---
title: mitigation_action
hide_title: false
hide_table_of_contents: false
keywords:
  - mitigation_action
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>mitigation_action</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mitigation_action</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>mitigation_action</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.mitigation_action</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ActionName</code></td><td><code>string</code></td><td>A unique identifier for the mitigation action.</td></tr>
<tr><td><code>RoleArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>ActionParams</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>MitigationActionArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MitigationActionId</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iot.mitigation_action
WHERE region = 'us-east-1' AND data__Identifier = '&lt;ActionName&gt;'
</pre>
