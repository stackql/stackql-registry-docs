---
title: region_ssl_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - region_ssl_certificates
  - compute
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>region_ssl_certificate</code> resource or lists <code>region_ssl_certificates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_ssl_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_ssl_certificates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="certificate" /> | `string` | A value read into memory from a certificate file. The certificate file must be in PEM format. The certificate chain must be no greater than 5 certs long. The chain must include at least one intermediate cert. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="expireTime" /> | `string` | [Output Only] Expire time of the certificate. RFC3339 |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#sslCertificate for SSL certificates. |
| <CopyableCode code="managed" /> | `object` | Configuration and status of a managed SSL certificate. |
| <CopyableCode code="privateKey" /> | `string` | A value read into memory from a write-only private key file. The private key file must be in PEM format. For security, only insert requests include this field. |
| <CopyableCode code="region" /> | `string` | [Output Only] URL of the region where the regional SSL Certificate resides. This field is not applicable to global SSL Certificate. |
| <CopyableCode code="selfLink" /> | `string` | [Output only] Server-defined URL for the resource. |
| <CopyableCode code="selfManaged" /> | `object` | Configuration and status of a self-managed SSL certificate. |
| <CopyableCode code="subjectAlternativeNames" /> | `array` | [Output Only] Domains associated with the certificate via Subject Alternative Name. |
| <CopyableCode code="type" /> | `string` | (Optional) Specifies the type of SSL certificate, either "SELF_MANAGED" or "MANAGED". If not specified, the certificate is self-managed and the fields certificate and private_key are used. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, region, sslCertificate" /> | Returns the specified SslCertificate resource in the specified region. Get a list of available SSL certificates by making a list() request. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Retrieves the list of SslCertificate resources available to the specified project in the specified region. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a SslCertificate resource in the specified project and region using the data included in the request |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, region, sslCertificate" /> | Deletes the specified SslCertificate resource in the region. |

## `SELECT` examples

Retrieves the list of SslCertificate resources available to the specified project in the specified region.

```sql
SELECT
id,
name,
description,
certificate,
creationTimestamp,
expireTime,
kind,
managed,
privateKey,
region,
selfLink,
selfManaged,
subjectAlternativeNames,
type
FROM google.compute.region_ssl_certificates
WHERE project = '{{ project }}'
AND region = '{{ region }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>region_ssl_certificates</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.compute.region_ssl_certificates (
project,
region,
kind,
id,
creationTimestamp,
name,
description,
selfLink,
certificate,
privateKey,
managed,
selfManaged,
type,
subjectAlternativeNames,
expireTime,
region
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ name }}',
'{{ description }}',
'{{ selfLink }}',
'{{ certificate }}',
'{{ privateKey }}',
'{{ managed }}',
'{{ selfManaged }}',
'{{ type }}',
'{{ subjectAlternativeNames }}',
'{{ expireTime }}',
'{{ region }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: kind
        value: '{{ kind }}'
      - name: id
        value: '{{ id }}'
      - name: creationTimestamp
        value: '{{ creationTimestamp }}'
      - name: name
        value: '{{ name }}'
      - name: description
        value: '{{ description }}'
      - name: selfLink
        value: '{{ selfLink }}'
      - name: certificate
        value: '{{ certificate }}'
      - name: privateKey
        value: '{{ privateKey }}'
      - name: managed
        value: '{{ managed }}'
      - name: selfManaged
        value: '{{ selfManaged }}'
      - name: type
        value: '{{ type }}'
      - name: subjectAlternativeNames
        value: '{{ subjectAlternativeNames }}'
      - name: expireTime
        value: '{{ expireTime }}'
      - name: region
        value: '{{ region }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified region_ssl_certificate resource.

```sql
DELETE FROM google.compute.region_ssl_certificates
WHERE project = '{{ project }}'
AND region = '{{ region }}'
AND sslCertificate = '{{ sslCertificate }}';
```
