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
<tr><td><b>Id</b></td><td><code>aws.apigateway.domain_name</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DomainName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DistributionDomainName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DistributionHostedZoneId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>EndpointConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>MutualTlsAuthentication</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>RegionalDomainName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RegionalHostedZoneId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CertificateArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RegionalCertificateArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>OwnershipVerificationCertificateArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SecurityPolicy</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.apigateway.domain_name
WHERE region = 'us-east-1' AND data__Identifier = '{DomainName}'
```
