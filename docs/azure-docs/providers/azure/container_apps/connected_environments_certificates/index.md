---
title: connected_environments_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_environments_certificates
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>connected_environments_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connected_environments_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.connected_environments_certificates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Certificate resource specific properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateName, connectedEnvironmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="certificateName, connectedEnvironmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="certificateName, connectedEnvironmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="certificateName, connectedEnvironmentName, resourceGroupName, subscriptionId" /> | Patches a certificate. Currently only patching of tags is supported |

## `SELECT` examples




```sql
SELECT
location,
properties,
tags
FROM azure.container_apps.connected_environments_certificates
WHERE connectedEnvironmentName = '{{ connectedEnvironmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connected_environments_certificates</code> resource.

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
INSERT INTO azure.container_apps.connected_environments_certificates (
certificateName,
connectedEnvironmentName,
resourceGroupName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ certificateName }}',
'{{ connectedEnvironmentName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: certificateKeyVaultProperties
          value:
            - name: identity
              value: string
            - name: keyVaultUrl
              value: string
        - name: password
          value: string
        - name: subjectName
          value: string
        - name: subjectAlternativeNames
          value:
            - string
        - name: value
          value: string
        - name: issuer
          value: string
        - name: issueDate
          value: string
        - name: expirationDate
          value: string
        - name: thumbprint
          value: string
        - name: valid
          value: boolean
        - name: publicKeyHash
          value: string
        - name: certificateType
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>connected_environments_certificates</code> resource.

```sql
/*+ update */
UPDATE azure.container_apps.connected_environments_certificates
SET 
tags = '{{ tags }}'
WHERE 
certificateName = '{{ certificateName }}'
AND connectedEnvironmentName = '{{ connectedEnvironmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>connected_environments_certificates</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.connected_environments_certificates
WHERE certificateName = '{{ certificateName }}'
AND connectedEnvironmentName = '{{ connectedEnvironmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
