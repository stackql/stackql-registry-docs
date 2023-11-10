---
title: certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate
  - certificatemanager
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>certificate</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>certificate</td></tr>
<tr><td><b>Id</b></td><td><code>aws.certificatemanager.certificate</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>certificate_authority_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_validation_options</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>certificate_transparency_logging_preference</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>validation_method</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subject_alternative_names</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
certificate_authority_arn,
domain_validation_options,
certificate_transparency_logging_preference,
domain_name,
validation_method,
subject_alternative_names,
id,
tags
FROM aws.certificatemanager.certificate
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
