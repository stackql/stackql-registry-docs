---
title: domain_name
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_name
  - apigateway
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>domain_name</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_name</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>domain_name</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.apigateway.domain_name</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>distribution_domain_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>distribution_hosted_zone_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>endpoint_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>mutual_tls_authentication</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>regional_domain_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>regional_hosted_zone_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>certificate_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>regional_certificate_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ownership_verification_certificate_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>security_policy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>domain_name</code> resource, the following permissions are required:

### Read
```json
apigateway:*
```

### Update
```json
apigateway:*
```

### Delete
```json
apigateway:*
```


## Example
```sql
SELECT
region,
domain_name,
distribution_domain_name,
distribution_hosted_zone_id,
endpoint_configuration,
mutual_tls_authentication,
regional_domain_name,
regional_hosted_zone_id,
certificate_arn,
regional_certificate_arn,
ownership_verification_certificate_arn,
security_policy,
tags
FROM awscc.apigateway.domain_name
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DomainName&gt;'
```
