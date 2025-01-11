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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>load_balancer_tls_certificate</code> resource or lists <code>load_balancer_tls_certificates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancer_tls_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::LoadBalancerTlsCertificate</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.load_balancer_tls_certificates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="load_balancer_name" /></td><td><code>string</code></td><td>The name of your load balancer.</td></tr>
<tr><td><CopyableCode code="certificate_name" /></td><td><code>string</code></td><td>The SSL/TLS certificate name.</td></tr>
<tr><td><CopyableCode code="certificate_domain_name" /></td><td><code>string</code></td><td>The domain name (e.g., example.com ) for your SSL/TLS certificate.</td></tr>
<tr><td><CopyableCode code="certificate_alternative_names" /></td><td><code>array</code></td><td>An array of strings listing alternative domains and subdomains for your SSL/TLS certificate.</td></tr>
<tr><td><CopyableCode code="load_balancer_tls_certificate_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="is_attached" /></td><td><code>boolean</code></td><td>When true, the SSL/TLS certificate is attached to the Lightsail load balancer.</td></tr>
<tr><td><CopyableCode code="https_redirection_enabled" /></td><td><code>boolean</code></td><td>A Boolean value that indicates whether HTTPS redirection is enabled for the load balancer.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The validation status of the SSL/TLS certificate.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancertlscertificate.html"><code>AWS::Lightsail::LoadBalancerTlsCertificate</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="LoadBalancerName, CertificateName, CertificateDomainName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>load_balancer_tls_certificates</code> in a region.
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
FROM aws.lightsail.load_balancer_tls_certificates
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>load_balancer_tls_certificate</code>.
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
FROM aws.lightsail.load_balancer_tls_certificates
WHERE region = 'us-east-1' AND data__Identifier = '<CertificateName>|<LoadBalancerName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>load_balancer_tls_certificate</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.lightsail.load_balancer_tls_certificates (
 LoadBalancerName,
 CertificateName,
 CertificateDomainName,
 region
)
SELECT 
'{{ LoadBalancerName }}',
 '{{ CertificateName }}',
 '{{ CertificateDomainName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.lightsail.load_balancer_tls_certificates (
 LoadBalancerName,
 CertificateName,
 CertificateDomainName,
 CertificateAlternativeNames,
 IsAttached,
 HttpsRedirectionEnabled,
 region
)
SELECT 
 '{{ LoadBalancerName }}',
 '{{ CertificateName }}',
 '{{ CertificateDomainName }}',
 '{{ CertificateAlternativeNames }}',
 '{{ IsAttached }}',
 '{{ HttpsRedirectionEnabled }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: load_balancer_tls_certificate
    props:
      - name: LoadBalancerName
        value: '{{ LoadBalancerName }}'
      - name: CertificateName
        value: '{{ CertificateName }}'
      - name: CertificateDomainName
        value: '{{ CertificateDomainName }}'
      - name: CertificateAlternativeNames
        value:
          - '{{ CertificateAlternativeNames[0] }}'
      - name: IsAttached
        value: '{{ IsAttached }}'
      - name: HttpsRedirectionEnabled
        value: '{{ HttpsRedirectionEnabled }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.lightsail.load_balancer_tls_certificates
WHERE data__Identifier = '<CertificateName|LoadBalancerName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>load_balancer_tls_certificates</code> resource, the following permissions are required:

### Create
```json
lightsail:CreateLoadBalancerTlsCertificate,
lightsail:GetLoadBalancerTlsCertificates,
lightsail:GetLoadBalancer,
lightsail:AttachLoadBalancerTlsCertificate,
lightsail:UpdateLoadBalancerAttribute
```

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

### List
```json
lightsail:GetLoadBalancerTlsCertificates,
lightsail:GetLoadBalancer
```
