---
title: managed_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_certificates
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

Creates, updates, deletes, gets or lists a <code>managed_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.managed_certificates" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentName, managedCertificateName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentName, managedCertificateName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentName, managedCertificateName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="environmentName, managedCertificateName, resourceGroupName, subscriptionId" /> | Patches a managed certificate. Oly patching of tags is supported |

## `SELECT` examples




```sql
SELECT
location,
properties,
tags
FROM azure.container_apps.managed_certificates
WHERE environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_certificates</code> resource.

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
INSERT INTO azure.container_apps.managed_certificates (
environmentName,
managedCertificateName,
resourceGroupName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ environmentName }}',
'{{ managedCertificateName }}',
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
        - name: subjectName
          value: string
        - name: error
          value: string
        - name: domainControlValidation
          value: string
        - name: validationToken
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>managed_certificates</code> resource.

```sql
/*+ update */
UPDATE azure.container_apps.managed_certificates
SET 
tags = '{{ tags }}'
WHERE 
environmentName = '{{ environmentName }}'
AND managedCertificateName = '{{ managedCertificateName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>managed_certificates</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.managed_certificates
WHERE environmentName = '{{ environmentName }}'
AND managedCertificateName = '{{ managedCertificateName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
