---
title: certificate_map_entries
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_map_entries
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

Creates, updates, deletes or gets an <code>certificate_map_entry</code> resource or lists <code>certificate_map_entries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_map_entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.certificatemanager.certificate_map_entries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. A user-defined name of the Certificate Map Entry. Certificate Map Entry names must be unique globally and match pattern `projects/*/locations/*/certificateMaps/*/certificateMapEntries/*`. |
| <CopyableCode code="description" /> | `string` | Optional. One or more paragraphs of text description of a certificate map entry. |
| <CopyableCode code="certificates" /> | `array` | Optional. A set of Certificates defines for the given `hostname`. There can be defined up to four certificates in each Certificate Map Entry. Each certificate must match pattern `projects/*/locations/*/certificates/*`. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of a Certificate Map Entry. |
| <CopyableCode code="hostname" /> | `string` | A Hostname (FQDN, e.g. `example.com`) or a wildcard hostname expression (`*.example.com`) for a set of hostnames with common suffix. Used as Server Name Indication (SNI) for selecting a proper certificate. |
| <CopyableCode code="labels" /> | `object` | Optional. Set of labels associated with a Certificate Map Entry. |
| <CopyableCode code="matcher" /> | `string` | A predefined matcher for particular cases, other than SNI selection. |
| <CopyableCode code="state" /> | `string` | Output only. A serving state of this Certificate Map Entry. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The update timestamp of a Certificate Map Entry. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateMapEntriesId, certificateMapsId, locationsId, projectsId" /> | Gets details of a single CertificateMapEntry. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="certificateMapsId, locationsId, projectsId" /> | Lists CertificateMapEntries in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="certificateMapsId, locationsId, projectsId" /> | Creates a new CertificateMapEntry in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="certificateMapEntriesId, certificateMapsId, locationsId, projectsId" /> | Deletes a single CertificateMapEntry. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="certificateMapEntriesId, certificateMapsId, locationsId, projectsId" /> | Updates a CertificateMapEntry. |

## `SELECT` examples

Lists CertificateMapEntries in a given project and location.

```sql
SELECT
name,
description,
certificates,
createTime,
hostname,
labels,
matcher,
state,
updateTime
FROM google.certificatemanager.certificate_map_entries
WHERE certificateMapsId = '{{ certificateMapsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>certificate_map_entries</code> resource.

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
INSERT INTO google.certificatemanager.certificate_map_entries (
certificateMapsId,
locationsId,
projectsId,
name,
description,
createTime,
updateTime,
labels,
hostname,
matcher,
certificates,
state
)
SELECT 
'{{ certificateMapsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ hostname }}',
'{{ matcher }}',
'{{ certificates }}',
'{{ state }}'
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
      - name: hostname
        value: '{{ hostname }}'
      - name: matcher
        value: '{{ matcher }}'
      - name: certificates
        value: '{{ certificates }}'
      - name: state
        value: '{{ state }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a certificate_map_entry only if the necessary resources are available.

```sql
UPDATE google.certificatemanager.certificate_map_entries
SET 
name = '{{ name }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
hostname = '{{ hostname }}',
matcher = '{{ matcher }}',
certificates = '{{ certificates }}',
state = '{{ state }}'
WHERE 
certificateMapEntriesId = '{{ certificateMapEntriesId }}'
AND certificateMapsId = '{{ certificateMapsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified certificate_map_entry resource.

```sql
DELETE FROM google.certificatemanager.certificate_map_entries
WHERE certificateMapEntriesId = '{{ certificateMapEntriesId }}'
AND certificateMapsId = '{{ certificateMapsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
