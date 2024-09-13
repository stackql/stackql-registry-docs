---
title: ssl_certs
hide_title: false
hide_table_of_contents: false
keywords:
  - ssl_certs
  - sqladmin
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

Creates, updates, deletes or gets an <code>ssl_cert</code> resource or lists <code>ssl_certs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ssl_certs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sqladmin.ssl_certs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cert" /> | `string` | PEM representation. |
| <CopyableCode code="certSerialNumber" /> | `string` | Serial number, as extracted from the certificate. |
| <CopyableCode code="commonName" /> | `string` | User supplied name. Constrained to [a-zA-Z.-_ ]+. |
| <CopyableCode code="createTime" /> | `string` | The time when the certificate was created in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z` |
| <CopyableCode code="expirationTime" /> | `string` | The time when the certificate expires in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. |
| <CopyableCode code="instance" /> | `string` | Name of the database instance. |
| <CopyableCode code="kind" /> | `string` | This is always `sql#sslCert`. |
| <CopyableCode code="selfLink" /> | `string` | The URI of this resource. |
| <CopyableCode code="sha1Fingerprint" /> | `string` | Sha1 Fingerprint. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instance, project, sha1Fingerprint" /> | Retrieves a particular SSL certificate. Does not include the private key (required for usage). The private key must be saved from the response to initial creation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instance, project" /> | Lists all of the current SSL certificates for the instance. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="instance, project" /> | Creates an SSL certificate and returns it along with the private key and server certificate authority. The new certificate will not be usable until the instance is restarted. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instance, project, sha1Fingerprint" /> | Deletes the SSL certificate. For First Generation instances, the certificate remains valid until the instance is restarted. |

## `SELECT` examples

Lists all of the current SSL certificates for the instance.

```sql
SELECT
cert,
certSerialNumber,
commonName,
createTime,
expirationTime,
instance,
kind,
selfLink,
sha1Fingerprint
FROM google.sqladmin.ssl_certs
WHERE instance = '{{ instance }}'
AND project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ssl_certs</code> resource.

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
INSERT INTO google.sqladmin.ssl_certs (
instance,
project,
commonName
)
SELECT 
'{{ instance }}',
'{{ project }}',
'{{ commonName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: commonName
        value: '{{ commonName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified ssl_cert resource.

```sql
DELETE FROM google.sqladmin.ssl_certs
WHERE instance = '{{ instance }}'
AND project = '{{ project }}'
AND sha1Fingerprint = '{{ sha1Fingerprint }}';
```
