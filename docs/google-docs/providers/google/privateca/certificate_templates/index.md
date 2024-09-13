---
title: certificate_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_templates
  - privateca
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

Creates, updates, deletes, gets or lists a <code>certificate_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.privateca.certificate_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name for this CertificateTemplate in the format `projects/*/locations/*/certificateTemplates/*`. |
| <CopyableCode code="description" /> | `string` | Optional. A human-readable description of scenarios this template is intended for. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which this CertificateTemplate was created. |
| <CopyableCode code="identityConstraints" /> | `object` | Describes constraints on a Certificate's Subject and SubjectAltNames. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels with user-defined metadata. |
| <CopyableCode code="maximumLifetime" /> | `string` | Optional. The maximum lifetime allowed for issued Certificates that use this template. If the issuing CaPool resource's IssuancePolicy specifies a maximum_lifetime the minimum of the two durations will be the maximum lifetime for issued Certificates. Note that if the issuing CertificateAuthority expires before a Certificate's requested maximum_lifetime, the effective lifetime will be explicitly truncated to match it. |
| <CopyableCode code="passthroughExtensions" /> | `object` | Describes a set of X.509 extensions that may be part of some certificate issuance controls. |
| <CopyableCode code="predefinedValues" /> | `object` | An X509Parameters is used to describe certain fields of an X.509 certificate, such as the key usage fields, fields specific to CA certificates, certificate policy extensions and custom extensions. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time at which this CertificateTemplate was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateTemplatesId, locationsId, projectsId" /> | Returns a CertificateTemplate. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists CertificateTemplates. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a new CertificateTemplate in a given Project and Location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="certificateTemplatesId, locationsId, projectsId" /> | DeleteCertificateTemplate deletes a CertificateTemplate. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="certificateTemplatesId, locationsId, projectsId" /> | Update a CertificateTemplate. |

## `SELECT` examples

Lists CertificateTemplates.

```sql
SELECT
name,
description,
createTime,
identityConstraints,
labels,
maximumLifetime,
passthroughExtensions,
predefinedValues,
updateTime
FROM google.privateca.certificate_templates
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>certificate_templates</code> resource.

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
INSERT INTO google.privateca.certificate_templates (
locationsId,
projectsId,
name,
maximumLifetime,
predefinedValues,
identityConstraints,
passthroughExtensions,
description,
createTime,
updateTime,
labels
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ maximumLifetime }}',
'{{ predefinedValues }}',
'{{ identityConstraints }}',
'{{ passthroughExtensions }}',
'{{ description }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}'
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
      - name: maximumLifetime
        value: '{{ maximumLifetime }}'
      - name: predefinedValues
        value: '{{ predefinedValues }}'
      - name: identityConstraints
        value: '{{ identityConstraints }}'
      - name: passthroughExtensions
        value: '{{ passthroughExtensions }}'
      - name: description
        value: '{{ description }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: labels
        value: '{{ labels }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>certificate_templates</code> resource.

```sql
/*+ update */
UPDATE google.privateca.certificate_templates
SET 
name = '{{ name }}',
maximumLifetime = '{{ maximumLifetime }}',
predefinedValues = '{{ predefinedValues }}',
identityConstraints = '{{ identityConstraints }}',
passthroughExtensions = '{{ passthroughExtensions }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}'
WHERE 
certificateTemplatesId = '{{ certificateTemplatesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>certificate_templates</code> resource.

```sql
/*+ delete */
DELETE FROM google.privateca.certificate_templates
WHERE certificateTemplatesId = '{{ certificateTemplatesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
