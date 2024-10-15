---
title: providers
hide_title: false
hide_table_of_contents: false
keywords:
  - providers
  - attestation
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

Creates, updates, deletes, gets or lists a <code>providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.attestation.providers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_providers', value: 'view', },
        { label: 'providers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="attest_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="providerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="tpm_attestation_authentication" /> | `text` | field from the `properties` object |
| <CopyableCode code="trust_model" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Status of attestation service. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="providerName, resourceGroupName, subscriptionId" /> | Get the status of Attestation Provider. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns a list of attestation providers in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns attestation providers list in a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="providerName, resourceGroupName, subscriptionId, data__location, data__properties" /> | Creates or updates an Attestation Provider. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="providerName, resourceGroupName, subscriptionId" /> | Delete Attestation Service. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="providerName, resourceGroupName, subscriptionId" /> | Updates the Attestation Provider. |

## `SELECT` examples

Returns a list of attestation providers in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_providers', value: 'view', },
        { label: 'providers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
attest_uri,
location,
private_endpoint_connections,
providerName,
public_network_access,
resourceGroupName,
status,
subscriptionId,
system_data,
tags,
tpm_attestation_authentication,
trust_model
FROM azure.attestation.vw_providers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
systemData,
tags
FROM azure.attestation.providers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>providers</code> resource.

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
INSERT INTO azure.attestation.providers (
providerName,
resourceGroupName,
subscriptionId,
data__location,
data__properties,
location,
tags,
properties
)
SELECT 
'{{ providerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: publicNetworkAccess
          value: []
        - name: policySigningCertificates
          value:
            - name: keys
              value:
                - - name: alg
                    value: string
                  - name: crv
                    value: string
                  - name: d
                    value: string
                  - name: dp
                    value: string
                  - name: dq
                    value: string
                  - name: e
                    value: string
                  - name: k
                    value: string
                  - name: kid
                    value: string
                  - name: kty
                    value: string
                  - name: 'n'
                    value: string
                  - name: p
                    value: string
                  - name: q
                    value: string
                  - name: qi
                    value: string
                  - name: use
                    value: string
                  - name: x
                    value: string
                  - name: x5c
                    value:
                      - string
                  - name: 'y'
                    value: string
        - name: tpmAttestationAuthentication
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>providers</code> resource.

```sql
/*+ update */
UPDATE azure.attestation.providers
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
providerName = '{{ providerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>providers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.attestation.providers
WHERE providerName = '{{ providerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
