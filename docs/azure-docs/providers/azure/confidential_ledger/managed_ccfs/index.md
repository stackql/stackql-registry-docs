---
title: managed_ccfs
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_ccfs
  - confidential_ledger
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

Creates, updates, deletes, gets or lists a <code>managed_ccfs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_ccfs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.confidential_ledger.managed_ccfs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_ccfs', value: 'view', },
        { label: 'managed_ccfs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="appName" /> | `text` | field from the `properties` object |
| <CopyableCode code="app_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="app_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity_service_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="member_identity_certificates" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="running_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Additional Managed CCF properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appName, resourceGroupName, subscriptionId" /> | Retrieves the properties of a Managed CCF app. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieves the properties of all Managed CCF apps. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieves the properties of all Managed CCF. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="appName, resourceGroupName, subscriptionId" /> | Creates a Managed CCF with the specified Managed CCF parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appName, resourceGroupName, subscriptionId" /> | Deletes an existing Managed CCF. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="appName, resourceGroupName, subscriptionId" /> | Updates properties of Managed CCF |
| <CopyableCode code="backup" /> | `EXEC` | <CopyableCode code="appName, resourceGroupName, subscriptionId, data__uri" /> | Backs up a Managed CCF Resource. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="appName, resourceGroupName, subscriptionId, data__fileShareName, data__restoreRegion, data__uri" /> | Restores a Managed CCF Resource. |

## `SELECT` examples

Retrieves the properties of all Managed CCF.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_ccfs', value: 'view', },
        { label: 'managed_ccfs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
appName,
app_name,
app_uri,
deployment_type,
identity_service_uri,
location,
member_identity_certificates,
node_count,
provisioning_state,
resourceGroupName,
running_state,
subscriptionId,
tags
FROM azure.confidential_ledger.vw_managed_ccfs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.confidential_ledger.managed_ccfs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_ccfs</code> resource.

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
INSERT INTO azure.confidential_ledger.managed_ccfs (
appName,
resourceGroupName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ appName }}',
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
        - name: appName
          value: string
        - name: appUri
          value: string
        - name: identityServiceUri
          value: string
        - name: memberIdentityCertificates
          value:
            - - name: certificate
                value: string
              - name: encryptionkey
                value: string
              - name: tags
                value: string
        - name: deploymentType
          value:
            - name: languageRuntime
              value: []
            - name: appSourceUri
              value: string
        - name: runningState
          value: []
        - name: provisioningState
          value: []
        - name: nodeCount
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>managed_ccfs</code> resource.

```sql
/*+ update */
UPDATE azure.confidential_ledger.managed_ccfs
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
appName = '{{ appName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>managed_ccfs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.confidential_ledger.managed_ccfs
WHERE appName = '{{ appName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
