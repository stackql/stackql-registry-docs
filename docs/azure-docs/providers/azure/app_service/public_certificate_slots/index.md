---
title: public_certificate_slots
hide_title: false
hide_table_of_contents: false
keywords:
  - public_certificate_slots
  - app_service
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

Creates, updates, deletes, gets or lists a <code>public_certificate_slots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_certificate_slots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.public_certificate_slots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | PublicCertificate resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, publicCertificateName, resourceGroupName, slot, subscriptionId" /> | Description for Get the named public certificate for an app (or deployment slot, if specified). |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Get public certificates for an app or a deployment slot. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, publicCertificateName, resourceGroupName, slot, subscriptionId" /> | Description for Creates a hostname binding for an app. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, publicCertificateName, resourceGroupName, slot, subscriptionId" /> | Description for Deletes a hostname binding for an app. |

## `SELECT` examples

Description for Get public certificates for an app or a deployment slot.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.public_certificate_slots
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>public_certificate_slots</code> resource.

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
INSERT INTO azure.app_service.public_certificate_slots (
name,
publicCertificateName,
resourceGroupName,
slot,
subscriptionId,
kind,
properties
)
SELECT 
'{{ name }}',
'{{ publicCertificateName }}',
'{{ resourceGroupName }}',
'{{ slot }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: kind
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: blob
          value: string
        - name: publicCertificateLocation
          value: string
        - name: thumbprint
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>public_certificate_slots</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.public_certificate_slots
WHERE name = '{{ name }}'
AND publicCertificateName = '{{ publicCertificateName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```
