---
title: code_signing_config
hide_title: false
hide_table_of_contents: false
keywords:
  - code_signing_config
  - lambda
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>code_signing_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>code_signing_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>code_signing_config</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lambda.code_signing_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>A description of the CodeSigningConfig</td></tr>
<tr><td><code>AllowedPublishers</code></td><td><code>object</code></td><td>When the CodeSigningConfig is later on attached to a function, the function code will be expected to be signed by profiles from this list</td></tr>
<tr><td><code>CodeSigningPolicies</code></td><td><code>object</code></td><td>Policies to control how to act if a signature is invalid</td></tr>
<tr><td><code>CodeSigningConfigId</code></td><td><code>string</code></td><td>A unique identifier for CodeSigningConfig resource</td></tr>
<tr><td><code>CodeSigningConfigArn</code></td><td><code>string</code></td><td>A unique Arn for CodeSigningConfig resource</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.lambda.code_signing_config<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;CodeSigningConfigArn&gt;'
</pre>
