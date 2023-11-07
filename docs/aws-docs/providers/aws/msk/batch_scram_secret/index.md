---
title: batch_scram_secret
hide_title: false
hide_table_of_contents: false
keywords:
  - batch_scram_secret
  - msk
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>batch_scram_secret</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>batch_scram_secret</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.msk.batch_scram_secret</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ClusterArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SecretArnList</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.msk.batch_scram_secret
WHERE region = 'us-east-1' AND data__Identifier = '&lt;ClusterArn&gt;'
</pre>
