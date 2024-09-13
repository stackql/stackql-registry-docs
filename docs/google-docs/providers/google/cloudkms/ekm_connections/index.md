---
title: ekm_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - ekm_connections
  - cloudkms
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

Creates, updates, deletes or gets an <code>ekm_connection</code> resource or lists <code>ekm_connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ekm_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudkms.ekm_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name for the EkmConnection in the format `projects/*/locations/*/ekmConnections/*`. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which the EkmConnection was created. |
| <CopyableCode code="cryptoSpacePath" /> | `string` | Optional. Identifies the EKM Crypto Space that this EkmConnection maps to. Note: This field is required if KeyManagementMode is CLOUD_KMS. |
| <CopyableCode code="etag" /> | `string` | Optional. Etag of the currently stored EkmConnection. |
| <CopyableCode code="keyManagementMode" /> | `string` | Optional. Describes who can perform control plane operations on the EKM. If unset, this defaults to MANUAL. |
| <CopyableCode code="serviceResolvers" /> | `array` | Optional. A list of ServiceResolvers where the EKM can be reached. There should be one ServiceResolver per EKM replica. Currently, only a single ServiceResolver is supported. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ekmConnectionsId, locationsId, projectsId" /> | Returns metadata for a given EkmConnection. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists EkmConnections. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new EkmConnection in a given Project and Location. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="ekmConnectionsId, locationsId, projectsId" /> | Updates an EkmConnection's metadata. |
| <CopyableCode code="verify_connectivity" /> | `EXEC` | <CopyableCode code="ekmConnectionsId, locationsId, projectsId" /> | Verifies that Cloud KMS can successfully connect to the external key manager specified by an EkmConnection. If there is an error connecting to the EKM, this method returns a FAILED_PRECONDITION status containing structured information as described at https://cloud.google.com/kms/docs/reference/ekm_errors. |

## `SELECT` examples

Lists EkmConnections.

```sql
SELECT
name,
createTime,
cryptoSpacePath,
etag,
keyManagementMode,
serviceResolvers
FROM google.cloudkms.ekm_connections
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ekm_connections</code> resource.

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
INSERT INTO google.cloudkms.ekm_connections (
locationsId,
projectsId,
name,
createTime,
serviceResolvers,
etag,
keyManagementMode,
cryptoSpacePath
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ serviceResolvers }}',
'{{ etag }}',
'{{ keyManagementMode }}',
'{{ cryptoSpacePath }}'
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
      - name: serviceResolvers
        value: '{{ serviceResolvers }}'
      - name: etag
        value: '{{ etag }}'
      - name: keyManagementMode
        value: '{{ keyManagementMode }}'
      - name: cryptoSpacePath
        value: '{{ cryptoSpacePath }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a ekm_connection only if the necessary resources are available.

```sql
UPDATE google.cloudkms.ekm_connections
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
serviceResolvers = '{{ serviceResolvers }}',
etag = '{{ etag }}',
keyManagementMode = '{{ keyManagementMode }}',
cryptoSpacePath = '{{ cryptoSpacePath }}'
WHERE 
ekmConnectionsId = '{{ ekmConnectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
