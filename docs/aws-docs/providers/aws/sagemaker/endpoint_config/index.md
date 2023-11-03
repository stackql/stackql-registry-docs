---
title: endpoint_config
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_config
  - sagemaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>endpoint_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.sagemaker.endpoint_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ShadowProductionVariants</code></td><td><code>array</code></td><td></td></tr><tr><td><code>DataCaptureConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ProductionVariants</code></td><td><code>array</code></td><td></td></tr><tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AsyncInferenceConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>EndpointConfigName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ExplainerConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.sagemaker.endpoint_config
WHERE region = 'us-east-1' AND data__Identifier = '<Id>'
</pre>
