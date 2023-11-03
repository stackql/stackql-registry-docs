---
title: simulation
hide_title: false
hide_table_of_contents: false
keywords:
  - simulation
  - simspaceweaver
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>simulation</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>simulation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.simspaceweaver.simulation</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the simulation.</td></tr><tr><td><code>RoleArn</code></td><td><code>string</code></td><td>Role ARN.</td></tr><tr><td><code>SchemaS3Location</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DescribePayload</code></td><td><code>string</code></td><td>Json object with all simulation details</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.simspaceweaver.simulation
WHERE region = 'us-east-1' AND data__Identifier = '{Name}'
</pre>
