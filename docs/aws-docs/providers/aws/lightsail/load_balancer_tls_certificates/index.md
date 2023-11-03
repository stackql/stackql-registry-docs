---
title: load_balancer_tls_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_tls_certificates
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
Retrieves a list of <code>load_balancer_tls_certificates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancer_tls_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.lightsail.load_balancer_tls_certificates</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>LoadBalancerName</code></td><td><code>string</code></td><td>The name of your load balancer.</td></tr><tr><td><code>CertificateName</code></td><td><code>string</code></td><td>The SSL/TLS certificate name.</td></tr><tr><td><code>CertificateDomainName</code></td><td><code>string</code></td><td>The domain name (e.g., example.com ) for your SSL/TLS certificate.</td></tr><tr><td><code>CertificateAlternativeNames</code></td><td><code>array</code></td><td>An array of strings listing alternative domains and subdomains for your SSL/TLS certificate.</td></tr><tr><td><code>LoadBalancerTlsCertificateArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>IsAttached</code></td><td><code>boolean</code></td><td>When true, the SSL/TLS certificate is attached to the Lightsail load balancer.</td></tr><tr><td><code>HttpsRedirectionEnabled</code></td><td><code>boolean</code></td><td>A Boolean value that indicates whether HTTPS redirection is enabled for the load balancer.</td></tr><tr><td><code>Status</code></td><td><code>string</code></td><td>The validation status of the SSL/TLS certificate.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.lightsail.load_balancer_tls_certificates
WHERE region = 'us-east-1'
</pre>
