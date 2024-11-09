---
title: swift_virtual_network_connection_with_check_slots
hide_title: false
hide_table_of_contents: false
keywords:
  - swift_virtual_network_connection_with_check_slots
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

Creates, updates, deletes, gets or lists a <code>swift_virtual_network_connection_with_check_slots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>swift_virtual_network_connection_with_check_slots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.swift_virtual_network_connection_with_check_slots" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not
in use by another App Service Plan other than the one this App is in. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not
in use by another App Service Plan other than the one this App is in. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>swift_virtual_network_connection_with_check_slots</code> resource.

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
INSERT INTO azure.app_service.swift_virtual_network_connection_with_check_slots (
name,
resourceGroupName,
slot,
subscriptionId,
kind,
properties
)
SELECT 
'{{ name }}',
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
        - name: subnetResourceId
          value: string
        - name: swiftSupported
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>swift_virtual_network_connection_with_check_slots</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.swift_virtual_network_connection_with_check_slots
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```