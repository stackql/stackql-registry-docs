---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - fluid_relay
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

Creates, updates, deletes, gets or lists a <code>servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.fluid_relay.servers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_servers', value: 'view', },
        { label: 'servers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="fluidRelayServerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="fluid_relay_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="frs_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroup" /> | `text` | field from the `properties` object |
| <CopyableCode code="storagesku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of a Fluid Relay Service resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fluidRelayServerName, resourceGroup, subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroup, subscriptionId" /> |  |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="fluidRelayServerName, resourceGroup, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fluidRelayServerName, resourceGroup, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="fluidRelayServerName, resourceGroup, subscriptionId" /> |  |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="fluidRelayServerName, resourceGroup, subscriptionId, data__keyName" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_servers', value: 'view', },
        { label: 'servers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
encryption,
fluidRelayServerName,
fluid_relay_endpoints,
frs_tenant_id,
identity,
location,
provisioning_state,
resourceGroup,
storagesku,
subscriptionId,
system_data,
tags
FROM azure.fluid_relay.vw_servers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
systemData,
tags
FROM azure.fluid_relay.servers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>servers</code> resource.

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
INSERT INTO azure.fluid_relay.servers (
fluidRelayServerName,
resourceGroup,
subscriptionId,
properties,
identity,
tags,
location
)
SELECT 
'{{ fluidRelayServerName }}',
'{{ resourceGroup }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ identity }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: frsTenantId
          value: string
        - name: fluidRelayEndpoints
          value:
            - name: ordererEndpoints
              value:
                - string
            - name: storageEndpoints
              value:
                - string
            - name: serviceEndpoints
              value:
                - string
        - name: provisioningState
          value: string
        - name: encryption
          value:
            - name: customerManagedKeyEncryption
              value:
                - name: keyEncryptionKeyIdentity
                  value:
                    - name: identityType
                      value: string
                    - name: userAssignedIdentityResourceId
                      value: string
                - name: keyEncryptionKeyUrl
                  value: string
        - name: storagesku
          value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: object
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>servers</code> resource.

```sql
/*+ update */
UPDATE azure.fluid_relay.servers
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
identity = '{{ identity }}',
location = '{{ location }}'
WHERE 
fluidRelayServerName = '{{ fluidRelayServerName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>servers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.fluid_relay.servers
WHERE fluidRelayServerName = '{{ fluidRelayServerName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```
