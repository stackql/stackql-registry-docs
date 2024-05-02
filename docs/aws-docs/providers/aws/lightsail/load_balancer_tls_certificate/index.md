---
title: load_balancer_tls_certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_tls_certificate
  - lightsail
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>load_balancer_tls_certificate</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancer_tls_certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::LoadBalancerTlsCertificate</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lightsail.load_balancer_tls_certificate</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>load_balancer_name</code></td><td><code>string</code></td><td>The name of your load balancer.</td></tr>
<tr><td><code>certificate_name</code></td><td><code>string</code></td><td>The SSL&#x2F;TLS certificate name.</td></tr>
<tr><td><code>certificate_domain_name</code></td><td><code>string</code></td><td>The domain name (e.g., example.com ) for your SSL&#x2F;TLS certificate.</td></tr>
<tr><td><code>certificate_alternative_names</code></td><td><code>array</code></td><td>An array of strings listing alternative domains and subdomains for your SSL&#x2F;TLS certificate.</td></tr>
<tr><td><code>load_balancer_tls_certificate_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>is_attached</code></td><td><code>boolean</code></td><td>When true, the SSL&#x2F;TLS certificate is attached to the Lightsail load balancer.</td></tr>
<tr><td><code>https_redirection_enabled</code></td><td><code>boolean</code></td><td>A Boolean value that indicates whether HTTPS redirection is enabled for the load balancer.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The validation status of the SSL&#x2F;TLS certificate.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
load_balancer_name,
certificate_name,
certificate_domain_name,
certificate_alternative_names,
load_balancer_tls_certificate_arn,
is_attached,
https_redirection_enabled,
status
FROM aws.lightsail.load_balancer_tls_certificate
WHERE data__Identifier = '<CertificateName>|<LoadBalancerName>';
```

## Permissions

To operate on the <code>load_balancer_tls_certificate</code> resource, the following permissions are required:

### Read
```json
lightsail:GetLoadBalancerTlsCertificates,
lightsail:GetLoadBalancer
```

### Update
```json
lightsail:AttachLoadBalancerTlsCertificate,
lightsail:GetLoadBalancerTlsCertificates,
lightsail:GetLoadBalancer,
lightsail:UpdateLoadBalancerAttribute
```

### Delete
```json
lightsail:DeleteLoadBalancerTlsCertificate,
lightsail:GetLoadBalancerTlsCertificates,
lightsail:GetLoadBalancer
```

