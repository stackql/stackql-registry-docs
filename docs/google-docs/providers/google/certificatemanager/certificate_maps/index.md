---
title: certificate_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_maps
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

Creates, updates, deletes, gets or lists a <code>certificate_maps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.certificatemanager.certificate_maps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. A user-defined name of the Certificate Map. Certificate Map names must be unique globally and match pattern `projects/*/locations/*/certificateMaps/*`. |
| <CopyableCode code="description" /> | `string` | Optional. One or more paragraphs of text description of a certificate map. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of a Certificate Map. |
| <CopyableCode code="gclbTargets" /> | `array` | Output only. A list of GCLB targets that use this Certificate Map. A Target Proxy is only present on this list if it's attached to a Forwarding Rule. |
| <CopyableCode code="labels" /> | `object` | Optional. Set of labels associated with a Certificate Map. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The update timestamp of a Certificate Map. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateMapsId, locationsId, projectsId" /> | Gets details of a single CertificateMap. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists CertificateMaps in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new CertificateMap in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="certificateMapsId, locationsId, projectsId" /> | Deletes a single CertificateMap. A Certificate Map can't be deleted if it contains Certificate Map Entries. Remove all the entries from the map before calling this method. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="certificateMapsId, locationsId, projectsId" /> | Updates a CertificateMap. |

## `SELECT` examples

Lists CertificateMaps in a given project and location.

```sql
SELECT
name,
description,
createTime,
gclbTargets,
labels,
updateTime
FROM google.certificatemanager.certificate_maps
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>certificate_maps</code> resource.

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
INSERT INTO google.certificatemanager.certificate_maps (
locationsId,
projectsId,
name,
description,
labels
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
description: string
createTime: string
updateTime: string
labels: object
gclbTargets:
  - targetHttpsProxy: string
    targetSslProxy: string
    ipConfigs:
      - ipAddress: string
        ports:
          - type: string
            format: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>certificate_maps</code> resource.

```sql
/*+ update */
UPDATE google.certificatemanager.certificate_maps
SET 
name = '{{ name }}',
description = '{{ description }}',
labels = '{{ labels }}'
WHERE 
certificateMapsId = '{{ certificateMapsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>certificate_maps</code> resource.

```sql
/*+ delete */
DELETE FROM google.certificatemanager.certificate_maps
WHERE certificateMapsId = '{{ certificateMapsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
