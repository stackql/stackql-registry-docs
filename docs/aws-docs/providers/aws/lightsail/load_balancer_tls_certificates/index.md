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


Used to retrieve a list of <code>load_balancer_tls_certificates</code> in a region or to create or delete a <code>load_balancer_tls_certificates</code> resource, use <code>load_balancer_tls_certificate</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancer_tls_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::LoadBalancerTlsCertificate</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.load_balancer_tls_certificates" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="certificate_name" /></td><td><code>string</code></td><td>The SSL&#x2F;TLS certificate name.</td></tr>
<tr><td><CopyableCode code="load_balancer_name" /></td><td><code>string</code></td><td>The name of your load balancer.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
certificate_name,
load_balancer_name
FROM aws.lightsail.load_balancer_tls_certificates
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "LoadBalancerName": "{{ LoadBalancerName }}",
 "CertificateName": "{{ CertificateName }}",
 "CertificateDomainName": "{{ CertificateDomainName }}"
}
>>>
--required properties only
INSERT INTO aws.lightsail.load_balancer_tls_certificates (
 LoadBalancerName,
 CertificateName,
 CertificateDomainName,
 region
)
SELECT 
{{ LoadBalancerName }},
 {{ CertificateName }},
 {{ CertificateDomainName }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "LoadBalancerName": "{{ LoadBalancerName }}",
 "CertificateName": "{{ CertificateName }}",
 "CertificateDomainName": "{{ CertificateDomainName }}",
 "CertificateAlternativeNames": [
  "{{ CertificateAlternativeNames[0] }}"
 ],
 "IsAttached": "{{ IsAttached }}",
 "HttpsRedirectionEnabled": "{{ HttpsRedirectionEnabled }}"
}
>>>
--all properties
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
 {{ LoadBalancerName }},
 {{ CertificateName }},
 {{ CertificateDomainName }},
 {{ CertificateAlternativeNames }},
 {{ IsAttached }},
 {{ HttpsRedirectionEnabled }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

