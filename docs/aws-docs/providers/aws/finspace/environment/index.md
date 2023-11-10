---
title: environment
hide_title: false
hide_table_of_contents: false
keywords:
  - environment
  - finspace
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>environment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>environment</td></tr>
<tr><td><b>Id</b></td><td><code>aws.finspace.environment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>environment_id</code></td><td><code>string</code></td><td>Unique identifier for representing FinSpace Environment</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the Environment</td></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td>AWS account ID associated with the Environment</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Description of the Environment</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>State of the Environment</td></tr>
<tr><td><code>environment_url</code></td><td><code>string</code></td><td>URL used to login to the Environment</td></tr>
<tr><td><code>environment_arn</code></td><td><code>string</code></td><td>ARN of the Environment</td></tr>
<tr><td><code>sage_maker_studio_domain_url</code></td><td><code>string</code></td><td>SageMaker Studio Domain URL associated with the Environment</td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td>KMS key used to encrypt customer data within FinSpace Environment infrastructure</td></tr>
<tr><td><code>dedicated_service_account_id</code></td><td><code>string</code></td><td>ID for FinSpace created account used to store Environment artifacts</td></tr>
<tr><td><code>federation_mode</code></td><td><code>string</code></td><td>Federation mode used with the Environment</td></tr>
<tr><td><code>federation_parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>superuser_parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>data_bundles</code></td><td><code>array</code></td><td>ARNs of FinSpace Data Bundles to install</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
environment_id,
name,
aws_account_id,
description,
status,
environment_url,
environment_arn,
sage_maker_studio_domain_url,
kms_key_id,
dedicated_service_account_id,
federation_mode,
federation_parameters,
superuser_parameters,
data_bundles
FROM aws.finspace.environment
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;EnvironmentId&gt;'
```
