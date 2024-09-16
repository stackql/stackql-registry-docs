---
title: key_handles
hide_title: false
hide_table_of_contents: false
keywords:
  - key_handles
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

Creates, updates, deletes, gets or lists a <code>key_handles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key_handles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudkms.key_handles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of the KeyHandle resource, e.g. `projects/{PROJECT_ID}/locations/{LOCATION}/keyHandles/{KEY_HANDLE_ID}`. |
| <CopyableCode code="kmsKey" /> | `string` | Output only. Name of a CryptoKey that has been provisioned for Customer Managed Encryption Key (CMEK) use in the KeyHandle project and location for the requested resource type. The CryptoKey project will reflect the value configured in the AutokeyConfig on the resource project's ancestor folder at the time of the KeyHandle creation. If more than one ancestor folder has a configured AutokeyConfig, the nearest of these configurations is used. |
| <CopyableCode code="resourceTypeSelector" /> | `string` | Required. Indicates the resource type that the resulting CryptoKey is meant to protect, e.g. `{SERVICE}.googleapis.com/{TYPE}`. See documentation for supported resource types. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keyHandlesId, locationsId, projectsId" /> | Returns the KeyHandle. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists KeyHandles. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new KeyHandle, triggering the provisioning of a new CryptoKey for CMEK use with the given resource type in the configured key project and the same location. GetOperation should be used to resolve the resulting long-running operation and get the resulting KeyHandle and CryptoKey. |

## `SELECT` examples

Lists KeyHandles.

```sql
SELECT
name,
kmsKey,
resourceTypeSelector
FROM google.cloudkms.key_handles
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>key_handles</code> resource.

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
INSERT INTO google.cloudkms.key_handles (
locationsId,
projectsId,
name,
resourceTypeSelector
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ resourceTypeSelector }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: resourceTypeSelector
      value: '{{ resourceTypeSelector }}'

```
</TabItem>
</Tabs>
