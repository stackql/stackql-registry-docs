---
title: conformance_pack
hide_title: false
hide_table_of_contents: false
keywords:
  - conformance_pack
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
Gets an individual <code>conformance_pack</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>conformance_pack</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>conformance_pack</td></tr>
<tr><td><b>Id</b></td><td><code>aws.config.conformance_pack</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ConformancePackName</code></td><td><code>string</code></td><td>Name of the conformance pack which will be assigned as the unique identifier.</td></tr>
<tr><td><code>DeliveryS3Bucket</code></td><td><code>string</code></td><td>AWS Config stores intermediate files while processing conformance pack template.</td></tr>
<tr><td><code>DeliveryS3KeyPrefix</code></td><td><code>string</code></td><td>The prefix for delivery S3 bucket.</td></tr>
<tr><td><code>TemplateBody</code></td><td><code>string</code></td><td>A string containing full conformance pack template body. You can only specify one of the template body or template S3Uri fields.</td></tr>
<tr><td><code>TemplateS3Uri</code></td><td><code>string</code></td><td>Location of file containing the template body which points to the conformance pack template that is located in an Amazon S3 bucket. You can only specify one of the template body or template S3Uri fields.</td></tr>
<tr><td><code>TemplateSSMDocumentDetails</code></td><td><code>object</code></td><td>The TemplateSSMDocumentDetails object contains the name of the SSM document and the version of the SSM document.</td></tr>
<tr><td><code>ConformancePackInputParameters</code></td><td><code>array</code></td><td>A list of ConformancePackInputParameter objects.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.config.conformance_pack<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;ConformancePackName&gt;'
</pre>
