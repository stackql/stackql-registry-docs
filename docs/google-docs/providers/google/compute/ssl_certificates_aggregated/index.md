---
title: ssl_certificates_aggregated
hide_title: false
hide_table_of_contents: false
keywords:
  - ssl_certificates_aggregated
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

Creates, updates, deletes, gets or lists a <code>ssl_certificates_aggregated</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ssl_certificates_aggregated</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.ssl_certificates_aggregated" /></td></tr>
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
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of all SslCertificate resources, regional and global, available to the specified project. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |

## `SELECT` examples

Retrieves the list of all SslCertificate resources, regional and global, available to the specified project. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

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
FROM google.compute.ssl_certificates_aggregated
WHERE project = '{{ project }}';
```
