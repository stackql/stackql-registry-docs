---
title: trust_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - trust_configs
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

Creates, updates, deletes, gets or lists a <code>trust_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trust_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.certificatemanager.trust_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. A user-defined name of the trust config. TrustConfig names must be unique globally and match pattern `projects/*/locations/*/trustConfigs/*`. |
| <CopyableCode code="description" /> | `string` | Optional. One or more paragraphs of text description of a TrustConfig. |
| <CopyableCode code="allowlistedCertificates" /> | `array` | Optional. A certificate matching an allowlisted certificate is always considered valid as long as the certificate is parseable, proof of private key possession is established, and constraints on the certificate's SAN field are met. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of a TrustConfig. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. Set of labels associated with a TrustConfig. |
| <CopyableCode code="trustStores" /> | `array` | Optional. Set of trust stores to perform validation against. This field is supported when TrustConfig is configured with Load Balancers, currently not supported for SPIFFE certificate validation. Only one TrustStore specified is currently allowed. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp of a TrustConfig. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, trustConfigsId" /> | Gets details of a single TrustConfig. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists TrustConfigs in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new TrustConfig in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, trustConfigsId" /> | Deletes a single TrustConfig. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, trustConfigsId" /> | Updates a TrustConfig. |

## `SELECT` examples

Lists TrustConfigs in a given project and location.

```sql
SELECT
name,
description,
allowlistedCertificates,
createTime,
etag,
labels,
trustStores,
updateTime
FROM google.certificatemanager.trust_configs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>trust_configs</code> resource.

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
INSERT INTO google.certificatemanager.trust_configs (
locationsId,
projectsId,
name,
createTime,
updateTime,
labels,
description,
etag,
trustStores,
allowlistedCertificates
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ description }}',
'{{ etag }}',
'{{ trustStores }}',
'{{ allowlistedCertificates }}'
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
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: labels
        value: '{{ labels }}'
      - name: description
        value: '{{ description }}'
      - name: etag
        value: '{{ etag }}'
      - name: trustStores
        value: '{{ trustStores }}'
      - name: allowlistedCertificates
        value: '{{ allowlistedCertificates }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>trust_configs</code> resource.

```sql
/*+ update */
UPDATE google.certificatemanager.trust_configs
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
description = '{{ description }}',
etag = '{{ etag }}',
trustStores = '{{ trustStores }}',
allowlistedCertificates = '{{ allowlistedCertificates }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND trustConfigsId = '{{ trustConfigsId }}';
```

## `DELETE` example

Deletes the specified <code>trust_configs</code> resource.

```sql
/*+ delete */
DELETE FROM google.certificatemanager.trust_configs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND trustConfigsId = '{{ trustConfigsId }}';
```
