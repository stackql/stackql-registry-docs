---
title: custom_data_identifier
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_data_identifier
  - macie
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>custom_data_identifier</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_data_identifier</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.macie.custom_data_identifier</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Name of custom data identifier.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>Description of custom data identifier.</td></tr><tr><td><code>Regex</code></td><td><code>string</code></td><td>Regular expression for custom data identifier.</td></tr><tr><td><code>MaximumMatchDistance</code></td><td><code>integer</code></td><td>Maximum match distance.</td></tr><tr><td><code>Keywords</code></td><td><code>array</code></td><td>Keywords to be matched against.</td></tr><tr><td><code>IgnoreWords</code></td><td><code>array</code></td><td>Words to be ignored.</td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td>Custom data identifier ID.</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>Custom data identifier ARN.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.macie.custom_data_identifier
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
</pre>
