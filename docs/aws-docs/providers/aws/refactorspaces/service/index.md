---
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
  - refactorspaces
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>service</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.refactorspaces.service</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ApplicationIdentifier</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr><tr><td><code>EndpointType</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>EnvironmentIdentifier</code></td><td><code>string</code></td><td></td></tr><tr><td><code>LambdaEndpoint</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ServiceIdentifier</code></td><td><code>string</code></td><td></td></tr><tr><td><code>UrlEndpoint</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>VpcId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.refactorspaces.service
WHERE region = 'us-east-1' AND data__Identifier = '{EnvironmentIdentifier}' AND data__Identifier = '{ApplicationIdentifier}' AND data__Identifier = '{ServiceIdentifier}'
</pre>
