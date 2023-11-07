---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
  - emrserverless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>application</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>application</td></tr>
<tr><td><b>Id</b></td><td><code>aws.emrserverless.application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Architecture</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>User friendly Application name.</td></tr>
<tr><td><code>ReleaseLabel</code></td><td><code>string</code></td><td>EMR release label.</td></tr>
<tr><td><code>Type</code></td><td><code>string</code></td><td>The type of the application</td></tr>
<tr><td><code>InitialCapacity</code></td><td><code>array</code></td><td>Initial capacity initialized when an Application is started.</td></tr>
<tr><td><code>MaximumCapacity</code></td><td><code>object</code></td><td>Maximum allowed cumulative resources for an Application. No new resources will be created once the limit is hit.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>Tag map with key and value</td></tr>
<tr><td><code>AutoStartConfiguration</code></td><td><code>object</code></td><td>Configuration for Auto Start of Application.</td></tr>
<tr><td><code>AutoStopConfiguration</code></td><td><code>object</code></td><td>Configuration for Auto Stop of Application.</td></tr>
<tr><td><code>ImageConfiguration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>NetworkConfiguration</code></td><td><code>object</code></td><td>Network Configuration for customer VPC connectivity.</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the EMR Serverless Application.</td></tr>
<tr><td><code>ApplicationId</code></td><td><code>string</code></td><td>The ID of the EMR Serverless Application.</td></tr>
<tr><td><code>WorkerTypeSpecifications</code></td><td><code>object</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.emrserverless.application<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;ApplicationId&gt;'
</pre>
