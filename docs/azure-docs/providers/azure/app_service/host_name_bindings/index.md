---
title: host_name_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - host_name_bindings
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

Creates, updates, deletes, gets or lists a <code>host_name_bindings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>host_name_bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.host_name_bindings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | HostNameBinding resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostName, name, resourceGroupName, subscriptionId" /> | Description for Get the named hostname binding for an app (or deployment slot, if specified). |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Get hostname bindings for an app or a deployment slot. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hostName, name, resourceGroupName, subscriptionId" /> | Description for Creates a hostname binding for an app. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hostName, name, resourceGroupName, subscriptionId" /> | Description for Deletes a hostname binding for an app. |

## `SELECT` examples

Description for Get hostname bindings for an app or a deployment slot.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.host_name_bindings
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>host_name_bindings</code> resource.

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
INSERT INTO azure.app_service.host_name_bindings (
hostName,
name,
resourceGroupName,
subscriptionId,
kind,
properties
)
SELECT 
'{{ hostName }}',
'{{ name }}',
'{{ resourceGroupName }}',
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
        - name: siteName
          value: string
        - name: domainId
          value: string
        - name: azureResourceName
          value: string
        - name: azureResourceType
          value: string
        - name: customHostNameDnsRecordType
          value: string
        - name: hostNameType
          value: string
        - name: sslState
          value: string
        - name: thumbprint
          value: string
        - name: virtualIP
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>host_name_bindings</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.host_name_bindings
WHERE hostName = '{{ hostName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
