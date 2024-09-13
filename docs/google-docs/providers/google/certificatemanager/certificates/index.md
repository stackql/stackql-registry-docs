---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - certificatemanager
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

Creates, updates, deletes, gets or lists a <code>certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.certificatemanager.certificates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. A user-defined name of the certificate. Certificate names must be unique globally and match pattern `projects/*/locations/*/certificates/*`. |
| <CopyableCode code="description" /> | `string` | Optional. One or more paragraphs of text description of a certificate. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of a Certificate. |
| <CopyableCode code="expireTime" /> | `string` | Output only. The expiry timestamp of a Certificate. |
| <CopyableCode code="labels" /> | `object` | Optional. Set of labels associated with a Certificate. |
| <CopyableCode code="managed" /> | `object` | Configuration and state of a Managed Certificate. Certificate Manager provisions and renews Managed Certificates automatically, for as long as it's authorized to do so. |
| <CopyableCode code="pemCertificate" /> | `string` | Output only. The PEM-encoded certificate chain. |
| <CopyableCode code="sanDnsnames" /> | `array` | Output only. The list of Subject Alternative Names of dnsName type defined in the certificate (see RFC 5280 4.2.1.6). Managed certificates that haven't been provisioned yet have this field populated with a value of the managed.domains field. |
| <CopyableCode code="scope" /> | `string` | Optional. Immutable. The scope of the certificate. |
| <CopyableCode code="selfManaged" /> | `object` | Certificate data for a SelfManaged Certificate. SelfManaged Certificates are uploaded by the user. Updating such certificates before they expire remains the user's responsibility. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp of a Certificate. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificatesId, locationsId, projectsId" /> | Gets details of a single Certificate. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Certificates in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Certificate in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="certificatesId, locationsId, projectsId" /> | Deletes a single Certificate. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="certificatesId, locationsId, projectsId" /> | Updates a Certificate. |

## `SELECT` examples

Lists Certificates in a given project and location.

```sql
SELECT
name,
description,
createTime,
expireTime,
labels,
managed,
pemCertificate,
sanDnsnames,
scope,
selfManaged,
updateTime
FROM google.certificatemanager.certificates
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>certificates</code> resource.

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
INSERT INTO google.certificatemanager.certificates (
locationsId,
projectsId,
name,
description,
createTime,
updateTime,
labels,
selfManaged,
managed,
sanDnsnames,
pemCertificate,
expireTime,
scope
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ selfManaged }}',
'{{ managed }}',
'{{ sanDnsnames }}',
'{{ pemCertificate }}',
'{{ expireTime }}',
'{{ scope }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: description
        value: '{{ description }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: labels
        value: '{{ labels }}'
      - name: selfManaged
        value: '{{ selfManaged }}'
      - name: managed
        value: '{{ managed }}'
      - name: sanDnsnames
        value: '{{ sanDnsnames }}'
      - name: pemCertificate
        value: '{{ pemCertificate }}'
      - name: expireTime
        value: '{{ expireTime }}'
      - name: scope
        value: '{{ scope }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>certificates</code> resource.

```sql
/*+ update */
UPDATE google.certificatemanager.certificates
SET 
name = '{{ name }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
selfManaged = '{{ selfManaged }}',
managed = '{{ managed }}',
sanDnsnames = '{{ sanDnsnames }}',
pemCertificate = '{{ pemCertificate }}',
expireTime = '{{ expireTime }}',
scope = '{{ scope }}'
WHERE 
certificatesId = '{{ certificatesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>certificates</code> resource.

```sql
/*+ delete */
DELETE FROM google.certificatemanager.certificates
WHERE certificatesId = '{{ certificatesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
