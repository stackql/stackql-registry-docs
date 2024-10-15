---
title: data_products
hide_title: false
hide_table_of_contents: false
keywords:
  - data_products
  - network_analytics
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

Creates, updates, deletes, gets or lists a <code>data_products</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network_analytics.data_products" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_products', value: 'view', },
        { label: 'data_products', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="available_minor_versions" /> | `text` | field from the `properties` object |
| <CopyableCode code="consumption_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_minor_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_encryption_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_managed_key_encryption_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataProductName" /> | `text` | field from the `properties` object |
| <CopyableCode code="documentation" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="key_vault_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="major_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_resource_group_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkacls" /> | `text` | field from the `properties` object |
| <CopyableCode code="owners" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_links_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="product" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher" /> | `text` | field from the `properties` object |
| <CopyableCode code="purview_account" /> | `text` | field from the `properties` object |
| <CopyableCode code="purview_collection" /> | `text` | field from the `properties` object |
| <CopyableCode code="redundancy" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The data product properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataProductName, resourceGroupName, subscriptionId" /> | Retrieve data product resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List data products by resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List data products by subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="dataProductName, resourceGroupName, subscriptionId" /> | Create data product resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataProductName, resourceGroupName, subscriptionId" /> | Delete data product resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="dataProductName, resourceGroupName, subscriptionId" /> | Update data product resource. |
| <CopyableCode code="add_user_role" /> | `EXEC` | <CopyableCode code="dataProductName, resourceGroupName, subscriptionId, data__dataTypeScope, data__principalId, data__principalType, data__role, data__roleId, data__userName" /> | Assign role to the data product. |
| <CopyableCode code="generate_storage_account_sas_token" /> | `EXEC` | <CopyableCode code="dataProductName, resourceGroupName, subscriptionId, data__expiryTimeStamp, data__ipAddress, data__startTimeStamp" /> | Generate sas token for storage account. |
| <CopyableCode code="remove_user_role" /> | `EXEC` | <CopyableCode code="dataProductName, resourceGroupName, subscriptionId, data__dataTypeScope, data__principalId, data__principalType, data__role, data__roleAssignmentId, data__roleId, data__userName" /> | Remove role from the data product. |
| <CopyableCode code="rotate_key" /> | `EXEC` | <CopyableCode code="dataProductName, resourceGroupName, subscriptionId, data__keyVaultUrl" /> | Initiate key rotation on Data Product. |

## `SELECT` examples

List data products by subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_products', value: 'view', },
        { label: 'data_products', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
available_minor_versions,
consumption_endpoints,
current_minor_version,
customer_encryption_key,
customer_managed_key_encryption_enabled,
dataProductName,
documentation,
identity,
key_vault_url,
location,
major_version,
managed_resource_group_configuration,
networkacls,
owners,
private_links_enabled,
product,
provisioning_state,
public_network_access,
publisher,
purview_account,
purview_collection,
redundancy,
resourceGroupName,
resource_guid,
subscriptionId,
tags
FROM azure.network_analytics.vw_data_products
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.network_analytics.data_products
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_products</code> resource.

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
INSERT INTO azure.network_analytics.data_products (
dataProductName,
resourceGroupName,
subscriptionId,
properties,
identity,
tags,
location
)
SELECT 
'{{ dataProductName }}',
'{{ resourceGroupName }}',
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
        - name: resourceGuid
          value: string
        - name: provisioningState
          value: []
        - name: publisher
          value: string
        - name: product
          value: string
        - name: majorVersion
          value: string
        - name: owners
          value:
            - string
        - name: redundancy
          value: []
        - name: purviewAccount
          value: string
        - name: purviewCollection
          value: string
        - name: customerEncryptionKey
          value:
            - name: keyVaultUri
              value: string
            - name: keyName
              value: string
            - name: keyVersion
              value: string
        - name: networkacls
          value:
            - name: virtualNetworkRule
              value:
                - - name: id
                    value: string
                  - name: action
                    value: string
                  - name: state
                    value: string
            - name: ipRules
              value:
                - - name: value
                    value: string
                  - name: action
                    value: string
            - name: allowedQueryIpRangeList
              value:
                - string
            - name: defaultAction
              value: []
        - name: managedResourceGroupConfiguration
          value:
            - name: name
              value: string
            - name: location
              value: string
        - name: availableMinorVersions
          value:
            - string
        - name: currentMinorVersion
          value: string
        - name: documentation
          value: string
        - name: consumptionEndpoints
          value:
            - name: ingestionUrl
              value: string
            - name: ingestionResourceId
              value: string
            - name: fileAccessUrl
              value: string
            - name: fileAccessResourceId
              value: string
            - name: queryUrl
              value: string
            - name: queryResourceId
              value: string
        - name: keyVaultUrl
          value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>data_products</code> resource.

```sql
/*+ update */
UPDATE azure.network_analytics.data_products
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
dataProductName = '{{ dataProductName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>data_products</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network_analytics.data_products
WHERE dataProductName = '{{ dataProductName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
