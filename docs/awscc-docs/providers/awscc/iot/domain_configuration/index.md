---
title: domain_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_configuration
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>domain_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>domain_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iot.domain_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>domain_configuration_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>authorizer_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>server_certificate_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>service_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>validation_certificate_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_configuration_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>server_certificate_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>server_certificates</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tls_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
domain_configuration_name,
authorizer_config,
domain_name,
server_certificate_arns,
service_type,
validation_certificate_arn,
arn,
domain_configuration_status,
domain_type,
server_certificate_config,
server_certificates,
tls_config,
tags
FROM awscc.iot.domain_configuration
WHERE region = 'us-east-1'
AND data__Identifier = '{DomainConfigurationName}';
```

## Permissions

To operate on the <code>domain_configuration</code> resource, the following permissions are required:

### Read
```json
iot:DescribeDomainConfiguration,
iot:ListTagsForResource
```

### Update
```json
iot:UpdateDomainConfiguration,
iot:DescribeDomainConfiguration,
iot:ListTagsForResource,
iot:TagResource,
iot:UntagResource
```

### Delete
```json
iot:DescribeDomainConfiguration,
iot:DeleteDomainConfiguration,
iot:UpdateDomainConfiguration
```

