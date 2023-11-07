---
title: integration_association
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_association
  - connect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>integration_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.connect.integration_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>IntegrationAssociationId</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>InstanceId</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>IntegrationArn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>IntegrationType</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.connect.integration_association
WHERE region = 'us-east-1' AND data__Identifier = '&lt;InstanceId&gt;' AND data__Identifier = '&lt;IntegrationType&gt;' AND data__Identifier = '&lt;IntegrationArn&gt;'
</pre>
